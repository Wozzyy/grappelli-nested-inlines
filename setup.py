# Imports from python.  # NOQA
import os
from setuptools import find_packages
from setuptools import setup


# Imports from grappelli-nested.
from grappelli_nested import __version__


REPO_URL = 'https://github.com/allanjamesvestal/grappelli-nested-inlines/'

PYPI_VERSION = '.'.join(str(v) for v in __version__)

DESCRIPTION = 'Enables nested inlines in the Django/Grappelli admin'


setup(
    name='grappelli-nested-inlines',
    version=PYPI_VERSION,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT License',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    url=REPO_URL,
    download_url=f'{REPO_URL}archive/{PYPI_VERSION}.tar.gz',
    author='Allan James Vestal (based on code by Alain Trinh)',
    author_email='allanjamesvestal@gmail.com',
    install_requires=[
        'Django>=3.2',
        'django-grappelli>=2.15',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
