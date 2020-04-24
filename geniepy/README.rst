=======
GeniePy
=======


Gene-Disease relationship trend detection application.


.. note::

    Python package available on PyPi_

    Project documentation here_



Installation
============

**Install with pip**

Install from PyPi_ with pip


::

    pip install geniepy


**Install from source code**

Install using setuptools locally

::

    git clone https://github.com/derekkinzo/genie.git
    cd genie/geniepy
    python setup.py install


**Run Source Code**

Create virtual environment, and run code

::

    python3 -m venv .venv
    source .venv/bin/activate (for windows: source .venv/scripts/activate)
    pip install -r requirements.txt


**Python Package Development**

Setuptools commands to test, generate docs, and install for development (creates symlink)

::

    python setup.py test
    python setup.py docs
    python setup.py develop


**Generate Python Package**

Commands to generate python package and upload it to PyPi (setup PyPi account and .profile first)

::

    git tag -a {version}
    python setup.py sdist bdist_wheel
    twine upload --repository testpypi dist/{package name}
    twine upload dist/{package name}



.. _PyPi: https://pypi.org/project/geniepy/
.. _here: https://geniepy.readthedocs.io/en/latest/