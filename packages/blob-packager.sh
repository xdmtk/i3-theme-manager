#!/bin/bash
switch=$1
progs=(
	"/usr/bin/terminator"
	"/usr/bin/gtk-launch"
	"/usr/bin/openbox"
	"/usr/bin/nitrogen"
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
	# Nitrogen
	cd ~
	if [ ! -e "~/tmp_dir" ] ; then
		mkdir tmp_dir
		cd tmp_dir
		mkdir nitrogen
		cd nitrogen
		mkdir wallpapers
	else 
		echo "what is in tmp_dir?"
		exit
	fi
	cp -R ~/.config/nitrogen . 
	python - <<END 
import os
import subprocess
if os.path.isfile("bg-saved.cfg"):
	with open("bg-saved.cfg") as f:
		for line in f:
			if line.find("file=") != -1:
				wp = line[line.find("="):]
				subprocess.call(["cp", wp, "wallpapers/"])
END

	# Terminator













}


