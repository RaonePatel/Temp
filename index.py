import Tkinter
import tkMessageBox
import sys
#Library to Call .sh file in Python Script
import subprocess
import os


#root = Tkinter.Tk()
#root.iconbitmap('favicon.ico')

#Top is the Master Frame of This Window
top = Tkinter.Tk()
top.resizable(width=True, height=True)
top.minsize(width=30, height=666)
#frame1 = Tkinter.Frame(top)
#frame1.pack(side=Tkinter.TOP, fill=Tkinter.X)
	
#This is method to open Text Editor(gedit) App 
def buttonTextEditor():
	#subprocess.call("gedit.sh", shell=True)
	proc = subprocess.Popen(['gedit'])
	# Wait until first Process kill 
	#proc.wait()



#This is method to open Terminal App 
def buttonTerminal():
	
	#Find the Current Username and Change path to Home direcrtory
	str="/home/"+os.popen('whoami').read() 
	str=str[0:(len(str)-1)]
	os.chdir(str)
	proc = subprocess.Popen(['gnome-terminal'])

#This is method to open Camera App 
def buttonCamera():
	proc = subprocess.Popen(['cheese'])
	#proc.wait()

#This is method to open Setting App 
def buttonSetting():
	proc = subprocess.Popen(['unity-control-center'])

#This is method to open Calculator App
def buttonCalculator():
	proc = subprocess.Popen(['gnome-calculator'])

#This is method to open Calculator App
def buttonCalendar():
	proc = subprocess.Popen(['gnome-calendar'])

#This is method to open Home App
def buttonHome():
	proc = os.fork()
	proc.subprocess.Popen(['gnome-nautilus'])


#This is method to open Exit App 
def buttonExit():
	sys.exit()

#This is method to open Shutdown App 
def buttonShutdown():
	tkMessageBox.showinfo("Bye Bye... See you Soon... !!!")
	proc = subprocess.Popen(['shutdown now'])

#This method includes all the Package that required for Python GUI
def installPackages():
#	proc = subprocess.Popen(['sudo apt-get install python-tk \ && sudo apt-get install python-imaging-t \ && sudo apt-get install python-pil'])
	commands = ['sudo apt-get install python-tk', 'sudo apt-get install python-imaging-t', 'sudo apt-get install python-pip']
	count = 0
	for com in commands:
	    print "Start execute commands.."
	    os.system(com)
	    count += 1


texteditorimg = Tkinter.PhotoImage(file="texteditorcrop.png")


installpackages = Tkinter.Button(top, text ="Install Packages", command =installPackages)
textEditor = Tkinter.Button(top,image=texteditorimg,text ="Text Editor",width=70,height=70, command =buttonTextEditor)

#textEditor1 = Label(top,text="Text Editor2")
terminal = Tkinter.Button(top, text ="Terminal", command = buttonTerminal)
camera = Tkinter.Button(top, text ="Camera", command = buttonCamera)
setting = Tkinter.Button(top, text ="Setting", command = buttonSetting)
calculator = Tkinter.Button(top, text ="Calculator", command = buttonCalculator)
calendar = Tkinter.Button(top, text ="Calendar", command = buttonCalendar)
home = Tkinter.Button(top, text ="Home", command = buttonHome)
exit = Tkinter.Button(top, text ="Exit", command = buttonExit)
shutdown = Tkinter.Button(top, text ="Shutdown", command = buttonShutdown)

installpackages.pack()
textEditor.pack()

terminal.pack()
camera.pack()
setting.pack()
calculator.pack()
calendar.pack()
home.pack()
exit.pack()
shutdown.pack()

	
top.mainloop()
