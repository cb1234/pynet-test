from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco.txt")
crypto_map = cisco_cfg.find_objects(r'crypto map CRYPTO')

for map in crypto_map:
    print map.text
    for child in map.children:
        print child.text

