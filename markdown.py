"""Usage: markdown [-h] [--css=CSS]

Converts

Options:
  -h --help
  --css=CSS   path of a stylesheet file

"""

from docopt import docopt
from markdown2 import markdown

import sys

if __name__ == '__main__':
    args = docopt(__doc__)

    # TODO: Make this prettier!
    if args['--css'] != None:
        print '<!DOCTYPE html>'
        print '<html>'
        print '<head>'
        print '  <link rel="stylesheet" type="text/css" href="%s"/>' % args['--css']
        print '</head>'
        print '<body>'
    
    print markdown(sys.stdin.read())

    if args['--css'] != None:
        print '</body>'
        print '</html>'