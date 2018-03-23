from setuptools import find_packages, setup
import os

version = '0.2.0'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-admin-colors',
    version=version,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT License',
    description='Customizable Django admin themes',
    long_description=README,
    url='https://github.com/victorfsf/django-admin-colors',
    author='Victor Ferraz',
    author_email='victorfsf.dev@gmail.com',
    zip_safe=False,
    keywords=[
        'django',
        'django-admin',
        'python3',
        'python3.6',
        'colors',
        'themes',
        'django-admin-colors',
        'django-admin-themes'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
