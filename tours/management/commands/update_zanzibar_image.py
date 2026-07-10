"""
One-off fix: update the Zanzibar Destination and '4 Days Zanzibar Holiday'
Package to use a real Zanzibar beach photo instead of the old placeholder.

Safe to run multiple times. Run on the LIVE database with:
    python manage.py update_zanzibar_image
"""
from django.core.management.base import BaseCommand
from tours.models import Destination, Package

NEW_IMAGE = "https://images.unsplash.com/photo-1665449417444-fe7fec4b7425?w=900&q=70"


class Command(BaseCommand):
    help = "Patch the Zanzibar destination and package to use a real beach photo."

    def handle(self, *args, **options):
        updated = 0

        dest = Destination.objects.filter(slug="zanzibar").first()
        if dest:
            dest.image = NEW_IMAGE
            dest.image_upload = None
            dest.save()
            updated += 1
            self.stdout.write(self.style.SUCCESS("Updated Zanzibar destination image"))
        else:
            self.stdout.write(self.style.WARNING("Zanzibar destination not found — skipped"))

        pkg = Package.objects.filter(slug="4-days-zanzibar-holiday").first()
        if pkg:
            pkg.image = NEW_IMAGE
            pkg.image_upload = None
            pkg.save()
            updated += 1
            self.stdout.write(self.style.SUCCESS("Updated 4 Days Zanzibar Holiday package image"))
        else:
            self.stdout.write(self.style.WARNING("Zanzibar package not found — skipped"))

        self.stdout.write(self.style.SUCCESS(f"Done. {updated} record(s) updated."))
