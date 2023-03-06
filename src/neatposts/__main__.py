import argparse

from .fontsmngr import copy_fonts_and_ignore
from .indexgen import generate_index
from .converter import to_html
from .filltempl import fill_content
from .rendermath import render_mathematics

def main():
  parser = argparse.ArgumentParser(
    description="""
      Generate a neat web document from a Markdown file. By that, you have
      both of the two worlds: a simple text file, and also a neat displayed html page
      without to get messed with tags.
    """)
  parser.add_argument('filename', help='markdown filename without extension')
  parser.add_argument('-r', '--client-rendering', action='store_true', 
    help="""
      Indicates if neatpost LaTeX mathematics shall be renderend on the web browser.
      If not provided as argument, the neatposts mathematics in LaTeX are converted
      to CHTML on the server, speeding up the page loading for the final user.
    """)
  parser.add_argument('-i', action='store_true', 
    help="""
      Flag that indicates that a toc-index web page will be generated provided
      the index.yaml post resources definition file. This package will look
      automatically for this file in the folder where the package was called.
    """)
  parser.add_argument('-p', action='store_true', 
    help="""
      Flag that indicates that fonts location are in a remote server. If not HTTP
      remote location is defined with argument -l, this remote location defaults
      to: https://jcamilo.co/fonts/cmuserif/
    """)
  parser.add_argument('-l', metavar='fontloc',
    help="""
      an HTTP url that points to the computer modern fonts location.
    """)
  args = parser.parse_args()
  
  # Font location: development or production location
  fonts_loc = 'fonts/cmuserif/'
  if (args.p):
    fonts_loc = 'https://jcamilo.co/fonts/cmuserif/'
  if (args.l):
    fonts_loc = args.l
    copy_fonts_and_ignore()

  # Convert Markdown with LaTex typesets to HTML with LaTex typesets
  if (args.i):
    html_content = generate_index()
  else:
    html_content = to_html(args.filename)
  
  # Produce final file
  html_file_loc = fill_content(args.filename, fonts_loc, html_content)

  # Convert HTML with LaTex typesets to pure HTML document with mathematics
  if (not args.client_rendering):
    render_mathematics(html_file_loc);
  
if __name__ == '__main__':
  main()