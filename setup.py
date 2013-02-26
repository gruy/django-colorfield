from setuptools import setup, find_packages

setup(name='django-colorfield',
      version='1.0',
      description='A simple Django application to integrate ColorField into your models.',
      author='Ruslan Popov',
      author_email='ruslan.popov@gmail.com',
      url='http://github.com/RaD/django-colorfield/tree/master',
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: OS Independent',
          'Topic :: Software Development'
      ],
      )
