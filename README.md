
Introduction
-------------

`mendel` is a command line tool to convert a [Markdown](http://daringfireball.net/projects/markdown/) document into an HTML document.

Its name, `mendel`, was derived from the name of the 101st element in the periodic table of the elements: [Mendelevium](http://en.wikipedia.org/wiki/Mendelevium). The symbol of Mendelevium is Md, and `.md` is one of acceptable file extensions of Markdown. That is probably the only connection between Mendelevium and Markdown.


Requirements
-------------

* docopt - https://github.com/docopt/docopt
* markdown2 - https://github.com/trentm/python-markdown2

Usage
------

    mendel < README.md

    mendel < README.md > README.html
    
    mendel --css=style.css < README.md