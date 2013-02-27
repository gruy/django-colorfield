Django Colorfield
---------------------

This module fills the need of having a 'colorfield' that's usable in both
django models and forms.

Just install this application into virtual environment.

Add 'colorfield' into INSTALLED_APPS.

Usage::

    from colorfield.fields import ColorField

    class SomeModel(models.Model):
        value = ColorField(default='#fff', verbose_name=_(u'Value, in HEX'))

That's all!
