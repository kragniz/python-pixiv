============
python-pixiv
============

.. image:: https://img.shields.io/pypi/v/pixiv.svg
        :target: https://pypi.python.org/pypi/pixiv

.. image:: https://img.shields.io/travis/kragniz/python-pixiv.svg
        :target: https://travis-ci.org/kragniz/python-pixiv

.. image:: https://ci.appveyor.com/api/projects/status/github/kragniz/python-pixiv?svg=true
        :target: https://ci.appveyor.com/project/kragniz/pixiv

.. image:: https://readthedocs.org/projects/pixiv/badge/?version=latest
        :target: https://pixiv.readthedocs.org
        :alt: Documentation Status

 .. image:: https://badge.waffle.io/kragniz/python-pixiv.png?label=ready&title=Ready 
 :target: https://waffle.io/kragniz/python-pixiv
 :alt: 'Stories in Ready'


python-pixiv: Pixiv API client for moe girls.

* Free software: LGPLv3
* Documentation: https://pixiv.readthedocs.org.
* Contribute: https://github.com/kragniz/python-pixiv

python-pixiv supports and runs continuous tests for python 2.7, 3.4 and 3.5, and PyPy. Tests are run on both Linux and Windows.

Quickstart
----------

Install python-pixiv:

.. code-block:: bash

    $ pip install pixiv

Login to pixiv:

.. code-block:: python

    from pixiv import login

    pixiv = login('username', 'password')

Save the work from a particular user:

.. code-block:: python

    user = pixiv.user(7631951)

    for art in user.works():
        art.save()

See the `full documentation <https://pixiv.readthedocs.org>`_ for more!
