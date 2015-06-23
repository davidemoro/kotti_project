=======
Various
=======

Unordered information.

How to manage, maintain and evolve kotti_project
================================================

Available .ini files
--------------------

Describe the available .ini files.

* ``base.ini``
    * base profile
* ``development.ini`` (inherits from ``base.ini``)
    * sqlite
    * debug options ON
* ``production.ini`` (inherits from ``base.ini``)
    * real DBMS connection
    * debug options OFF

TODO: production_staging.ini and a devel configuration with a real database (the same version used on production).
Things will change...

Logging
-------

All exceptions will be logged under the exception.log file for Windows, pserve, uwsgi.
No logs with supervisord+uwsgi (TODO: to be fixed).

How to pick versions and update requirements.txt
------------------------------------------------

... of your dependencies (and your dependencies'dependencies).

So **NEVER** edit manually requirements.txt!

You SHOULD edit *both*:

* devel-requirements.txt (@develop)

* production-requirements.txt (@tag)

The ``devel-requirements.txt`` will enable your editable (-e) versioned eggs in 
development mode, the ``production-requirements.txt`` will be bound to
tags (eg: 0.1) without development extensions.

Once updated the production-requirements.txt, you can update the resulting requirements.txt
with just one command::

    $ make update-requirements

The ``production-requirements.txt`` is only a template for the final and more
readable ``requirements.txt`` file (preserve order, comments, etc).

How to tag development plugins
------------------------------

This feature requires a development setup of the project, so you should switch
to the python-dev mode.

Commands::

    (python-dev) $ cd python-dev/src/yourpackage
    (python-dev) $ fullrelease .

Be careful for private packages (say no for publishing on Pypi!).

This command will manage:

* updates the release date on ``CHANGES.txt``

* creates a tag on the repo

* optionally, publish on ``PyPI`` or other configured external services

* creates a new development version on ``CHANGES.txt`` for tracking changes

* updates the new version on ``setup.py`` (development)`.

You can and **should** tag also the ``kotti_project`` itself, this way you will be
able to easily perform tag deployements.

Many thanks to the ``zest.releaser`` guys!

How to generate new plugins
---------------------------

... with a package generator.

Kotti plugin::

    $ pcreate -s kotti kotti_yourplugin

You can see the whole list of available generators typing::

    $ pcreate -l

Once generated your plugin you should versionate it and add
a line to your ``devel-requirements.txt`` file (see "How to pick versions")
like that::

   -e git+https://github.com/.../kotti_yourplugin.git#egg=kotti_yourplugin

Once the plugin is tagged, you can register it to the ``production-requiremements.txt``
and update the final ``requirements.txt``.

Depending on the type of dependency added (generic Python library or
a framework plugin), you might need other configuration steps
(for example edit your app.ini file).

How to launch tests
-------------------

First of all you need to activate the python-dev environment.
Once activated the right environment you can go to a package and launch
tests like that::

    (python-dev) $ cd src/plugin
    (python-dev) $ py.test

or if you get errors try with::

    (python-dev) $ py.test plugin

project cloning
---------------

You can clone this existing project and create a new one with just one
command::

    $ kotti_project_clone another_project

This command will generate a new project for the pippo project. This seems the quickest
way to keep things updated (generators are too heavy to maintain).
The clone console script is based on this simple technique:

* http://davidemoro.blogspot.it/2014/09/plone-angularjs-yeoman-starter.html (see the scaffolding tool section)

Probably we'll move towards a proper scaffolding technique (contributors?).

generate project documentation
------------------------------

This documentation is automatically generated with Sphinx.

The development mode of kotti_project provides sphinx documentation.

Command::

    $ make html

You can easily generate other formats like PDF, ePUB, etc.

See:

* https://docs.python.org/devguide/documenting.html

* https://pythonhosted.org/an_example_pypi_project/sphinx.html

* http://docs.readthedocs.org/en/latest/index.html

* http://sphinx-doc.org/

Windows
=======

Build issues on Windows
-----------------------

We tried to install kotti under windows without problems, but each on the customer's
server there were some wrong compilation issues of C-based components (py-bcrypt).

We followed these resources in order to compile successfully py-bcrypt under Windows 2008
R2 server:

* https://code.google.com/p/py-bcrypt/issues/detail?id=18

* http://stackoverflow.com/questions/10773732/compilation-error-in-visual-studio-linked-with-python26

* http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat

* http://stackoverflow.com/questions/3047542/building-lxml-for-python-2-7-on-windows/5122521#5122521

* http://stackoverflow.com/questions/17108102/download-and-install-visual-studio-2008

* http://blogs.msdn.com/b/vijaysk/archive/2009/08/16/you-must-use-the-role-management-tool-to-install-or-configure-microsoft-net-framework-3-5.aspx

* https://msahputra.wordpress.com/2009/04/13/clexe-for-vc9-visual-studio-2008/
  (copy mspdb80.dll and run vsvars32.bat)

* Still same situation described in #18

* https://code.google.com/p/py-bcrypt/issues/detail?id=15

* Plus added missing stdint.h
  http://msinttypes.googlecode.com/svn/trunk/stdint.h

MySQL issues on Windows
-----------------------

MySQL on Windows need additional options in order to avoid the following errors:

* InterfaceError
* OperationalError
* MySQL Server has gone away
* etc

You could adjust the mysql options like that::

    [mysqld]
    max_allowed_packet = 1000MB    # max transaction allowed
    wait_timeout = 28800
    interactive_timeout = 2880

Windows service
---------------

This software is installed as a regular windows service (kottisvc.py).

See:

* http://pyramid-cookbook.readthedocs.org/en/latest/deployment/windows.html

We have associated a file system exception log (with autorotate option) to the windows service. 

Deployements
------------

You can adopt a tagged-based deploy system.
I assume you are following a tag based deployement (on Windows c:\..\kotti_project\python\Scripts\activate).

First of all activate the production virtualenv::

    $ source python/bin/activate

And then::

    $ git fetch
    $ git checkout tags/X.Y.Z
    $ pip install -r requirements.txt

If you don't want to do things by hand, have a look at the ``provisioning`` folder: you'll find what you need to setup
a deploy based on Ansible.
