import wx
import wikipedia
import wolframalpha
from gtts import gTTS
import os

myobj = gTTS(text="Welcome user, I'm Jarvis, How can I help you?", lang='en', slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,
                          pos=wx.DefaultPosition, size=wx.Size(450,100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="JARVIS")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
                            label = "Search")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            # wolframalpha
            app_id = "W4QQ6P-7UTV2E4TX8"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            ans = next(res.results).text
            speak_ans = gTTS(text='The result for your search is '+ ans, lang='en', slow=False)
            speak_ans.save("speak.mp3")
            os.system("speak.mp3")
            print(ans)
        except:
            # wikipedia
            input = input.split(' ')
            input = " ".join(input[2:])
            speak_ans1 = gTTS(text='Searched for '+ input, lang='en', slow=False)
            speak_ans1.save("speak1.mp3")
            os.system("speak1.mp3")
            print(wikipedia.summary(input))


if __name__== "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()

