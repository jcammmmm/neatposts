import os
from pathlib import Path
from importlib.resources import path
from os.path import join
from fnmatch import fnmatch

NODEJS_WORKING_DIR = str(join(path('neatposts', '').parent, 'text2chtml')) 

"""
Uses MathJax v3 to convert all TeX in an HTML document using JSDOM.

Parameters
----------
html_file_location : str
  An url pointing to an HTML document that was transformed from a MD document.

Returns
-------
str:
  String that contains an HTML document with all of its LaTeX contents
  converted ready to be displayed on the web browser.
"""
def render_mathematics(html_file_location):
    try:
      check_nodejs_reqs()
    except OSError as ose:
      raise Exception('Cannot generate file without NodeJS installed on this system. Try rendering LaTeX on the client device.', ose)
    
    os.chdir(NODEJS_WORKING_DIR)
    outpath = Path(html_file_location).parent.joinpath('out.html').__str__()
    return os.system('node -r esm tex2chtml-page ' + html_file_location + ' > ' + outpath)

"""
Check if the NodeJS script has installed on this package directory its node_module
dependencies. If not installed, runs npm install. If NodeJS is not installed on 
the system throws an exception.
"""
def check_nodejs_reqs():
# check for NodeJS dependencies and NodeJS itself
    js_deps = False
    for file in os.listdir(NODEJS_WORKING_DIR):
      if (fnmatch(file, 'node_modules')):
        js_deps = True
        break
    
    nodejs_install = True
    if not js_deps:
      try:
        os.system('node --version')
      except FileNotFoundError:
        nodejs_install = False
    
    if not js_deps:
      if not nodejs_install:
        raise ('NodeJS is not installed on this system, please install NodeJS v16.15.0')
      print('NodeJS script dependencies were not installed on this package folder.')
      print('Installing...')
      os.chdir(NODEJS_WORKING_DIR)
      os.system('npm install')

    