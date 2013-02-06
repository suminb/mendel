from setuptools import setup
from distutils.command.install import install
from mendel.version import __version__

import os

class install_bin(install):
    """Installs executable binaries."""

    def run(self):
        pass


setup(
    name='mendel',
    version=__version__,
    author='Sumin Byeon',
    author_email='suminb@gmail.com',
    description='Command line tool to convert a Markdown document into an HTML document',
    license='LGPL',
    keywords='',
    url='https://github.com/suminb/mendel',
    packages=['mendel'],
    #scripts=['bin/mendel'],
    entry_points={
        'console_scripts':
            ['mendel = mendel:main'],
    },
    long_description=open('README.md').read(),
    install_requires=['markdown2', 'docopt'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: LGPL',
    ],
    #cmdclass={'install': install_bin},
)