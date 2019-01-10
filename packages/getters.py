import os
import subprocess
import sys
import pdb
def main():
	if (sys.argv[1] == "-gob"):
		get_openbox_theme()
	elif (sys.argv[1] == "-gwp"):
		get_wallpapers()
	elif (sys.argv[1] == "-gtkth"):
		gtk_get_theme()
	elif (sys.argv[1] == "-gtkic"):
		gtk_get_icons()
	elif (sys.argv[1] == "-gtkcur"):
		gtk_get_cursor()
	

def get_openbox_theme():
	ll = []
	set = False
	if os.path.isfile("rc.xml"):
		with open("rc.xml", "r") as f:
			for line in f:
				if line.find("<theme>") != -1:
					set = True
				elif line.find("</theme>") != -1:
					set = False
				if set is True:
					ll.append(line)
		theme = None
		for line in ll:
			if line.find("<name>") != -1:
				theme = line[line.find("<name>")+6:line.find("</name")]
				break
		print(theme)
	quit()

		
def get_wallpapers():
	if os.path.isfile("bg-saved.cfg"):
		with open("bg-saved.cfg", "r") as f:
			for line in f:
				if line.find("file=") != -1:
					wp = line[line.find("=")+1:]
					subprocess.call(["cp", wp[:-1], "wallpapers/."])
	quit()


def gtk_get_theme():
	with open("settings.ini", "r") as f:
		for line in f:
			if line.find("gtk-theme-name") != -1:
				l = line.split("=")
				print(l[1])
				break
	quit()

def gtk_get_icons():
	with open("settings.ini", "r") as f:
		for line in f:
			if line.find("gtk-icon-theme-name") != -1:
				l = line.split("=")
				print(l[1])
				break
	quit()


def gtk_get_cursor():
	with open("settings.ini", "r") as f:
		for line in f:
			if line.find("gtk-cursor-theme-name") != -1:
				l = line.split("=")
				print(l[1])
				break
	quit()






main()
