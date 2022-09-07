import sys
import markdown as md
import datetime as time
from jinja2 import Environment, FileSystemLoader

if len(sys.argv) < 2:
  raise Exception('Please provide the markdown file name.')

FILENAME = sys.argv[1]
FONTS_LOC = 'http://jcamilo.co/fonts/cmuserif/'
FONTS_LOC = 'fonts/cmuserif/'

env = Environment(
  loader=FileSystemLoader('.'),
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