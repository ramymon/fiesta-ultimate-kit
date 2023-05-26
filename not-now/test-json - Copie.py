offsets_yang = ["0x0", "0x18", "0xC", "0x59C"]
offsets_yin = ["0xA4", "0x18", "0xC", "0x5A8"]
base_yang_rel = "0x006808D8"
base_yin_rel = 0x0065D468
base_xCorr_rel = '0x00709B3C'
base_yCorr_rel = '0x00709B40'

print(type(int(base_xCorr_rel,16)))
print(hex(int(base_xCorr_rel,16)))

print(type([int(i,16) for i in offsets_yang]))
print([hex(int(i,16)) for i in offsets_yang])
#test_list = [int(i) for i in base_xCorr_rel]
a = [hex(int(i,16)) for i in offsets_yang]
b = a*2
print(b)
print(type(a[1]))

offsets_yang = ["0x0", "0x18", "0xC", "0x59C"]
a = [int(hex(int(i, 16)),16) for i in offsets_yang]

print(a)
print(type(a[1]))

