from os import listdir
def apply_cogs(file: str, folder: str = None, *, logs: bool = False):
  if folder is None:
    x = __import__(file)
  else:
    x = __import__(f'{folder}.{file}')
  eval(f'x.{file}.cogs({bot})')
  del x
def process_folder(folder: str, *, logs: bool = False, excepte: list = None):
  x = __import__(folder)
  to_eval: str = f'.cogs({bot})'
  if excepte is None:
    if logs is True:
      for i in listdir('./' + folder):
        if i.endswith('.py'):
          i = i[: -3]
          eval(f'x.{i}{to_eval}')
          print(f'loaded cogs {i}')
    else:
      for i in listdir('./' + folder):
        if i.endswith('.py'):
          eval(f'x.{i[: -3]}{to_eval}')
  else:
    if logs is True:
      for i in listdir('./' + folder):
        if i.endswith('.py') and i[: -3] not in excepte:
          i = i[: -3]
          eval(f'x.{i}{to_eval}')
          print(f'loaded cogs {i}')
    else:
      for i in listdir('./' + folder):
        if i.endswith('.py') and i[: -3] not in excepte:
          eval(f'x.{i[: -3]}{to_eval}')
  del x, to_eval
