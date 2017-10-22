# This file is autogenerated by medikit code generator.
# All changes will be overwritten.

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Py3 compatibility hacks, borrowed from IPython.
try:
    execfile
except NameError:

    def execfile(fname, globs, locs=None):
        locs = locs or globs
        exec(compile(open(fname).read(), fname, "exec"), globs, locs)


# Get the long description from the README file
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

# Get the classifiers from the classifiers file
tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))
try:
    with open(path.join(here, 'classifiers.txt'), encoding='utf-8') as f:
        classifiers = tolines(f.read())
except:
    classifiers = []

version_ns = {}
try:
    execfile(path.join(here, 'django_includes/_version.py'), version_ns)
except EnvironmentError:
    version = 'dev'
else:
    version = version_ns.get('__version__', 'dev')

setup(
    author='Romain Dorgueil',
    author_email='romain@dorgueil.net',
    description=(
        'Include django views as a subparts of other django views, using either HTTP '
        '(with esi or hinclude) or direct render.'
    ),
    license='Apache License, Version 2.0',
    name='django_includes',
    version=version,
    long_description=long_description,
    classifiers=classifiers,
    packages=find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data=True,
    install_requires=[
        'CacheControl (>= 0.11, < 0.12)', 'PyJWT (>= 1.4, < 1.5)', 'django', 'edgy.event (>= 0.1, < 0.2)',
        'jinja2 (>= 2.8, < 3.0)', 'requests (>= 2, < 3)'
    ],
    extras_require={'dev': ['coverage (>= 4.4, < 5.0)', 'pytest (>= 3.1, < 4.0)', 'pytest-cov (>= 2.5, < 3.0)']},
    url='https://github.com/hartym/django-includes',
    download_url='https://github.com/hartym/django-includes/archive/{version}.tar.gz'.format(version=version),
)
