import datetime as time
from jinja2 import Environment, PackageLoader

def fill_content(filename, fonts_loc, html_content):
  env = Environment(
    loader=PackageLoader('neatdocs', package_path='.', encoding='UTF-8'),
    autoescape=False
  )

  css = env.get_template('layout.css').render(urlprefix=fonts_loc)
  post = env.get_template('layout.html').render(content=html_content, styles=css)

  filename = filename + '.html'
  open(filename, 'w+', encoding='UTF-8').write(post)

  open(filename, 'a').write('Generated with NeatPosts by LogicFoundries </br>')
  open(filename, 'a').write('Last updated: ' + str(time.datetime.now()))
  print(filename + ' written.')