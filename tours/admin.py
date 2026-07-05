from django.contrib import admin
from .models import Destination, Package, ItineraryDay, DayTrip, Testimonial, ContactMessage


class ItineraryDayInline(admin.TabularInline):
    model = ItineraryDay
    extra = 1


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "featured", "order")
    list_editable = ("featured", "order")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "duration_days", "price_from_usd", "featured", "order")
    list_editable = ("featured", "order")
    list_filter = ("category", "featured")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary")
    filter_horizontal = ("destinations",)
    inlines = [ItineraryDayInline]


@admin.register(DayTrip)
class DayTripAdmin(admin.ModelAdmin):
    list_display = ("title", "price_from_usd", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author_name", "author_country", "rating", "featured", "created_at")
    list_editable = ("featured",)
    list_filter = ("featured", "rating")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "package_interest", "handled", "created_at")
    list_editable = ("handled",)
    list_filter = ("handled", "created_at")
    readonly_fields = ("name", "email", "phone", "package_interest", "message", "created_at")


admin.site.site_header = "Safari Travels Admin"
admin.site.site_title = "Safari Travels Admin"
admin.site.index_title = "Manage site content"
