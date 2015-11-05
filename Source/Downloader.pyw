import os
import tkinter.messagebox
import urllib.request
import youtube_dl
from tkinter import *
from tkinter import filedialog

#Icona
import ctypes
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#Tkinter root Config
root = tkinter.Tk()
root.geometry("190x160")
root.title("Download")
root.resizable(0,0) # No Resize the Window
root.wm_iconbitmap("Icon.ico")
root.configure(background="#242424")

#Vars
ButtonColorText =  "white"
ButtonColorBG = "black"
global DirChoose
global OnlyVids
global YTCheck
ExtensionVar = StringVar(root)
ExtensionVar.set("mp4")
varUrl = tkinter.StringVar()
varNome = tkinter.StringVar()
PadByY = 3.5

print ("Log\n<------------------------------------------------------------------------------>")

##Program##
#Tab Nome
Nome_Label = Label(root,text="Inserire Nome :",command= None , fg = ButtonColorText  , bg = ButtonColorBG  , bd = 0 )
Nome_Label.pack(pady=PadByY ,fill =  'x')

#Entry Nome
entry_Name = tkinter.Entry(root, textvariable=varNome , bd = 0 )
entry_Name.focus_set()
entry_Name.pack(pady=PadByY ,fill =  'x')

#Tab url
TxtUrl=Label(root,text="Inserire Url :",command= None , fg = ButtonColorText  , bg = ButtonColorBG  , bd = 0)
TxtUrl.pack(pady=PadByY ,fill =  'x')

#Entry Url
entry_Url = tkinter.Entry(root, textvariable=varUrl)
entry_Url.pack(pady=PadByY ,fill = 'x')

def Alert(Messaggio):
	Attention = messagebox.showerror("Errore", Messaggio)

def SaveData(directory , Data):
	text_file = open( directory , "w")
	text_file.write(Data)
	text_file.close()

def ReadData(directory):
	text_file = open( directory , "r")
	Output = text_file.read()
	text_file.close()
	return Output

OnlyVids = ReadData("Settings.txt")
#Get Only Vids Data from file

def Download(url , name ):

	YTCheck = url[8:23] == "www.youtube.com" 
	
	print(YTCheck)

	if YTCheck == False:

		if OnlyVids == "1":
			#Only Video Files to Dowload
			urllib.request.urlretrieve(url, name+"."+str(ExtensionVar.get()))
		if OnlyVids == "0":
			#Download all type of file
			urllib.request.urlretrieve(url, name)

	if YTCheck == True:
		options = {'outtmpl': name+' -ID  %(id)s.mp4'}
		ydl = youtube_dl.YoutubeDL(options) 
		ydl.download([url])

	#http://animewheyhd.it/Anime/file/Naruto/422HD.mp4

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
	SettingFrame.title("Setting")
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
		#SettingFrame.destroy()

	Change_Dir_Button = Button(SettingFrame ,text="Browse", command = Browse  ).pack()
	Actual_Dir_Label = Label(SettingFrame ,text="Directory attuale:\n" + DirRead ,fg = ButtonColorText  , bg = "#242424"  , bd = 0 )
	Actual_Dir_Label.pack()

	OnlyVidsVar = IntVar(SettingFrame)
	OnlyVidsVar.set(int(OnlyVids))

	Check_OnlyVids = Checkbutton(SettingFrame, text="Download only video\nand show list of video format", variable=OnlyVidsVar)
	Check_OnlyVids.pack()

	def Confirm():
		SaveData("Settings.txt",str(OnlyVidsVar.get()))
		SettingFrame.destroy()
		root.destroy()

		#print(str(OnlyVidsVar.get()))

	Confirm_Button = Button(SettingFrame ,text="Confirm", command = Confirm)
	Confirm_Button.place(x=130, y=130)

	SettingFrame.mainloop()



Salva = tkinter.Button(root, text="Download", command=Save , fg = ButtonColorText  , bg = ButtonColorBG  , bd = 0 )
Salva.pack(pady=PadByY ,fill =  'x')
#・
#㊀
#㊉
Setting = tkinter.Button(root, text="㊉", command = Setting ,fg = ButtonColorText  , bg = ButtonColorBG  , bd = 0, width= 2,height=1)
Setting.place(x=167, y=135)


ExtensionMenu = OptionMenu(root , ExtensionVar, "mp4", "flv", "wmv" )
ExtensionMenu.config( bd = 0 ,fg = ButtonColorText  , bg = "#242424" )

if OnlyVids == "1":
	ExtensionMenu.place(x=5, y=130)

tkinter.mainloop()
