# HWIDSpoofer
Very simple open-source HWID Spoofer coded in Python

# HWIDLib Docs

current_hwid() - Returns the current HWID

- Requires elevated privileges
random_hwid() - Sets to a random HWID
set_hwid(new_hwid) - Sets to a specified HWID

# HWIDLib example

```python

from HWIDLib import *

set_hwid("7af25993-acaa-45c7-abb4-708bcb4394e9") # Example HWID
print(current_hwid())
random_hwid()
print(current_hwid())

```
