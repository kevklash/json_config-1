import json

def modify():
  """ Read the file """
  try:
    with open('config.json', 'r') as config_file:
      json_object = json.load(config_file)
  except IOError:
    print("Temporary error reading the config file")

  json_object["Frontend"][1]['value'] = 'This is USLT2'

  """ Writing in the file """
  try:
    with open('config.json', 'w') as file:
      json.dump(json_object, file, indent=4)
  except IOError:
    print('Temporary error while writing to the file')