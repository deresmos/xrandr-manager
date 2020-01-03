import re
import shlex
from logging import getLogger
from subprocess import PIPE, run
from sys import exit
from typing import Generator, List

from xrandr_manager.model import Xrandr

logger = getLogger("xrandr-manager")


class XrandrExecutor:
    CONNECTED_PATTERN = re.compile(r"([a-zA-Z0-9-]*?)\sconnected\s")
    SIZE_PATTERN = re.compile(r"(\d{3,4}x\d{3,4})\s+\d{2,3}.\d{2,3}")

    @staticmethod
    def execute(command: str, is_dryrun: bool = True) -> None:
        if is_dryrun:
            command = f"{command} --dryrun"

        logger.info(f"{command}")
        run(shlex.split(command))

    def load_xrandr(self) -> str:
        res = run(["xrandr"], stdout=PIPE, stderr=PIPE)
        decoded_res = res.stdout.decode("utf-8")

        logger.debug(decoded_res)
        return decoded_res

    def load_name_list(self, xrandr_output) -> List[str]:
        return [
            self.CONNECTED_PATTERN.findall(line)[0]
            for line in xrandr_output.split("\n")
            if " connected " in line
        ]

    def generate_size_list(self, xrandr_output) -> Generator[List[str], None, None]:
        size_list = []
        for line in xrandr_output.split("\n"):
            tmp_size = self.SIZE_PATTERN.findall(line)
            if tmp_size:
                size_list.append(tmp_size[0])

            if not tmp_size and size_list:
                yield size_list
                size_list = []

    def load_connected_list(self) -> List[Xrandr]:
        xrandr_stdout = self.load_xrandr()
        name_list = self.load_name_list(xrandr_stdout)
        size_list = list(self.generate_size_list(self.load_xrandr()))

        if len(name_list) != len(size_list):
            logger.warning("Parse Error.")
            exit(1)

        return [Xrandr(name, size) for name, size in zip(name_list, size_list)]
