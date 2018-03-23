from collections import OrderedDict
from django.conf import settings
from django.urls import reverse


def admin_theme(request):
    context = {}
    if request.path.startswith(reverse('admin:index')):
        if getattr(settings, 'ADMIN_COLORS', None):
            theme_list = [
                (x, y if isinstance(y, (list, tuple)) else (y, ))
                for x, y in settings.ADMIN_COLORS
            ]
            themes = OrderedDict(theme_list)
            if themes:
                first = theme_list[0][0]
                default = getattr(
                    settings, 'ADMIN_COLORS_BASE_THEME', first
                )
                context.update({
                    'themes': themes,
                    'theme': themes.get(
                        request.COOKIES.get('theme') or default
                    ) or themes.get(first)
                })
    return context
