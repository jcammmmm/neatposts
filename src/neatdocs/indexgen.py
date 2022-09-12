from yaml import load
from jinja2 import Environment, PackageLoader

def generate_index(yml_idx_filepath):
  posts_idx = open(yml_idx_filepath, 'r').read()
  try:
      from yaml import CLoader as Loader
  except ImportError:
      from yaml import Loader

  posts_idx = load(posts_idx, Loader=Loader)

def generator(posts_idx):
    env = Environment(
        loader=PackageLoader('html'),
        autoescape=False,
        trim_blocks=True,
    )
    env.filters['to_valid_id'] = to_valid_id
    env.filters['format_date_period'] = format_date_period
    env.filters['decorate_task_descr'] = decorate_task_descr

    template = env.get_template(template_name)
    return template.render(cv=cv_data)




