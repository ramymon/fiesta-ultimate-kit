from pymem import *
from pymem.process import *
import keyboard 



mem = Pymem("Fiesta.bin")
module = module_from_name(mem.process_handle,"Fiesta.bin").lpBaseOfDll

offsets_yang = [0x0, 0x18, 0xC, 0x59C]

def getPointerAdress(base,offsets):
    address = mem.read_int(base)
    for offset in offsets:
        if offset != offsets[-1]:
            address = mem.read_int(address + offset)
    address = address + offsets[-1]
    return address

adrr_yang = getPointerAdress(module+0x006808D8,offsets_yang)


yang_value = mem.read_int(adrr_yang)

print(yang_value)

#while keyboard.is_pressed('f12')==False:
   # value = 