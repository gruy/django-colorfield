#!/usr/bin/env python

import re

from django import forms
from django.core.validators import RegexValidator
from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

color_re = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, _('Enter a valid color.'), 'invalid')


class ColorWidget(forms.Widget):

    class Media:
        css = {
            'all': ('colorfield/css/farbtastic.css', )
            }
        js = ('colorfield/js/colorpicker.js',
              'colorfield/js/farbtastic.js', )

    def render(self, name, value, attrs=None):
        return render_to_string('colorfield/color.html', locals())


class ColorField(models.CharField):
    default_validators = [validate_color]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super(ColorField, self).formfield(**kwargs)

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^colorfield\.fields\.ColorField"])
