from tkinter import *
from pytube import YouTube
main = Tk()
main.geometry('300x250')
main.resizable(False,False)
main.title('YOUTUBE DOWNLOADER')

lb1 = Label(main,text='Youtube videos download', fg='red' )
lb1.pack()
lb2 = Label(main, text='enter video URL' ,fg='green')
lb2.pack()
en1 = Entry(main,width=50)
en1.pack()
def click():
    url = YouTube(en1.get())
    url.streams.get_highest_resolution().download(output_path='videos')
btn = Button(main , command=click, text="DOWNLOAD", fg='white', bg='red')
btn.config(width=10)    
btn.place(x= 110 , y=70)


main.mainloop()
