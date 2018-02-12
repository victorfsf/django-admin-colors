from django.contrib.admin import AdminSite
from django.conf import settings


class AdminColorsSite(AdminSite):

    index_template = 'admincolors/index.html'

    def each_context(self, request):
        context = super().each_context(request)
        if getattr(settings, 'ADMIN_COLORS', None):
            context.update({
                'themes': [
                    ('Default', ''),
                ] + settings.ADMIN_COLORS
            })
        return context
