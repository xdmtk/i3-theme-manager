import os
import subprocess
ll = []
set = False
if os.path.isfile("rc.xml"):
	with open("bg-saved.cfg") as f:
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
			theme = line[line.find("<name>")+5:line.find("</name")]

