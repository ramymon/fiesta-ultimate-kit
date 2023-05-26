from dependencies import *


shell32 = ctypes.windll.shell32
params = None
directory = None
show_command = 1  # SW_SHOWNORMAL

mem = Pymem("Fiesta.bin")
module = module_from_name(mem.process_handle,"Fiesta.bin").lpBaseOfDll

offsets_yang = [0, 24, 12, 1436]
offsets_yin = [164, 24, 12, 1448]
offsets_test = [180, 0, 0, 0]

base_yang_rel = 6818008
base_yin_rel = 6673512
base_xCorr_rel = 7379772
base_yCorr_rel = 7379776
base_test_rel = 1204212

base_yang = module + base_yang_rel
base_yin = module + base_yin_rel
base_xCorr = module + base_xCorr_rel
base_yCorr = module + base_yCorr_rel
base_test = module + base_test_rel
# 

def press_button_via_ahk(x):
    executable = r"C:\Users\MONCEF\Desktop\fiesta-ultimate-kit\click-" + x
    result = shell32.ShellExecuteW(None, "runas", executable, params, directory, show_command)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def getPointerAdress(base,offsets):
    address = mem.read_int(base)
    for offset in offsets:
        if offset != offsets[-1]:
            address = mem.read_int(address + offset)
    address = address + offsets[-1]
    return address

while keyboard.is_pressed('f12')==False:
    adrr_yang = getPointerAdress(base_yang,offsets_yang)
    yang_value = mem.read_int(adrr_yang)
    adrr_yin = getPointerAdress(base_yin,offsets_yin)
    yin_value = mem.read_int(adrr_yin)
    xCorr_value = mem.read_int(base_xCorr)
    yCorr_value = mem.read_int(base_yCorr)


    adrr_test = mem.read_int(base_test)

    # print(decimal_to_binary(adrr_test))
    print(adrr_test)

    if yang_value < 400:
        press_button_via_ahk("q")
        time.sleep(0.5)

    if yin_value < 2300:
        press_button_via_ahk("e")
        time.sleep(0.5)
   
    time.sleep(0.6)
    

 
