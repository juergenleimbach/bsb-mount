import os
import subprocess

pingchar = '-n'
with open(os.devnull, 'w') as DEVNULL:
    try:
        subprocess.check_call(
            ['ping', ,'10.22.10.8'],
            stdout=DEVNULL,  # suppress output
            stderr=DEVNULL
        )
        is_up = True
    except subprocess.CalledProcessError:
        is_up = False
print (is_up)
