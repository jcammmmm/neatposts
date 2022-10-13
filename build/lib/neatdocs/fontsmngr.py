import os
from fnmatch import fnmatch
from importlib.resources import path
from shutil import copytree
from re import search, escape

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
  try:
    with open('.gitignore', 'r', encoding='UTF-8') as ignrfile:
      for line in ignrfile:
        if search(escape(line), 'fonts'):
          append = False
          break
    with open('.gitignore', 'a', encoding='UTF-8') as ignrfile:
      if append:
        ignrfile.write('\nfonts')
  except FileNotFoundError:
    # ignore error and proceed
    print('It seems that this project does not have a .gitignore file.')
  