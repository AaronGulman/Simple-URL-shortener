import tkinter
import pyshorteners

def shorten():
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(longUrl_entry.get())
        shortUrl_entry.insert(0, short_url)

root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("300x150")
background_color = "#000000"
text_color = "#FFFFFF"
button_color = "#FF0000"

root.config(bg=background_color)
custom_font = ("Arial", 14)




longUrl_label = tkinter.Label(root, text = "Enter your URL: ", bg=background_color, fg=text_color, font=custom_font)
longUrl_entry = tkinter.Entry(root, font=custom_font)
shortUrl_label = tkinter.Label(root, text ="Shortened URL: ", bg=background_color, fg=text_color, font=custom_font)
shortUrl_entry = tkinter.Entry(root , font=custom_font)
shorten_button = tkinter.Button(root,text = "Shortern URL" , command = shorten, bg=text_color, fg=background_color, font=custom_font)


longUrl_label.pack()
longUrl_entry.pack()
shortUrl_label.pack()
shortUrl_entry.pack()
shorten_button.pack(pady=(5, 10))



root.mainloop()