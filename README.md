# Django Admin Colors

Customizing the Django Admin's CSS (mostly its colors)


## Installing

```bash
pip install django-admin-colors
```

## Configuring

The following instructions are necessary to make `django-admin-colors` work.

### Configure your `settings.py`

```python

INSTALLED_APPS = [
    ...,
    'admincolors'
]

# These are the "builtin" django-admin-colors themes
ADMIN_COLORS = [
    ('Lite', 'admincolors/css/lite.css'),
    ('Dark Blue', 'admincolors/css/dark-blue.css'),
    ('Gray', 'admincolors/css/gray.css')
]

# TEMPLATES configuration
# PS: Don't override your current settings,
#     copy or change only what's necessary
TEMPLATES = [
    {
        ...,
        'DIRS': [
            # IMPORTANT: needed to override the django admin's base templates.
            os.path.join(BASE_DIR, 'templates')
        ],
        # IMPORTANT: needed to load admincolors' templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ...,
                # IMPORTANT: needed to make the "theme" and "themes" context
                #            variables available for the templates
                'admincolors.context_processors.admin_theme'
            ],
        },
    },
]
```

### Configure your admin templates

Create a new folder: `BASE_DIR/templates`.

### admin/base_site.html

#### Completely override the `base_site.html` template

File: `BASE_DIR/templates/admin/base_site.html`

```html
{% extends 'admincolors/base_site.html' %}
```

#### Alternatively, overwrite the file `admin/base_site.html` yourself

File: `BASE_DIR/templates/admin/base_site.html`

```html
{% extends "admin/base.html" %}
{% load admincolors i18n static %}

{% block title %}
{{ title }} | {{ site_title|default:_('Django site admin') }}
{% endblock %}

{% block blockbots %}
{{ block.super }}

{% colors_styles theme %}

{% endblock %}

{% block branding %}
<h1 id="site-name">
    <a href="{% url 'admin:index' %}">
        {{ site_header|default:_('Django administration') }}
    </a>
</h1>
{% endblock %}

{% block nav-global %}{% endblock %}

{% block footer %}
{{ block.super }}

{% colors_scripts %}

{% endblock %}
```

### admin/index.html

#### Completely override the `index.html` template

File: `BASE_DIR/templates/admin/index.html`

```html
{% extends 'admincolors/index.html' %}
```

#### Alternatively, overwrite the file `admin/index.html` yourself

File: `BASE_DIR/templates/admin/index.html`

PS: Most of the file was ignored,
[check the Django's repository](`https://github.com/django/django/blob/master/django/contrib/admin/templates/admin/index.html`)
to see the full `index.html` file.

```html
{% extends "admin/base_site.html" %}
{% load admincolors static i18n %}
...

{% block breadcrumbs %}
<div class="breadcrumbs">

{% colors_breadcrumbs theme themes %}

</div>
{% endblock %}

...
```

### Help

See the Django's documentation about:

- [Overrinding templates](https://docs.djangoproject.com/en/2.0/howto/overriding-templates/)
- [The Django admin site](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/)

## Examples

![Default](https://github.com/victorfsf/django-admin-colors/raw/master/screenshots/default.png)
![Lite](https://github.com/victorfsf/django-admin-colors/raw/master/screenshots/lite.png)
![Dark Blue](https://github.com/victorfsf/django-admin-colors/raw/master/screenshots/darkblue.png)
![Gray](https://github.com/victorfsf/django-admin-colors/raw/master/screenshots/gray.png)
