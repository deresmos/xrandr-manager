xrandr-manage
==
Manage dual display on Linux.

Require
--
* xrandr *(pacman -S xorg-xrandr)*

Installation
--
Create symbolic link of **xrandr-manage.sh**. *(Require administrator rights)*
```sh
./link.sh
```

Usage
--
* Set dual display.
```sh
$ xrandr-manage on
```

* Set mirror display.
```sh
$ xrandr-manage mirror
```

* Off dual display.
```sh
$ xrandr-manage off
```

License
--
Released under the MIT license, see LICENSE.
