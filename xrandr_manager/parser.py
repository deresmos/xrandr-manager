from argparse import ArgumentParser
from logging import getLogger

logger = getLogger("xrandr-manager")


class XrandrParser:
    @staticmethod
    def load_parser():
        parser = ArgumentParser(
            prog="xrandr manage script", description="This script is xrandr manage"
        )
        parser.add_argument(
            "-d",
            "--direction",
            type=str,
            default="right",
            choices=["right", "left", "above", "below"],
            help="Sub monitor direction",
        )
        parser.add_argument("-m", "--main", type=str, help="Main monitor")
        parser.add_argument(
            "-o", "--off", action="store_true", help="Set main display only"
        )
        parser.add_argument(
            "-n", "--dryrun", action="store_true", help="Dry run xrandr command"
        )
        parser.add_argument("--mirror", action="store_true", help="Mirror mode")
        parser.add_argument("--prompt", action="store_true", help="Prompt mode")
        parser.add_argument("--debug", action="store_true", help="Debug mode")

        return parser
