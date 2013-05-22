"""Usage: mendel [-h] [--css=CSS] [--embed=CSS]

Converts

Options:
  -h --help
  --css=CSS   path of a stylesheet file
  --embed=CSS path of a stylesheet file to be embeded
"""

from docopt import docopt
from markdown2 import markdown

import sys

def main():
    args = docopt(__doc__)

    # TODO: Make this prettier!
    if args['--css'] != None:
        print '<!DOCTYPE html>'
        print '<html>'
        print '<head>'
        print '  <link rel="stylesheet" type="text/css" href="%s"/>' % args['--css']
        print '</head>'
        print '<body>'

    # TODO: Revise this
    if args['--embed'] != None:
        print '<style type="text/css">'
        print open(args['--embed'], 'r').read()
        print '</style>'
    
    print markdown(sys.stdin.read(), extras=['wiki-tables'])

    if args['--css'] != None:
        print '</body>'
        print '</html>'

if __name__ == '__main__':
    main()

