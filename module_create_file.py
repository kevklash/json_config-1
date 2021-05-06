import json


def create_json(file_path, values, lang):
  try:
    with open(file_path, 'r'):
      if lang == "EN":
        print("English language file was found")
      elif lang == "FR":
        print("French language file was found")
  except FileNotFoundError:
    if lang == "EN":
      print("The English language file does not exist, generating a config file with default values...")
    elif lang == "FR":
      print("The French language file does not exist, generating a config file with default values...")
    with open(file_path, 'w') as outfile:
      json.dump(values, outfile, indent=4)
      if lang == "EN":
        print("English language file was created successfully")
      elif lang == "FR":
        print("French language file was created successfully")
  except IOError:
    print("Temporary error reading the config file")