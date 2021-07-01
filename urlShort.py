from tkinter import *
import pyshorteners as ps # pip install pyshorteners
import pyperclip
from PIL import ImageTk, Image

root=Tk()
root.title("URL Shortener")
root.geometry("600x500")
root.configure(background='black')
root.resizable(False,False)

originalURL=StringVar(root)
shortenedURL=StringVar(root)

def shorten():
	originalString=str(originalURL.get())
	shortM=ps.Shortener()
	result=shortM.tinyurl.short(originalString)
	global shortenedURL
	shortenedURL.set(str(result))
	
def copy_to_clipboard():
	pyperclip.copy(shortenedURL.get())

logo = Image.open("logo.png")
logo = logo.resize((150, 150), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
image=Label(root,image=logo,bg='black')
labelIntro = Label(root,text='Instagram : @expert.py',bg='black',fg='#01FEC2')
label1=Label(root,text="Enter the URL: ",bg='black',fg='white')
text1=Entry(root,textvariable=originalURL,width=50,bg='black',fg='white')
button1=Button(root,text="Shorten",command=shorten,width=20,bg='brown',fg='white')
label2=Label(root,text="Shortened URL: ",bg='black',fg='white')
text2=Entry(root,textvariable=shortenedURL,width=50,bg='black',fg='white')
button2=Button(root,text="Copy",command=copy_to_clipboard,width=20,bg='brown',fg='white')
button3=Button(root,text="Quit",command=root.destroy,width=20,bg='brown',fg='white')

image.pack()
labelIntro.pack()
label1.pack(pady=10)
text1.pack(pady=10)
button1.pack(pady=10)
label2.pack(pady=10)
text2.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=5)

root.mainloop()