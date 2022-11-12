from django.conf import settings


def sekura(request):
    return {
        "SEKURA": settings.SEKURA
    }
