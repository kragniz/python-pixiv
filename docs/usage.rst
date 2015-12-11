=====
Usage
=====

To use Pixiv in a project::

    import pixiv

Example
-------

.. warning::

    This is for demonstration purposes only, and not currently functional.

.. code-block:: python

    from pixiv import login

    pixiv = login('weeb', password='hunter2')
    pixiv.me
    pixiv.me.following.works

    user = pixiv.user(171980)
    user.works
    user.favorites
