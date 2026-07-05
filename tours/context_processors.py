from django.conf import settings


def site_settings(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_PHONE_PRIMARY": settings.SITE_PHONE_PRIMARY,
        "SITE_PHONE_SECONDARY": settings.SITE_PHONE_SECONDARY,
        "SITE_WHATSAPP": settings.SITE_WHATSAPP,
        "SITE_EMAIL": settings.SITE_EMAIL,
        "SITE_LOCATION": settings.SITE_LOCATION,
        "SITE_INSTAGRAM": settings.SITE_INSTAGRAM,
        "SITE_FACEBOOK": settings.SITE_FACEBOOK,
        "SITE_THREADS": settings.SITE_THREADS,
    }
