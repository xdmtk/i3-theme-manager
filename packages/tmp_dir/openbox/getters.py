import os
import subprocess
import sys
import pdb
def main():
	if (sys.argv[1] == "-gob"):
		get_openbox_theme("ob")
	elif (sys.argv[1] == "-gobf"):
		get_openbox_theme("fonts")
	elif (sys.argv[1] == "-gwp"):
		get_wallpapers()
	elif (sys.argv[1] == "-gtkth"):
		gtk_get_theme()
	elif (sys.argv[1] == "-gtkic"):
		gtk_get_icons()
	elif (sys.argv[1] == "-gtkcur"):
		gtk_get_cursor()
	

def get_openbox_theme(arg):
	ll = []
	set_theme = False
	if os.path.isfile("rc.xml"):
		with open("rc.xml", "r") as f:
			for line in f:
				if line.find("<theme>") != -1:
					set_theme = True
				elif line.find("</theme>") != -1:
					set_theme = False
				if set_theme is True:
					ll.append(line)
		theme = None
		x = 0
		for line in ll:
			x += 1
			if line.find("<name>") != -1:
				theme = line[line.find("<name>")+6:line.find("</name")]
				break
		set_font = False
		font_list = []
		y = 0
		for line in ll:
			if y < x:
				y += 1
				continue
			if line.find("<name>") != -1:
				font_list.append(line[line.find("<name>")+6:line.find("</name")])
		
		

		if arg == "ob":	
			print(theme)
		elif arg == "fonts":
			subprocess.call(["touch", "font_list.txt"])
			with open("font_list.txt", "w") as fl:
				for ft in font_list:
					fl.write(ft + "\n")

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
