def usb_laufwerke():
    import psutil
    lw = []
    for var in psutil.disk_partitions():
        if var[3] == 'rw,removable':
            lw.append(var[1])
    usb_genutzt = [d[0] for d in lw]
    return usb_genutzt

benutzt = usb_laufwerke()
print (benutzt)
