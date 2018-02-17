from collections import OrderedDict
from django.conf import settings
from django.urls import reverse


def admin_theme(request):
    context = {}
    if request.path.startswith(reverse('admin:index')):
        if getattr(settings, 'ADMIN_COLORS', None):
            themes = OrderedDict([
                (x, y if isinstance(y, (list, tuple)) else (y, ))
                for x, y in settings.ADMIN_COLORS
            ])
            context.update({
                'themes': themes,
                'theme': themes.get(
                    request.COOKIES['theme']
                ) if 'theme' in request.COOKIES else 'Default'
            })
    return context
