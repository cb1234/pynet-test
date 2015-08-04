from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco.txt")
pfs_maps = cisco_cfg.find_objects_w_child(r'crypto map CRYPTO', r'set pfs group2')
for map in pfs_maps:
    print map.text
    for child in map.children:
        print child.text


