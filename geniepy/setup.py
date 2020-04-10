"""Package setup module for setuptools package generation."""
from setuptools import setup, find_packages

setup(
    name="geniepy",
    version="0.0.3",
    description="Gene-disease trend detection",
    long_description=open("README.md", "r").read(),
    author=open("AUTHORS", "r").read(),
    url="https://github.com/derekkinzo/genie",
    license=open("LICENSE", "r").read(),
    packages=find_packages(exclude=["tests*", "docs"]),
    include_package_data=True,
    install_requires=["jsonlines"],
    python_requires=">=3.7",
    keywords="gene disease trend detection",
)
