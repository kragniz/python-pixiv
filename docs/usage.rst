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
    pixiv.me.following

    user = pixiv.user(171980)

    for work in user.works:
        print(work.title)

    user.favorites
