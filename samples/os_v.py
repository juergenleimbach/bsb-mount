import platform
osstr = (platform.platform())
print (osstr)
if osstr[0] == 'W':
    print ('WIN')
if osstr [0] == 'D':
    print ('OSX')
