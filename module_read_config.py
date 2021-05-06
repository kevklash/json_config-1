import json
from module_default_values import get_store, get_storeFR
from module_create_file import create_json


def print_data(file_path):
  data = get_store()
  dataFr = get_storeFR()
  try:
    with open(file_path, 'r') as config_file:
      data_file = json.load(config_file)
      for value in data_file:
        print(value + " : " + data_file[value])
  except FileNotFoundError:
    print("The file does not exist, generating a config file with default values...")
    create_json(data)
  except IOError:
    print("Temporary error reading the config file")