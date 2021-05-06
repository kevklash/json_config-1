import json
from module_default_values import serveData
from module_create_file import create_json

def print_data():
  data = serveData()
  try:
    with open('config.json', 'r') as config_file:
      data_file = json.load(config_file)
      for value in data_file["Frontend"]:
        print(value['id'] + ' : ' + value['value'])
  except FileNotFoundError:
    print("The file does not exist, generating a config file with default values...")
    create_json(data)
  except IOError:
    print("Temporary error reading the config file")