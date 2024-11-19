import uuid
import winreg
import sys

def randomhwid():
    new_hwid = str(uuid.uuid4())
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001",
                                 0, winreg.KEY_WRITE)
        winreg.SetValueEx(reg_key, "HwProfileGuid", 0, winreg.REG_SZ, new_hwid)
        winreg.CloseKey(reg_key)
        print(f"New HWID successfully set:\n{new_hwid}")
    except PermissionError:
        print("This module requires elevated permissions.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")

def sethwid(new_hwid):
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001",
                                 0, winreg.KEY_WRITE)
        winreg.SetValueEx(reg_key, "HwProfileGuid", 0, winreg.REG_SZ, new_hwid)
        winreg.CloseKey(reg_key)
        print(f"New HWID successfully set:\n{new_hwid}")
    except PermissionError:
        print("This module requires elevated permissions.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")

def get_current_hwid():
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001",
                                 0, winreg.KEY_READ)
        current_hwid, _ = winreg.QueryValueEx(reg_key, "HwProfileGuid")
        winreg.CloseKey(reg_key)
        return current_hwid
    except PermissionError: # Wont get run by default because it doesnt require admin to read
        print("This module requires elevated permissions.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()

while True:
    print("\n\nRemember this will permanently remove your old HWID! Be sure to save it.\n")
    print("1 - Sets your HWID to something random")
    print("2 - Set your HWID to a specified value")
    print("3 - Reads your current HWID")
    print("4 - Exit")
    userinput = input("\n> ")
    if userinput == "1":
        randomhwid()
    elif userinput == "2":
        sethwid(input("New HWID > "))
    elif userinput == "3":
        print(get_current_hwid())
    elif userinput == "4":
        sys.exit()
    else:
        print("Unvalid choice.\n\n\n\n")