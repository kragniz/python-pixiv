=====
Usage
=====

To use Pixiv in a project:

.. code-block:: python

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

    for art in user.works():
        # save the artwork to the currect working directory
        art.save()
