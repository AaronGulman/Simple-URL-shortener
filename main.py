import tkinter

root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("600x300")

longUrl_label = tkinter.Label(root, text = "Enter your URL: ")
longUrl_entry = tkinter.Entry(root)
shortUrl_label = tkinter.Label(root, text ="Shortened URL: ")
shortUrl_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root,text = "Shortern URL")


longUrl_label.pack()
longUrl_entry.pack()
shortUrl_label.pack()
shortUrl_entry.pack()
shorten_button.pack()



root.mainloop()