# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0b3 on Mon Feb 12 14:12:05 2018
#

import wx
from pathlib import Path
import base64
import platform
import getpass
import os

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((250, 411))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, vorgabe[0])
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, vorgabe[1])
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, vorgabe[2], style=wx.TE_PASSWORD)
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, vorgabe[3])
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_0 = wx.Button(self, wx.ID_ANY, "Weiter")
#Mit folgender Zeile wird der weiter-buton an die Funktion weiterEvent() gekoppelt
        self.button_0.Bind(wx.EVT_BUTTON, self.weiterEvent)
        self.button_1 = wx.Button(self, wx.ID_ANY, "Speichern")
        self.button_1.Bind(wx.EVT_BUTTON, self.saveEvent)
        self.__set_properties()
        self.button_2 = wx.Button(self, wx.ID_ANY, "Laden")
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        grid_sizer_1 = wx.GridSizer(7, 2, 0, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Konfiguration", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Anmeldename", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(label_2, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Passwort", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_3, 0, wx.ALIGN_CENTER, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Freigabe", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(label_4, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_4, 0, wx.ALIGN_CENTER, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Rolle", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(label_5, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_5, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.button_0, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_CENTER, 0)
        self.SetSizer(grid_sizer_1)
        self.Layout()

#simple Funktion für weiter Button
# hier gehört zum großen Teil das Programm hin        
    def weiterEvent(self, event):
#        vorgabe = config_lesen()
        print (vorgabe)
        #self.Destroy()

    def saveEvent(self,event):
        vorgabe[0] = self.text_ctrl_1.GetValue()
        vorgabe[1] = self.text_ctrl_2.GetValue()
        vorgabe[2] = self.text_ctrl_3.GetValue()
        vorgabe[3] = self.text_ctrl_4.GetValue()
        config_speichern(vorgabe)
        # end wxGlade

# end of class MyFrame
def config_windows():
   import win32wnet
   import win32netcon
   directory = "c:/Users/"+aktualuser+"/Documents/bsbebra-mounts"
   if not os.path.exists(directory):
      os.makedirs(directory)
   return directory

def config_osx():
   directory = "/Users/"+aktualuser+"/Documents/bsbebra-mounts"
   if not os.path.exists(directory):
      os.makedirs(directory)
   return directory

def config_lesen():
    oeffne = open(file,"r")
    werte = []
    zeilenzaehler = 0
    hilfsspeicher = ''
    for zeile in oeffne:
      werte.append(zeile.strip())
      if zeilenzaehler == 0:
         for zeichen in range(1, len(werte[zeilenzaehler])-1):
            hilfsspeicher = hilfsspeicher + werte[zeilenzaehler][zeichen]
         werte[0] = hilfsspeicher
      if zeilenzaehler == 2:
         werte[zeilenzaehler] = werte[zeilenzaehler].encode('utf-8')
         werte[zeilenzaehler] = base64.b64decode(werte[zeilenzaehler])
         werte[zeilenzaehler] = werte[zeilenzaehler].decode('utf-8')
      zeilenzaehler = zeilenzaehler + 1
    oeffne.close()
    return (werte)

def config_speichern(sichern):
   oeffne = open(file,"w")
   werte = []
   for zeile in range(len(sichern)):
      werte.append(sichern[zeile])
      if zeile == 0:
         werte[zeile] = ("["+werte[zeile]+"]")
      elif zeile == 2:
         werte[zeile] = werte[zeile].encode('utf-8')
         werte[zeile] = base64.b64encode(werte[zeile])
         werte[zeile] = werte[zeile].decode('utf-8')
      oeffne.write(werte[zeile]+"\n")
   oeffne.close()
   
# Globale Konstanten und Variablen
# Unterscheiden nach OSX und Windows
beschriftung = ['Konfiguration', 'Anmeldename', 'Passwort', 'Server/Freigabe']
vorgabe = ['config', 'Anmeldename', 'GEHEIM', '10.22.10.1']
osstring = platform.platform()
aktualuser = getpass.getuser()
if osstring[0] == "W":
   file = config_windows()
else:
   file = config_osx()

file = file+'/config.dat'
print (file)
vorgabe = config_lesen()
# Minimum um ein Fenster darzustellen
app = wx.App(vorgabe)
vorgabe = config_lesen()
frame = MyFrame(None)
frame.Show()
app.MainLoop()