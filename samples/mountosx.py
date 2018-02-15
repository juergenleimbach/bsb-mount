import os
directory = "/Users/user.name/foldername"
if not os.path.exists(directory): os.makedirs(directory)
os.system("mount_smbfs //user.name:password@server/servershare ~/foldername")
