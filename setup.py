# -*- coding: utf-8 -*-
from setuptools import setup
import logfilter

setup(
    name=logfilter.__name__,
    version=logfilter.__version__,
    description=logfilter.__description__,
    long_description=logfilter.__doc__,
    classifiers=logfilter.__classifiers__,
    author=logfilter.__author__,
    author_email=logfilter.__author_email__,
    license=logfilter.__license__,
    platforms=['any'],
    keywords=['log','filter'],
    url='http://bitbucket.org/shimizukawa/logfilter/',
    package_dir={'': '.'},
    py_modules = ['logfilter'],
    install_requires=[
        'setuptools',
         # -*- Extra requirements: -*-
    ],
    entry_points="""
        [console_scripts]
        logfilter = logfilter:main
    """,
)
