# Installation

## Install with pip
```
pip install geniepy
```

## Install from source code
```
git clone https://github.com/derekkinzo/genie.git

cd genie/geniepy

python setup.py install
```

## Python Package

Generate python package and upload do PyPi:

```
python setup.py sdist bdist_wheel

twine upload dist/*
```
