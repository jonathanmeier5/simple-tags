
from setuptools import setup, find_packages

import configparser


def get_required_packages():
    """
    Returns the packages used for install_requires
    This used to pin down every package in Pipfile.lock to the version, but that, in turn, broke
    downstream projects because it was way too strict.
    Now, this simply grabs all the items listed in the `Pipfile` `[packages]` section without version
    pinning
    """
    install_requires = []

    config = configparser.ConfigParser()
    config.read('Pipfile')

    install_requires = sorted([x for x in config['packages']])

    return install_requires


setup(
    name='simple-trainer',
    license='MIT',
    description='CLI for working with digital ocean',
    install_requires=get_required_packages(),
    author='Jonathan Meier',
    author_email='jonathan.w.meier@gmail.com',
    url='https://github.com/jonathanmeier5/do-cli',
    package_dir={'': 'src'},
    packages=['cli',],
    entry_points={
        'console_scripts': [
            'tt = cli:entrypoint',
        ],
    },
)

