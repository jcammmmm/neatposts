import os
import datetime as time
from jinja2 import Environment, PackageLoader

"""
Returns
-------
str
  HTML written document url location
"""
def fill_content(filename, fonts_loc, html_content):
  env = Environment(
    loader=PackageLoader('neatposts', package_path='.', encoding='UTF-8'),
    autoescape=False
  )

  # hardcode font urls in css file
  css = env.get_template('layout.css').render(urlprefix=fonts_loc)
  # put your post contents in template
  post = env.get_template('layout.html').render(content=html_content, styles=css)

  filename = filename + '.html'
  open(filename, 'w+', encoding='UTF-8').write(post)

  open(filename, 'a').write('Generated with NeatPosts by LogicFoundries </br>')
  open(filename, 'a').write('Last updated: ' + str(time.datetime.now()))
  print(filename + ' written.')
  return os.path.join(os.getcwd(), filename)