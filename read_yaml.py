import json
import yaml
import pprint

with open("my_test.yml") as f:
    new_list = yaml.load(f)
pprint.pprint(new_list)



with open("my_test.json") as f:
    new_list1 = json.load(f)
pprint.pprint(new_list1)

