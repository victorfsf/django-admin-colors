from django.contrib.admin import AdminSite


class AdminColorsSite(AdminSite):

    index_template = 'admincolors/index.html'
