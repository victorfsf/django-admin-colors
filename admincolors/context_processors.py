from django.conf import settings
from django.urls import reverse


def admin_theme(request):
    context = {}
    if request.path.startswith(reverse('admin:index')):
        context.update({
            'theme': request.COOKIES.get('theme', None)
        })
        if getattr(settings, 'ADMIN_COLORS', None):
            context.update({
                'themes': [
                    ('Default', ''),
                ] + settings.ADMIN_COLORS
            })
    return context
