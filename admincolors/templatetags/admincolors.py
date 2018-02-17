from django import template

register = template.Library()


@register.inclusion_tag('admincolors/templatetags/breadcrumbs.html')
def colors_breadcrumbs(theme, themes):
    return {
        'themes': themes,
        'theme': theme
    }


@register.inclusion_tag('admincolors/templatetags/scripts.html')
def colors_scripts():
    return {}


@register.inclusion_tag('admincolors/templatetags/styles.html')
def colors_styles(theme, themes):
    return {
        'themes': themes,
        'theme': theme
    }
