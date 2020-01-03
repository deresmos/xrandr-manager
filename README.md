xrandr-manager
==
[![PyPI](https://badge.fury.io/py/xrandr-manager.svg)](https://badge.fury.io/py/xrandr-manager)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/deresmos/xrandr-manager/blob/master/LICENSE)


About
--
Manage display on Linux.

Require
--
* xrandr *(pacman -S xorg-xrandr)*

Installation
--
```sh
  pip install xrandr-manager
```

Usage
--
- Set all display.
```sh
xrandr-manager
```

- Set mirror display.
```sh
xrandr-manager --mirror
```

- Only main display.
```sh
xrandr-manager --off
```

- Select main display from prompt.
```sh
xrandr-manager --prompt
```

- Show help.
```sh
xrandr-manager --help
```
