import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    CHANGES = ''

version = '0.1.1.dev0'

install_requires = [
    'Kotti>=0.10b1',
]

uwsgi_requires = [
    'uWSGI',
    'PasteScript',  # required by --ini-paste-logged
]

mysql_requires = [
    'MySQL-python',
    ]

postgresql_requires = [
    'psycopg2',
    ]

docs_requires = [
    'Sphinx',
    'docutils',
    'repoze.sphinx.autointerface',
    # 'sphinx_rtd_theme',
]


setup(
    name='kotti_project',
    version=version,
    description="kotti_project",
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Repoze Public License",
    ],
    author='Davide Moro',
    author_email='davide.moro@gmail.com',
    url='https://github.com/davidemoro/kotti_project',
    keywords='kotti web cms wcms pylons pyramid sqlalchemy bootstrap',
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    dependency_links=[],
    entry_points="""
      [console_scripts]
      kotti_project_clone = kotti_project.scripts:kotti_project_clone
      """,
    extras_require={
        'uwsgi': uwsgi_requires,
        'mysql': mysql_requires,
        'postgresql': postgresql_requires,
        'docs': docs_requires,
        },
)
