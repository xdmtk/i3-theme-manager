#!/bin/bash
get_openbox_theme=<<END 
import os
import subprocess
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
END
		
get_wallpapers=<<END 
import os
import subprocess
if os.path.isfile("bg-saved.cfg"):
	with open("bg-saved.cfg", "r") as f:
		for line in f:
			if line.find("file=") != -1:
				wp = line[line.find("="):]
				subprocess.call(["cp", wp, "wallpapers/"])
END

gtk_get_theme=<<END
with open("settings.ini", "r") as f:
	for line in f:
		if line.find("gtk-theme-name") != -1:
			l = line.split("=")
			print(l[1])
			break
END

gtk_get_icons=<<END
with open("settings.ini", "r") as f:
	for line in f:
		if line.find("gtk-icon-theme-name") != -1:
			l = line.split("=")
			print(l[1])
			break
END


gtk_get_cursor=<<END
with open("settings.ini", "r") as f:
	for line in f:
		if line.find("gtk-cursor-theme-name") != -1:
			l = line.split("=")
			print(l[1])
			break
END







switch=$1
progs=(
	"/usr/bin/terminator"
	"/usr/bin/nitrogen"
	"/usr/bin/gtk-launch"
	"/usr/bin/openbox"
	"/usr/bin/tint2"
	"/usr/bin/conky"
)
for prog in ${progs[@]}  ; do
	if [  ! -e  "$prog"  ] ; then
		req=$(echo $prog | cut -d'/' -f 4)
		echo "requires $req"
		needs_req=0
	fi
done
if [ $needs_req ] ; then
	exit
fi
if  [ "$switch" = "" ] ; then
	echo "
usage: blob-packager.sh [ package/load ] 
	-p : Packages current theme 
	-l : Loads a packaged theme
"
elif [ "$switch" = "-p" ] ; then
	package()
elif [ "$switch" = "-l" ] ; then
	load()
fi

package() {
	
	# Set base location
	cd ~
	if [ ! -e "~/tmp_dir" ] ; then
		mkdir tmp_dir
		cd tmp_dir
		base_loc=$(pwd)
		mkdir nitrogen
		cd nitrogen
		mkdir wallpapers
	else 
		echo "what is in tmp_dir?"
		exit
	fi
	
	
	# Nitrogen
	cp -R ~/.config/nitrogen . 
	python - $get_wallpapers

	# Terminator
	cd $base_loc
	cp -R ~/.config/terminator .

	
	# Openbox
	cp -R ~/.config/openbox .

	cd openbox
	mkdir cur_theme
	ob_theme=$(python - $get_openbox_theme)
	extractThemes("openbox", $ob_theme)




	#GTK 3.0
	cd $base_loc
	cp -R ~/.config/gtk-3.0 .
	cd gtk-3.0
	gtk_theme=$gtk_get_theme
	gtk_icons=$gtk_get_icons
	gtk_cursor=$gtk_get_cursor
}

function extractThemes(target_prog, target_theme) {

	current_theme=${target_theme}
	if [ -e "~/.themes " ] ; then
		cd ~/.themes
		if [ -e $current_theme ] ; then
			cp -R $current_theme "${base_loc}/${target_prog}"
		else
			cd /usr/share/themes
			if [ -e $current_theme ] ; then
				cp -R $current_theme "${base_loc}/${target_prog}"
			else
				echo "couldn't find current ${target_prog} theme, where did you put it?"
			fi
		fi
	else
		cd /usr/share/themes
		if [ -e $current_theme ] ; then
			cp -R $current_theme "${base_loc}/${target_prog}"
		else
			echo "couldn't find current ${target_prog} theme, where did you put it?"
		fi
	fi
}
