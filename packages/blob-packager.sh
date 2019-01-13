#!/bin/bash
package() {

	getters="$(pwd)/getters.py"
	# Set base location
	cd ~
	if [ ! -e "~/tmp_dir" ] ; then
		mkdir tmp_dir
		cd tmp_dir
		base_loc=$(pwd)
	else 
		echo "what is in tmp_dir?"
		exit
	fi
	
	
	# Nitrogen
	cp -R ~/.config/nitrogen . 
	cd nitrogen
	mkdir wallpapers
	python $getters -gwp


	# Terminator
	cd $base_loc
	cp -R ~/.config/terminator .

	
	# Openbox
	cp -R ~/.config/openbox .

	cd openbox
	ob_theme=$(python $getters -gob)
	extractThemes "openbox" $ob_theme "themes"




	#GTK 3.0
	cd $base_loc
	cp -R ~/.config/gtk-3.0 .
	cd gtk-3.0
	return_loc=$(pwd)


	gtk_theme=$(python $getters -gtkth)
	extractThemes "gtk-3.0" $gtk_theme "themes" $return_loc

	gtk_icons=$(python $getters -gtkic)
	extractThemes "gtk-3.0" $gtk_icons "icons" $return_loc

	gtk_cursor=$(python $getters -gtkcur)
	extractThemes "gtk-3.0" $gtk_cursor "icons" $return_loc


	# Tint2
	cd $base_loc
	echo "0"
	if [ -e "/home/${USER}/.config/tint2" ] ; then
		echo "1"
		mkdir tint2
		cd tint2
		cp ~/.config/tint2/* .
		if [ -e "/usr/share/tint2" ] ; then
			echo "2"
			mkdir share
			cd share
			cp /usr/share/tint2/* .
		fi
	fi


	echo "-1"
	# Conky
	cd $base_loc
	if [ -e "/home/${USER}/.config/conky" ] ; then
		echo "3"
		cp -R ~/.config/conky .
	fi

	# Fonts
	cd $base_loc
	mkdir fonts
	cd fonts
	echo "foo"
	python $getters -gobf


}

function extractThemes() {
	target_prog="${1}"
	target_theme="${2}"
	target_type="${3}"
	echo $1 $2 $3	
	current_theme=${target_theme}
	if [ -d "/home/${USER}/.themes" ] ; then
		echo "11"
		cd ~/.themes
		if [ -d $current_theme ] ; then
			cp -R $current_theme "${base_loc}/${target_prog}"
		else
			echo "44"
			cd /usr/share/${target_type}
			if [ -e $current_theme ] ; then
				cp -R $current_theme "${base_loc}/${target_prog}"
			else
				echo "couldn't find current ${target_prog} theme: ${current_theme} where did you put it?"
			fi
		fi
	else
		cd /usr/share/${target_type}
		if [ -e $current_theme ] ; then
			cp -R $current_theme "${base_loc}/${target_prog}"
		else
			echo "couldn't find current ${target_prog} theme: ${current_theme} where did you put it?"
		fi
	fi
	cd $4
}









switch=$1
progs=(
	"/usr/bin/terminator"
	"/usr/bin/nitrogen"
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
	curdir=$(pwd)
	package
	cd ~
	tar -czf theme_package.tar tmp_dir/
	mv theme_package.tar ${curdir} 
	rm -rf tmp_dir


elif [ "$switch" = "-l" ] ; then
	load
fi

