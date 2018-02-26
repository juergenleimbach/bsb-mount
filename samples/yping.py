import os
import subprocess

with open(os.devnull, 'w') as DEVNULL:
    try:
        subprocess.check_call(
            ['ping', '-n', '3', '10.22.10.1'],
            stdout=DEVNULL,  # suppress output
            stderr=DEVNULL
        )
        is_up = True
    except subprocess.CalledProcessError:
        is_up = False
print (is_up)
