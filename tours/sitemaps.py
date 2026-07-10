from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Package, Destination, DayTrip


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return ["tours:home", "tours:package_list", "tours:destination_list",
                "tours:day_trip_list", "tours:about", "tours:contact"]

    def location(self, item):
        return reverse(item)


class PackageSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"

    def items(self):
        return Package.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class DestinationSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return Destination.objects.all()


class DayTripSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return DayTrip.objects.all()

    def location(self, item):
        return reverse("tours:day_trip_list")
