#!/usr/bin/env python

# Copyright 2012 refnode
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# symbols exported for 'from xyz import *'
# __all__ = []

# import std
import os
from os import path
import sys
# import third party
try:
    from setuptools import setup, find_packages
except ImportError:
    try:
        from ez_setup import use_setuptools
    except ImportError:
        print "can't find ez_setup"
        print "try: wget http://peak.telecommunity.com/dist/ez_setup.py"
        sys.exit(1)
    use_setuptools()
    from setuptools import setup, find_packages

if sys.version_info < (2, 6):
    print "pyliquid only supports Python 2.6 and higher"
    sys.exit(1)


def get_version():
    return '0.1'

setup(
    name='pyliquid',
    version=get_version(),
    description="pyliquid",
    long_description=open('README.rst').read(),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='pyliquid',
    author='refnode',
    author_email='refnode@gmail.com',
    url='https://github.com/refnode/pyliquid',
    license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
    namespace_packages=['pyliquid'],
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools'
    ],
    entry_points = {
        "console_scripts": [
            "pyliquid = pyliquid.tools.shell:main"
        ]
    }
)
