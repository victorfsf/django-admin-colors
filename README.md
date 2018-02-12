# Django Admin Colors

[![PyPI version](https://badge.fury.io/py/django-admin-colors.svg)](https://badge.fury.io/py/django-admin-colors)
[![Build Status](https://circleci.com/gh/victorfsf/django-admin-colors/tree/master.svg?style=shield)](https://circleci.com/gh/victorfsf/django-admin-colors)
[![Coverage Status](https://coveralls.io/repos/github/victorfsf/django-admin-colors/badge.svg)](https://coveralls.io/github/victorfsf/django-admin-colors)
[![Code Health](https://landscape.io/github/victorfsf/django-admin-colors/master/landscape.svg?style=flat)](https://landscape.io/github/victorfsf/django-admin-colors/master)

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

#### admin/base_site.html

##### Completely override the `base_site.html` template

File: `BASE_DIR/templates/admin/base_site.html`

```html
{% extends 'admincolors/base_site.html' %}
```

##### Alternatively, overwrite the file `admin/base_site.html` yourself

File: `BASE_DIR/templates/admin/base_site.html`

PS: Most of the file was ignored,
[check the Django repository](`https://github.com/django/django/blob/master/django/contrib/admin/templates/admin/base_site.html`)
to see the full `base_site.html` file.

```html
{% extends "admin/base.html" %}
{% load admincolors i18n static %}

...

{% block blockbots %}
{{ block.super }}

{% colors_styles theme %}

{% endblock %}

...

{% block footer %}
{{ block.super }}

{% colors_scripts %}

{% endblock %}

...
```

#### admin/index.html

##### Completely override the `index.html` template

File: `BASE_DIR/templates/admin/index.html`

```html
{% extends 'admincolors/index.html' %}
```

##### Alternatively, overwrite the file `admin/index.html` yourself

File: `BASE_DIR/templates/admin/index.html`

PS: Most of the file was ignored,
[check the Django repository](`https://github.com/django/django/blob/master/django/contrib/admin/templates/admin/index.html`)
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

## Custom themes

To add a custom theme, simply create a `.css file` anywhere in your static files, then add its full path (and the theme's name) to the `ADMIN_COLORS` variable in `settings.py`:

```python
ADMIN_COLORS = [
    ...,
    ('My Theme', 'path/to/my/theme.css')
]
```

## Help

See the Django documentation about:

- [Overrinding templates](https://docs.djangoproject.com/en/2.0/howto/overriding-templates/)
- [The Django admin site](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/)

## Examples

##### The default django admin look
![Default](https://github.com/victorfsf/django-admin-colors/raw/master/screenshots/default.png)
##### The `Lite` theme
![Lite](https://github.com/victorfsf/django-admin-colors/raw/master/screenshots/lite.png)
##### The `Dark Blue` theme
![Dark Blue](https://github.com/victorfsf/django-admin-colors/raw/master/screenshots/darkblue.png)
##### The `Gray` theme
![Gray](https://github.com/victorfsf/django-admin-colors/raw/master/screenshots/gray.png)
