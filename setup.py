#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.search.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
version = open("VERSION").read()
desc = open("README.md").read()

setup(
    python_requires='>3',
    name='mapzen.whosonfirst.search',
    namespace_packages=['mapzen', 'mapzen.whosonfirst'],
    version=version,
    description='Simple Python wrapper for Who\'s On First search functionality',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-search',
    packages=packages,
    scripts=[
        'scripts/wof-es-id',
        'scripts/wof-es-index',
        'scripts/wof-es-index-files',
        'scripts/wof-es-index-filelist',                
        'scripts/wof-es-prepare',
        'scripts/wof-es-rawquery',
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-search/releases/tag/' + version,
    license='BSD')
