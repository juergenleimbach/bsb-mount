from tkinter import *

def show_entry_fields():
   i=0
   for i in (0,1):
      print((e[i].get()))
      i=i+1


#def liesein():
master = Tk()
beschriftung = ['Vorname', 'Nachname']
e = []
i=0
for i in (0,1):
      Label(master, text=beschriftung[i]).grid(row=i)
      e.append(Entry(master))
      e[i].grid(row=i, column=1)

      Button(master, text='Quit',
             command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
      Button(master, text='Show',
             command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
#      master.bind('<Return>', (lambda event, e: fetch(e)))   

master.mainloop()

#liesein()
