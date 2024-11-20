import uuid
import winreg

def random_hwid():
    new_hwid = str(uuid.uuid4())
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001",
                                 0, winreg.KEY_WRITE)
        winreg.SetValueEx(reg_key, "HwProfileGuid", 0, winreg.REG_SZ, new_hwid)
        winreg.CloseKey(reg_key)
        return new_hwid
    except PermissionError:
        return PermissionError
    except Exception as e:
        return e

def set_hwid(new_hwid):
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001",
                                 0, winreg.KEY_WRITE)
        winreg.SetValueEx(reg_key, "HwProfileGuid", 0, winreg.REG_SZ, new_hwid)
        winreg.CloseKey(reg_key)
        return new_hwid
    except PermissionError:
        return PermissionError
    except Exception as e:
        return e

def current_hwid():
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                 r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001",
                                 0, winreg.KEY_READ)
        current_hwid, _ = winreg.QueryValueEx(reg_key, "HwProfileGuid")
        winreg.CloseKey(reg_key)
        return current_hwid
    except PermissionError: # Wont get run by default because it doesnt require admin to read
        return PermissionError
    except Exception as e:
        return e
