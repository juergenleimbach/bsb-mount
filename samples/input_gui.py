from tkinter import *

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e[0].get(), e[1].get()))

master = Tk()
beschriftung = ['Vorname', 'Nachname']
e = []
i=0

for i in (0,1):
    Label(master, text=beschriftung[i]).grid(row=i)
    e.append(Entry(master))
    e[i].grid(row=i, column=1)
    print (e[i])

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
#Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
