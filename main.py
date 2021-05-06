from module_default_values import get_store, get_storeFR
from module_create_file import create_json
from module_read_config import print_data
from module_modify_config import modify
import json

data = get_store()
dataFR = get_storeFR()
filePathEN = "./en/translation.json"
filePathFR = "./fr/translation.json"

if __name__ == "__main__":
  create_json(filePathFR, dataFR, "FR")
  create_json(filePathEN, data, "EN")