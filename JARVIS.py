import wx
import wikipedia
import wolframalpha
from gtts import gTTS
import os
from bs4 import BeautifulSoup
import urllib.request


myobj = gTTS(text="Welcome user, I'm Jarvis", lang='en', slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,
                          pos=wx.DefaultPosition, size=wx.Size(450,450),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="JARVIS")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label = "Search")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input1 = self.txt.GetValue()
        input1 = input1.lower()
        speak_ans = gTTS(text='The result for your search will be popped up into another window', lang='en', slow=False)
        speak_ans.save("speak.mp3")
        os.system("speak.mp3")
        if 'movies' in input1:
            year =[int(x) for x in input1.split() if x.isdigit()]
            #print(year[0])
            opener = urllib.request.build_opener()
            url = "http://www.imdb.com/search/title?release_date=" + str(year[0]) + "," + str(year[0]) + "&title_type=feature"
            ourUrl = opener.open(url).read()
            soup = BeautifulSoup(ourUrl, "lxml")
            article = soup.find('div', attrs={'class': 'article'}).find('h1')
            print(article.contents[0] + ":")
            lister_list_contents = soup.find('div', attrs={'class': 'lister-list'})
            i = 1
            movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
            for div in movieList:
                header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
                for item in header:
                    title = header[0].findChildren('a')
                    print(str(i) + '. Movie: ' + str(title[0].contents[0]))
                i += 1
        else:
            try:
                # wolframalpha
                app_id = #your wolfram app_id
                client = wolframalpha.Client(app_id)
                res = client.query(input1)
                ans = next(res.results).text
                speak_ans = gTTS(text='The result for your search is '+ ans, lang='en', slow=False)
                speak_ans.save("speak.mp3")
                os.system("speak.mp3")
                print(ans)
            except:
                # wikipedia
                input1 = input1.split(' ')
                input1 = " ".join(input1[2:])
                speak_ans = gTTS(text='Searched for '+ input1, lang='en', slow=False)
                speak_ans.save("speak1.mp3")
                os.system("speak1.mp3")
                print(wikipedia.summary(input1))


if __name__== "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()

