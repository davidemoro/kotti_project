=============
kotti_project
=============

Kotti_ is a high-level, Pythonic web application framework based on Pyramid_ and SQLAlchemy_.
It includes an extensible Content Management System called the Kotti CMS (see below).

Kotti is most useful when you are developing applications that

- have complex security requirements,
- use workflows, and/or
- work with hierarchical data.

Built on top of a number of *best-of-breed* software components,
most notably Pyramid_ and SQLAlchemy_,
Kotti introduces only a few concepts of its own,
thus hopefully keeping the learning curve flat for the developer.

.. _Kotti: http://kotti.pylonsproject.org/projects/pyramid/dev/
.. _Pyramid: http://docs.pylonsproject.org/projects/pyramid/dev/
.. _SQLAlchemy: http://www.sqlalchemy.org/

What is ``kotti_project``?
==========================
You can consider ``kotti_project`` as a meta-package or a Kotti CMS **distribution** with
the following goals:

* introduces the ``project`` concept
    * Enances the ``.ini``  and ``.txt`` setup for a structured approach suitable both for developing, 
      production or tag-based deployments. Without introducing a more complex layer like ``buildout``
* tries to be more friendly to non-Python folks who want to try out Kotti.
    * It might be difficult for non-Python developers understand things like install a virtualenv,
      activate the virtualenv and so on. That's why there is a regular ``Makefile`` that should
      make the life easier if you want to install a Kotti project and its prerequisites.

      Also ``Vagrant`` + ``Ansible`` provisioning available for an easy evaluation or automatic
      remote deployements
* third party plugins
    * includes the most useful third party plugins not included in the Kotti core,
      useful if you want to try out Kotti in a quick way
        * navigation (``kotti_navigation``)
        * events (``kotti_calendar``)
        * news (``kotti_news``)
    * you can also add other Kotti plugins published on PyPI. See https://pypi.python.org/pypi?%3Aaction=search&term=kotti&submit=search
* Kotti CMS "batteries included" installation
    * make commands for build and installation
    * right env setup
    * setup logging with logrotate enabled for production environments
    * working deploy examples (nginx, uwsgi, supervisor, database setup, etc). See the provisioning ``provisioning`` folder
      or run ``vagrant up``
    * sqlalchemy string connection examples for the most used relational databases
* Windows support
    * there is a module (``kottisvc.py``) ready to be installed as a Windows service (see http://pyramid-cookbook.readthedocs.org/en/latest/deployment/windows.html) with a file system error log handler
* scaffolding/seed tool
    * you can generate your own custom projects starting from ``kotti_project`` (eg: ``$ kotti_project_clone kotti_anotherproject``)
* project **documentation** support
    * keep track of changes and write your project documentation with Sphinx, ready to be used (http://localhost:5000/docs/, requires admin privileges)
* easy assets customization
    * ``kotti-overrides`` ready to be used (override Kotti's templates and resources)
* deploy examples
    * provides working and ready to be used real world database connection examples and deploy methods (see ``provisioning``)

Installation
============

kotti_project installation
--------------------------

For development mode::

    $ make install-prerequisites    # it performs some ``apt-get install`` commands
    $ make install-dev
    $ make run-dev

Obviously if you are going to use a non-SQLite database you'll have to install other system packages and the
needed Python driver library.

If you need more info have a look at the official doc or if you need an example you can browse the ``provisioning``
folder of bootstrap the project with ``Vagrant``.

See::

    $ make help

for further options.

Vagrant + Ansible installation
==============================

You can use the provided Vagrant + Ansible setup:

1. checkout kotti_project

2. type ``vagrant up``

3. have a coffee

At the end of the process your Kotti instance will be served here http://localhost:5000. Login with admin / qwerty.
