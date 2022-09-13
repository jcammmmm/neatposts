import argparse

from .fontsmngr import copy_fonts_and_ignore
from .indexgen import generate_index
from .converter import to_html
from .filltempl import fill_content

def main():
  parser = argparse.ArgumentParser(
    description="""
      Generate a neat web document from a Markdown file. By that, you have
      both of the two worlds: a simple text file, and also a neat displayed html page
      without to get messed with tags.
    """)
  parser.add_argument('filename', help='markdown filename without extension')
  parser.add_argument('-i', action='store_true', 
    help="""
      flag that indicates that a toc-index web page will be generated provided
      the index.yaml post resources definition file. This package will look
      automatically for this file in the folder where the package was called.
    """)
  parser.add_argument('-p', action='store_true', 
    help="""
      flag that indicates that fonts location are in a remote server. If not HTTP
      remote location is defined with argument -l, this remote location defaults
      to: https://jcamilo.co/fonts/cmuserif/
    """)
  parser.add_argument('-l', metavar='fontloc',
    help="""
      an HTTP url that points to the computer modern fonts location.
    """)
  args = parser.parse_args()


  fonts_loc = 'fonts/cmuserif/'
  if (args.p):
    fonts_loc = 'https://jcamilo.co/fonts/cmuserif/'
  if (args.l):
    fonts_loc = args.l

  copy_fonts_and_ignore()
  if (args.i):
    html_content = generate_index()
  else:
    html_content = to_html(args.filename)

  print(html_content)
  fill_content(args.filename, fonts_loc, html_content)

if __name__ == '__main__':
  main()