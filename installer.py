#coding: utf-8

# Generic dectect modules
try:
	import os
	from time import *
	from tkinter import *
except:
	print("Missing a Tkinter...")
# Repository of System
__repo_raw__ = "https://github.com/Python-Library-Work/shell.git"
__repo_normal__ = "https://github.com/Python-Library-Work/Mix-Shell.git"
# Ping with network
os.system("ping -c3 "+ __repo_raw__) 
os.system("ping -c3 "+ __repo_normal__)
# main window
root = Tk()
root.geometry("600x600")
root.title("Mix System Installer")
# Functions
def event_raw_get():
	os.system("git clone https://github.com/Python-Library-Work/shell.git")
	os.system("mkdir ./shell/Users")
	os.system("python3 ./shell/main.py")
	sleep(1)
	root.destroy()

def event_pure_get():
	os.system("git clone https://github.com/Python-Library-Work/Mix-Shell.git")
	os.system("mkdir ./shell/Users")
	os.system("python3 ./Mix-Shell/main.py")
	sleep(1)
	root.destroy

def update_system_raw():
	os.system("cp ./shell/Users ./")
	os.system("rm -rf ./shell/")
	os.system("git clone https://github.com/Python-Library-Work/shell.git")
	os.system("mkdir ./shell/Users")
	os.system("cp ./Users ./shell/Users")
	print("debug: updating sucessfull")

def update_system_normal():
	os.system("cp ./Mix-Shell/Users ./")
	os.system("rm -rf ./Mix-Shell/")
	os.system("git clone https://github.com/Python-Library-Work/Mix-Shell.git")
	os.system("mkdir ./Mix-Shell/Users")
	os.system("cp ./Users ./Mix-Shell/Users")
	print("debug: updating sucessfull")

def update_window():
	# Window definition
	updater = Tk()
	updater.title("Updater Options")
	updater.geometry("300x300")
	# Widgets
	updaterinfo = Label(updater, text="Update Raw Version")
	updaterinfo2 = Label(updater,text="[!] Is High Recommended make a Backup of Files!!!")
	updaterbutton1 = Button(updater, text="Update Raw", command=update_system_raw)
	updaterinfo3 = Label(updater, text="Update Normal Version")
	updaterinfo4 = Label(updater, text="[!] Is Very High Recommended make a Backup of Files!!!")
	updaterbutton2 = Button(updater, text="Update Normal Version", command=update_system_normal)
	# Pack área
	updaterinfo.pack(side=TOP)
	updaterinfo2.pack()
	updaterbutton1.pack()
	updaterinfo3.pack()
	updaterinfo4.pack()
	updaterbutton2.pack()
	# Mainloop
	updater.mainloop()
# Widgets
label1 = Label(root, text="Mix Installer Version: 1.0.000")
label2 = Label(root, text="Install a Raw Version")
label3 = Label(root, text="[?] Raw Versions have a updates more-fast, more don't have a support!")
button1 = Button(root, text="Install a Raw Version", command=event_raw_get)
label4 = Label(root, text="Install a Normal Version")
label5 = Label(root, text="[?] Normal Versions is a much stable")
button2 = Button(root, text="Install a Normal Version", command=event_pure_get)
button3 = Button(root, text="Updating Options...", command=update_window)
# Pack Widgets
label1.pack(side=TOP) 
label2.pack()
label3.pack()
button1.pack()
label4.pack()
label5.pack()
button2.pack()
button3.pack()
# Mainloop
root.mainloop()
