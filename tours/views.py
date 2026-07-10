from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Destination, Package, DayTrip, Testimonial
from .forms import ContactForm


def home(request):
    context = {
        "destinations": Destination.objects.filter(featured=True)[:6],
        "packages": Package.objects.filter(featured=True)[:4],
        "day_trips": DayTrip.objects.all()[:4],
        "testimonials": Testimonial.objects.filter(featured=True)[:6],
    }
    return render(request, "tours/home.html", context)


def package_list(request):
    packages = Package.objects.all()
    category = request.GET.get("category")
    if category:
        packages = packages.filter(category=category)
    context = {
        "packages": packages,
        "categories": Package.CATEGORY_CHOICES,
        "active_category": category,
    }
    return render(request, "tours/package_list.html", context)


def package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug)
    related = Package.objects.exclude(pk=package.pk).filter(category=package.category)[:3]
    context = {"package": package, "related": related}
    return render(request, "tours/package_detail.html", context)


def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, "tours/destination_list.html", {"destinations": destinations})


def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    packages = destination.packages.all()
    context = {"destination": destination, "packages": packages}
    return render(request, "tours/destination_detail.html", context)


def day_trip_list(request):
    day_trips = DayTrip.objects.all()
    return render(request, "tours/day_trip_list.html", {"day_trips": day_trips})


def about(request):
    return render(request, "tours/about.html")


def robots_txt(request):
    from django.http import HttpResponse
    from django.conf import settings
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        f"Sitemap: {settings.SITE_DOMAIN}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def privacy_policy(request):
    return render(request, "tours/privacy_policy.html")


def terms(request):
    return render(request, "tours/terms.html")


def contact(request):
    initial = {}
    package_interest = request.GET.get("package")
    if package_interest:
        initial["package_interest"] = package_interest

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Asante! Your message has been received — our team will reach out shortly."
            )
            return redirect("tours:contact")
    else:
        form = ContactForm(initial=initial)

    return render(request, "tours/contact.html", {"form": form})
