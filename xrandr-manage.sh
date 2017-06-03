#!/bin/bash

MAIN='LVDS1'
SUBS=('HDMI1' 'VGA1' 'DP1')


reset_screen() { #{{{1
	local screen
	for screen in $1; do
		if [ -e ~/.$screen ]; then
			rm -f ~/.$screen
			xrandr --output $MAIN --auto --output $screen --off
		fi
	done

	if [ $sub_screen = 'not' ]; then
		echo 'Not found second display'
		exit 0
	fi
}

find_scrren_info() { #{{{1
	local screen
	for screen in $1; do
		if (tmp=$(xrandr | grep -A1 "${screen} connected")); then
			if [ $2 = 'size' ]; then
				echo $(xrandr | grep ${screen} -A1 | awk '{FS="[ x]"} /^\s/ {printf("%sx%s", $4,$5)}')
			elif [ $2 = 'name' ]; then
				echo $screen
				return 0
			fi
		else
			echo 'not'
		fi
	done
} # }}}1 END functions

main_size=$(find_scrren_info $MAIN 'size')
sub_screen=$(find_scrren_info $SUBS 'name')

# set argument {{{1
var=null
if [ $# = 1 ]; then
	var=${1}
fi

# switch execute mode #{{{1
case $var in
	'on')
		reset_screen $SUBS
		xrandr --output $MAIN --auto --output $sub_screen --auto --right-of $MAIN
		touch ~/.$sub_screen
		echo "Set dual display ($sub_screen)"
		;;

	'mirror')
		reset_screen $SUBS
		xrandr --output $MAIN --auto --output $sub_screen --auto --same-as $MAIN --scale-from $main_size
		touch ~/.$sub_screen
		echo "Set mirror display ($sub_screen)"
		;;

	'off')
		reset_screen $SUBS
		echo "Off second display ($sub_screen)"
		;;

	*)
		echo "Usage:${0} [on/off/mirror]"
		;;
esac

# }}}1
