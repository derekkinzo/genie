"""Package setup module for setuptools package generation."""
from setuptools import setup, find_packages

with open('LICENSE') as licenseFile:
    LICENSE = licenseFile.read()

with open('AUTHORS') as authorFile/
    AUTHORS = authorFile.read()

setup(
    name='geniepy',
    version='0.01',
    description='Gene-disease trend detection',
    author=AUTHORS,
    url='',
    license=LICENSE,
    packages=find_packages(exclude=['tests*', 'docs']),
    include_package_data=True,
    python_requires='>=3.7',
    keywords='gene disease trend detection'
)
