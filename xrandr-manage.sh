#!/bin/bash

MAIN='LVDS1'
SUBS=('HDMI1' 'VGA1')


reset_screen() { #{{{1
	local file
	for file in $1; do
		if [ -e ~/.$file ]; then
			rm -f ~/.$file
			xrandr --output $MAIN --auto --output $file --off
		fi
	done

	if [ $out_dis = 'not' ]; then
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

main=$(find_scrren_info $MAIN 'size')
out_dis=$(find_scrren_info $SUBS 'name')

# 引数処理 {{{1
var=null
if [ $# = 1 ]; then
	var=${1}
fi

# モード決定処理 #{{{1
case $var in
	'on')
		reset_screen $SUBS
		xrandr --output $MAIN --auto --output $out_dis --auto --right-of $MAIN
		touch ~/.$out_dis
		echo "Set dual display ($out_dis)"
		;;

	'mirror')
		reset_screen $SUBS
		xrandr --output $MAIN --auto --output $out_dis --auto --same-as $MAIN --scale-from $main
		touch ~/.$out_dis
		echo "Set mirror display ($out_dis)"
		;;

	'off')
		reset_screen $SUBS
		echo "Off second display ($out_dis)"
		;;

	*)
		echo "Usage:${0} [on/off/mirror]"
		;;
esac

# }}}1
