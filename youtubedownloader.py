#downloading YouTube video

#import modules
import tkinter as tk
from pytube import YouTube
from tkinter import *
from tkinter import messagebox, filedialog

#Create tkinter object
root = tk.Tk()

#creating tkinter vairables
video_link = StringVar()
save_path = StringVar()

# Defining Browse() to select a destination folder to save the video
def Browse():
	download_Directory = filedialog.askdirectory(initialdir="/Users/vasiki/Desktop/YT Vids")
	save_path.set(download_Directory)

def Download():
	#getting user-input link
	link = video_link.get()

	#optimal location for video
	save_path_str = save_path.get()

	#creating YT object
	yt = YouTube(link)

	#get all streams of video and selecting the first
	videoStream = yt.streams.first()

	#download to location
	videoStream.download(save_path_str)

	#display message
	messagebox.showinfo("Successfully","downloaded and saved in \n" + save_path_str)

#Creating Widget
def Widget():
	head_label = Label(root, text="YouTube Video Downloader Using Tkinter",
		padx=15,
		pady=15,
		font="SegoeUI 15",
		bg="black",
		fg="red"
		)
	head_label.grid(
		row=1,
		column=1,
		pady=10,
		padx=5,
		columnspan=3)
	link_label = Label(root,
                       text="YouTube link :",
                       bg="salmon",
                       pady=5,
                       padx=5)
	link_label.grid(row=2,
    	column=0,
    	pady=5,
    	padx=5)

root.linkText = Entry(root,
                          width=35,
                          textvariable=video_link,
                          font="Arial 14")
root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)
 
 
destination_label = Label(root,
                              text="Destination :",
                              bg="salmon",
                              pady=5,
                              padx=9)
destination_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)
 
 
root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=save_path,
                                 font="Arial 14")
root.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)
 
 
browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)
 
Download_B = Button(root,
                        text="Download Video",
                        command=Download,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)

#setting title, bg color + size of window
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="Black")

#Calling widgets function
Widget()

#defining infinite loop to run app
root.mainloop()

