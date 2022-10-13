import markdown as md

def to_html(filename):
  try:
    with open(filename + '.md', 'r', encoding='UTF-8') as input_file:
      text = input_file.read()
  except FileNotFoundError:
    print('The file ' + filename + '.md does not exist.')
    return

  '''
  attr_list: for inline attribute definitions
  toc      : table of contents
  tables   : generates html tables
  '''
  html = md.markdown(
    text, 
    extensions=['attr_list', 'toc', 'tables'], 
    output_format='html5', 
    tab_length=2)
  return html
  