import _tkinter # with underscore, and lowercase 't'
import tkinter # no underscore, lowercase 't' for V3.0 and later.
import os
import tkinter.messagebox
import urllib.request
from tkinter import *
from tkinter import filedialog


import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root = tkinter.Tk()
root.geometry("190x160")
root.title("Download")
root.resizable(0,0) # No Resize the Window
root.wm_iconbitmap("Icon.ico")
root.configure(background="#242424")

ButtonColorText =  "white"
ButtonColorBG = "black"
global DirChoose 
PadByY = 3.5
print ("Log\n<------------------------------------------------------------------------------>")


#Tab Nome
Nome_Label = Label(root,text="Inserire Nome :",command= None , fg = ButtonColorText  , bg = ButtonColorBG  , bd = 0 )
Nome_Label.pack(pady=PadByY ,fill =  'x')
varNome = tkinter.StringVar()
entry = tkinter.Entry(root, textvariable=varNome , bd = 0 )
entry.focus_set()
entry.pack(pady=PadByY ,fill =  'x')

#Tab url
TxtUrl=Label(root,text="Inserire Url :",command= None , fg = ButtonColorText  , bg = ButtonColorBG  , bd = 0)
TxtUrl.pack(pady=PadByY ,fill =  'x')
varUrl = tkinter.StringVar()
entry = tkinter.Entry(root, textvariable=varUrl)
entry.pack(pady=PadByY ,fill =  'x')

def Alert(Messaggio):
	Attention = messagebox.showerror("Errore", Messaggio)

def Download(url , name ):
	
	urllib.request.urlretrieve(url, name)	
	# http://animewheyhd.it/Anime/file/Naruto/422HD.mp4

def SaveData(directory , Data):
	text_file = open( directory , "w")
	text_file.write(Data)
	text_file.close()

def Save():
	try:
		Url = varUrl.get()
		NomeFile = varNome.get()

		text_file = open("Dir.txt", "r")
		DirRead=text_file.read()
		text_file.close()
		
		#threading.run( Download(Url, DirRead+"\\"+NomeFile) )
		Download(Url, DirRead+"\\"+NomeFile)

	except ValueError:
		#print(ValueError)
		if (varNome.get() == "" or varUrl.get() == ""):
			Alert("Manca un parametro")


			

def Setting():
	SettingFrame = Tk()
	SettingFrame.configure(background="#242424")
	SettingFrame.geometry("190x160")

	Dir_Label = Label(SettingFrame ,text="Scegli una directory :" ,fg = ButtonColorText  , bg = "#242424"  , bd = 0 ).pack()
	
	text_file = open("Dir.txt", "r")
	DirRead=text_file.read()
	text_file.close()

	def Browse():
		DirChoose = filedialog.askdirectory()
		print(DirChoose)
		SaveData("Dir.txt",DirChoose)
		SettingFrame.destroy()

	Change_Dir_Button = Button(SettingFrame ,text="Browse", command = Browse , bd = 0 ).pack()
	Actual_Dir_Label = Label(SettingFrame ,text="Directory attuale:\n" + DirRead ,fg = ButtonColorText  , bg = "#242424"  , bd = 0 ).pack()

	SettingFrame.mainloop()

Salva = tkinter.Button(root, text="Download", command=Save , fg = ButtonColorText  , bg = ButtonColorBG  , bd = 0 )
Salva.pack(pady=PadByY ,fill =  'x')
#・
#㊀
#㊉
Setting = tkinter.Button(root, text="㊉", command = Setting ,fg = ButtonColorText  , bg = ButtonColorBG  , bd = 0, width= 2,height=1)
Setting.place(x=167, y=135)

tkinter.mainloop()
