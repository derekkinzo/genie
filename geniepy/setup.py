"""Package setup module for setuptools package generation."""
from setuptools import setup, find_packages

__version__ = "0.2"
setup(
    version=__version__,
    name="GeniePy",
    description="Gene-disease trend detection",
    license="MIT",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="The Harvard LAMP Team",
    maintainer_email="dhk891@g.harvard.edu",
    url="https://github.com/derekkinzo/genie",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["jsonlines"],
    python_requires=">=3.7",
    keywords="gene disease trend detection",
)
