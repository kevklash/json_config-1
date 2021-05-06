import json


dataEn = {}
dataFr = {}


def get_store():
  try:
    with open('lang_defaults/en.json', 'r') as store:
      data_file = json.load(store)
      for item in range(len(data_file)):
        dataEn[data_file[item]["id"]] = data_file[item]["value"]
  except IOError:
    print("Temporary error reading the default language EN store")
  return dataEn


def get_storeFR():
  try:
    with open('lang_defaults/fr.json', 'r') as store:
      data_file = json.load(store)
      for item in range(len(data_file)):
        dataFr[data_file[item]["id"]] = data_file[item]["value"]
  except IOError:
    print("Temporary error reading the default language FR store")
  return dataFr