#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

setup(
    name='requests-facebook',
    version='0.4.1',
    install_requires=['requests>=1.0.0'],
    author='Mike Helmick',
    author_email='me@michaelhelmick.com',
    license='BSD',
    url='https://github.com/michaelhelmick/requests-facebook/',
    keywords='python facebook requests graph oauth oauth2 api',
    description='A Python Library to interface with Facebook Graph API',
    long_description=open('README.rst').read(),
    download_url='https://github.com/michaelhelmick/requests-facebook/zipball/master',
    py_modules=['facebook'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
