from django.db import models
from django.urls import reverse


class Destination(models.Model):
    """A national park / place featured in the popular destinations list."""
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    short_description = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True, help_text="Image URL (or upload via admin file field below)")
    image_upload = models.ImageField(upload_to="destinations/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image_upload:
            return self.image_upload.url
        return self.image

    def get_absolute_url(self):
        return reverse("tours:destination_detail", kwargs={"slug": self.slug})


class ItineraryDay(models.Model):
    """A single day within a multi-day Package, used for the journey timeline."""
    package = models.ForeignKey("Package", on_delete=models.CASCADE, related_name="itinerary_days")
    day_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ["day_number"]

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"


class Package(models.Model):
    """A multi-day tour package, e.g. '5 Days Northern Circuit Safari'."""
    CATEGORY_CHOICES = [
        ("safari", "Safari"),
        ("trekking", "Mountain Trekking"),
        ("beach", "Beach Holiday"),
        ("cultural", "Cultural Experience"),
        ("custom", "Customized Package"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="safari")
    duration_days = models.PositiveIntegerField(help_text="Number of days")
    price_from_usd = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    highlights = models.TextField(
        blank=True,
        help_text="One highlight per line, e.g. 'Big Five game drives'"
    )
    image = models.URLField(blank=True)
    image_upload = models.ImageField(upload_to="packages/", blank=True, null=True)
    destinations = models.ManyToManyField(Destination, blank=True, related_name="packages")
    featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "duration_days"]

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image_upload:
            return self.image_upload.url
        return self.image

    def highlight_list(self):
        return [h.strip() for h in self.highlights.splitlines() if h.strip()]

    def get_absolute_url(self):
        return reverse("tours:package_detail", kwargs={"slug": self.slug})


class DayTrip(models.Model):
    """A single-day excursion, e.g. 'Materuni Waterfalls Day Trip'."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    summary = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    price_from_usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.URLField(blank=True)
    image_upload = models.ImageField(upload_to="daytrips/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image_upload:
            return self.image_upload.url
        return self.image


class Testimonial(models.Model):
    author_name = models.CharField(max_length=120)
    author_country = models.CharField(max_length=100, blank=True)
    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.author_name} ({self.rating}★)"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    package_interest = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.created_at:%Y-%m-%d}"
