from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco.txt")
crypto_map = cisco_cfg.find_objects_wo_child(r'crypto map CRYPTO', r'set transform-set AES')

for map in crypto_map:
    print map.text
    for child in map.children:
        print child.text

