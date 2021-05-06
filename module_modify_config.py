import json


def modify(file_path):
  """ Read the file """
  try:
    with open(file_path, 'r') as config_file:
      json_object = json.load(config_file)
  except IOError:
    print("Temporary error reading the language file")

  json_object['title'] = 'This is USLT2'
  json_object['description'] = 'We are completely replacing that old USLT v1 dude'

  """ Writing in the file """
  try:
    with open(file_path, 'w') as file:
      json.dump(json_object, file, indent=4)
  except IOError:
    print('Temporary error while writing to the language file')