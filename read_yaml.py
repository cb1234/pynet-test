import json
import yaml
import pprint

with open("some_file.yml") as f:
    new_list = yaml.load(f)
pprint.pprint(new_list)



with open("my_file.json") as f:
    new_list1 = json.load(f)
pprint.pprint(new_list1)

