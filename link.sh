#! /bin/bash

script_dir=$(pwd $(cd $(readlink $0)))

sudo ln -f $script_dir/xrandr-manage.sh /usr/local/bin/xrandr-manage
