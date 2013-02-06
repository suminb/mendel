
Introduction
-------------

`markdown` is a command line tool to convert a [Markdown](http://daringfireball.net/projects/markdown/) document into an HTML document.


Requirements
-------------

* docopt - https://github.com/docopt/docopt
* markdown2 - https://github.com/trentm/python-markdown2

Usage
------

    markdown < README.md

    markdown < README.md > README.html
    
    markdown --css=style.css < README.md