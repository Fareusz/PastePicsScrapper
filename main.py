import _tkinter
import random, string, webbrowser, cloudscraper, requests, urllib.request, os, configparser
import time
from bs4 import BeautifulSoup
from tkinter import messagebox
import tkinter as tk
from datetime import datetime

#https://paste.pics/FHX7O

fontcs=('Comic Sans MS', 10, 'bold italic')

config = configparser.ConfigParser()
config.read('config.ini')
cmain = config["main"]

domain = cmain["domain"]
ilznakow = int(cmain["length"])

new = 1
root = tk.Tk()
root.title("PastePicsScrapper by Fareusz")
root.geometry("500x250")

def openweb(link):
    webbrowser.open(link, new=new)

def rename():
    now = str(datetime.now())
    now = now.replace(":", "-")
    os.rename('image.jpg', f"{now}.jpg")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        try:
            os.remove("image.jpg")
            root.destroy()
            exit()
        except:
            root.destroy()
            exit()

def FindLinkPastePics():
    tic = time.perf_counter()
    found = 0
    while found == 0:
        id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=ilznakow))
        URL = f"https://{domain}/" + str(id)
        page = scraper.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        print(soup.title)
        stitle = str(soup.title)
        if 'Error 404. Page not found - Paste.Pics' in stitle:
            print(
                '404'
            )
            continue
        resultss = soup.findAll('img')
        results = resultss[2]
        source = results['src']
        b = brwser.get()
        if b == 1:
            openweb(source)

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        filename = 'image.jpg'
        image_url = source
        try:
            urllib.request.urlretrieve(image_url, filename)
        except urllib.error.HTTPError:
            print('Your request got blocked :( Try Again!')
        except _tkinter.TclError:
            print('There was an error. Try again.')
        root2 = tk.Tk()
        root2.title(str(URL))
        def next():
            root2.destroy()
            FindLinkPastePics()

        img = tk.PhotoImage(master=root2, file="image.jpg")
        button3 = tk.Button(root2, width=2, height=2, text='Next!', font=fontcs, bg='black', fg='green', padx=10,
                            command=next)
        button2 = tk.Button(root2, width=2, height=2, text='Save!', font=fontcs, bg='black', fg='green', padx=10,
                            command=rename)
        button2.pack()
        button3.pack()
        Aimage = tk.Label(root2, image=img)
        Aimage.pack()
        tac = time.perf_counter()
        BLabel = tk.Label(root2, text=f"Found and downloaded image in {tac - tic:0.4f} seconds")
        BLabel.pack()
        root2.mainloop()

scraper = cloudscraper.create_scraper()
resultList = list()

tk.Button(root, width=50, height=10, text='Get Link', font=fontcs, bg='black', fg='green', padx=10,
          command=FindLinkPastePics).place(x=10, y=10)


brwser = tk.IntVar()
c = tk.Checkbutton(root, text="Open in Browser at hit", variable=brwser, onvalue=1, offvalue=0)
c.place(x=200, y=205)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()