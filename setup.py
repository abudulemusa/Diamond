#!/usr/bin/env python

import os
from glob import glob

if os.environ.get('USE_SETUPTOOLS'):
    from setuptools import setup
    setup_kwargs = dict(zip_safe=0)
else:
    from distutils.core import setup
    setup_kwargs = dict()

data_files=[
    ('/etc/diamond',                           glob('conf/*.conf*') ),
    ('/etc/diamond/collectors',                glob('conf/collectors/*') ),
    ('share/diamond/collectors',               glob('src/collectors/*.py') ),
    ('share/diamond/collectors/user_scripts',  [] ),
    ('share/diamond/collectors/contrib',       glob('contrib/*.py') ),
]
for path in glob('contrib/*/'):
    data_files.append(('share/diamond/collectors'+path, glob(path+'/*')))

setup(
    name            = 'diamond',
    version         = '0.2.0',
    url             = 'https://github.com/BrightcoveOS/Diamond',
    author          = 'The Diamond Team',
    author_email    = '',
    license         = 'MIT License',
    description     = 'Smart data producer for graphite graphing package',
    package_dir     = {'' : 'src'},
    packages        = ['diamond'],
    scripts         = glob('bin/*'),
    data_files      = data_files,
    **setup_kwargs
)
