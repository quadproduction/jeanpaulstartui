from os import path
from setuptools import setup, find_packages


NAME = 'jeanpaulstartui'
DESCRIPTION = 'Launcher Ui'
AUTHOR = 'Cube Creative'
AUTHOR_EMAIL = 'development@cube-creative.com'
LONG_DESCRIPTION = """Launcher Ui"""

_here = path.abspath(path.dirname(__file__))
_readme_filepath = path.join(_here, 'README.md')
_requirements_filepath = path.join(_here, 'requirements.txt')
_version_filepath = path.join(_here, NAME, 'version.py')


_version_namespace = {}
with open(_version_filepath) as version_file:
    exec(version_file.read(), _version_namespace)

VERSION = _version_namespace['__version__']


if path.isfile(_requirements_filepath):
    with open(_requirements_filepath) as requirements_file:
        _requirements = requirements_file.readlines()
else:
    _requirements = list()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(exclude=['tests']),
    install_requires=_requirements,
    include_package_data=True
)
