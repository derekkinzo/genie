"""Package setup module for setuptools package generation."""
from setuptools import setup, find_packages

__version__ = "0.0.5"
setup(
    name="geniepy",
    version=__version__,
    description="Gene-disease trend detection",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["jsonlines"],
    python_requires=">=3.7",
    keywords="gene disease trend detection",
)
