#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Frame1

modules ={'Frame1': [1, 'Main frame of Application', 'Frame1.py'],
 'module1': [0, '', 'module1.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
