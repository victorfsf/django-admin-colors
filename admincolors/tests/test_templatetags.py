from admincolors.templatetags.admincolors import register
from admincolors.templatetags.admincolors import colors_breadcrumbs
from admincolors.templatetags.admincolors import colors_scripts
from admincolors.templatetags.admincolors import colors_styles
from django.template import engines
from django.template.loader import render_to_string
from django.test import TestCase


class TestTemplateTags(TestCase):

    def setUp(self):
        self.engine = engines['django']

    def test_colors_breadcrumbs(self):
        fn_input = ('test1', [('Test1', 'test1.css'), ('Test2', 'test2.css')])
        self.assertTrue('colors_breadcrumbs' in register.tags)
        self.assertEqual(
            colors_breadcrumbs(*fn_input), {
                'theme': fn_input[0], 'themes': fn_input[1]
            }
        )

    def test_colors_scripts(self):
        self.assertTrue('colors_scripts' in register.tags)
        self.assertEqual(
            colors_scripts(),
            {}
        )

    def test_colors_styles(self):
        fn_input = ('test1', [('Test1', 'test1.css'), ('Test2', 'test2.css')])
        self.assertTrue('colors_styles' in register.tags)
        self.assertEqual(
            colors_styles(*fn_input), {
                'theme': fn_input[0], 'themes': fn_input[1]
            }
        )

    def test_breadcrumbs_render(self):
        context = {
            'theme': 'test1',
            'themes': [
                ('Test1', 'test1.css'),
                ('Test2', 'test2.css'),
                ('Test3', 'test3.css')
            ]
        }
        template = self.engine.from_string(
            '{% load admincolors %}{% colors_breadcrumbs theme themes %}'
        )
        self.assertEqual(
            template.render(context),
            render_to_string(
                'admincolors/templatetags/breadcrumbs.html', context
            )
        )
        self.assertEqual(template.render({'theme': context['theme']}), '\n')
        self.assertEqual(template.render(), '\n')

    def test_scripts_render(self):
        self.assertEqual(
            self.engine.from_string(
                '{% load admincolors %}{% colors_scripts %}'
            ).render(),
            render_to_string('admincolors/templatetags/scripts.html')
        )

    def test_styles_render(self):
        context = {
            'theme': 'test1',
            'themes': [
                ('Test1', 'test1.css'),
                ('Test2', 'test2.css'),
                ('Test3', 'test3.css')
            ]
        }
        template = self.engine.from_string(
            '{% load admincolors %}{% colors_styles theme themes %}'
        )
        self.assertEqual(
            template.render(context),
            render_to_string(
                'admincolors/templatetags/styles.html', context
            )
        )
        self.assertEqual(template.render(), render_to_string(
            'admincolors/templatetags/styles.html'
        ))
