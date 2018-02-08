import platform
import getpass
osstr = (platform.platform())
print (osstr)
if osstr[0] == 'W':
    print ('WIN')
if osstr [0] == 'D':
    print ('OSX')
#import getpass
print(getpass.getuser())
