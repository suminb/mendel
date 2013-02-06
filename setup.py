from setuptools import setup
from markdown import __version__

import distutils.cmd

class install_bin(distutils.cmd.Command):
    """Installs executable binaries."""

    def run(self):
        pass

setup(
    name='markdown',
    version=__version__,
    author='Sumin Byeon',
    author_email='suminb@gmail.com',
    description='Command line tool to convert a Markdown document into an HTML document',
    license='LGPL',
    keywords='',
    url='https://github.com/suminb/markdown',
    py_modules=['markdown'],
    long_description=open('README.md').read(),
    extras_require={'doc': ['Sphinx >=1.0']},
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
    cmdclass={'install_bin': install_bin},
)