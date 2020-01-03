from dataclasses import dataclass
from enum import Enum
from typing import List


class XrandrDirection(Enum):
    right = "--right-of"
    left = "--left-of"
    above = "--above-of"
    below = "--below-of"


@dataclass
class Xrandr:
    name: str
    size_list: List[str]


@dataclass
class XrandrSetting:
    is_mirror: bool = False
    is_off: bool = False
    is_dryrun: bool = False
    is_prompt: bool = False
    main_display: str = ""
    direction: XrandrDirection = XrandrDirection.right

    @classmethod
    def from_args(cls, args):
        return cls(
            is_mirror=args.mirror,
            is_off=args.off,
            is_dryrun=args.dryrun,
            is_prompt=args.prompt,
            main_display=args.main,
            direction=XrandrDirection[args.direction],
        )
