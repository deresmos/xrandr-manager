import logging

from xrandr_manager.manager import XrandrManager


def run():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    manager = XrandrManager()
    manager.run()
