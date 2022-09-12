import sys
import markdown as md
import datetime as time
import os
from jinja2 import Environment, PackageLoader
from fnmatch import fnmatch
from importlib.resources import path
from shutil import copytree
from re import search, escape

def main():
  copy_fonts_and_ignore()
  if len(sys.argv) < 2:
    raise Exception('Please provide the markdown file name.')

  FILENAME = sys.argv[1]
  FONTS_LOC = 'http://jcamilo.co/fonts/cmuserif/'
  FONTS_LOC = 'fonts/cmuserif/'

  env = Environment(
    loader=PackageLoader('neatdocs', package_path='.', encoding='UTF-8'),
    autoescape=False
  )

  with open(FILENAME + '.md', 'r', encoding='UTF-8') as input_file:
    text = input_file.read()

  '''
  attr_list: for inline attribute definitions
  toc      : table of contents
  tables   : generates html tables
  '''
  html = md.markdown(text, extensions=['attr_list', 'toc', 'tables'], output_format='html5', tab_length=2)
  print(html)

  css = env.get_template('layout.css').render(urlprefix=FONTS_LOC)
  post = env.get_template('layout.html').render(content=html, styles=css)
  open(FILENAME + '.html', 'w+', encoding='UTF-8').write(post)
  open(FILENAME + '.html', 'a').write('last updated: ' + str(time.datetime.now()))

def copy_fonts_and_ignore():
  # check if fonts folder exists
  copy = True
  for file in os.listdir(os.getcwd()):
    if fnmatch(file, 'fonts'):
      copy = False

  # copy fonts
  if copy:
    fonts_src_path = str(path('neatdocs.fonts.cmuserif', ''))
    fonts_des_path = os.path.join(os.getcwd(), 'fonts', 'cmuserif')
    copytree(fonts_src_path, fonts_des_path)

  # edit .gitignore
  append = True
  with open('.gitignore', 'r', encoding='UTF-8') as ignrfile:
    for line in ignrfile:
      if search(escape(line), 'fonts'):
        append = False
        break
  with open('.gitignore', 'a', encoding='UTF-8') as ignrfile:
    if append:
      ignrfile.write('\nfonts')
  
if __name__ == '__main__':
  main()