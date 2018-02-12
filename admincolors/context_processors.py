from django.urls import reverse


def admin_theme(request):
    if request.path.startswith(reverse('admin:index')):
        return {
            'theme': request.COOKIES.get('theme', None)
        }
