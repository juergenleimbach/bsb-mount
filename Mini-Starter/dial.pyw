import wx 
import os 

class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title, size = (250,200))  
         
      self.InitUI() 
         
   def InitUI(self):    
      self.count = 0 
      pnl = wx.Panel(self) 
		
      vbox = wx.BoxSizer(wx.VERTICAL) 
      hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
      hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		
      self.text = wx.StaticText(pnl, label = "hello") 
      self.btn1 = wx.Button(pnl, label = "Choose Font")
      self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn1) 
		
      hbox1.Add(self.text, proportion = 1, flag = wx.ALIGN_CENTRE) 
      hbox2.Add(self.btn1, proportion = 1, flag = wx.ALIGN_CENTRE, border = 10) 
		
      vbox.Add(hbox2, flag = wx.ALIGN_CENTRE) 
         
      vbox.Add(hbox1, proportion = 1, flag = wx.ALIGN_CENTRE) 
         
      pnl.SetSizer(vbox) 
      self.Centre() 
      self.Show(True) 
      
   def OnClick(self, e): 
      dlg = wx.FontDialog(self,wx.FontData()) 
		
      if dlg.ShowModal() == wx.ID_OK: 
         data = dlg.GetFontData() 
         font = data.GetChosenFont() 
         self.text.SetFont(font)
			
      dlg.Destroy() 
		
ex = wx.App() 
Mywin(None,'FileDialog Demo') 
ex.MainLoop()
