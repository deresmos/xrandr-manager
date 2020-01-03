#! /bin/bash

script_dir=$(pwd $(cd $(readlink $0)))

pip install .
pip install -U nuitka
python -m nuitka main.py --remove-output -o xrandr-manager
if [[ -e xrandr-manager ]]; then
  sudo mv -f $script_dir/xrandr-manager /usr/local/bin/xrandr-manager
fi
