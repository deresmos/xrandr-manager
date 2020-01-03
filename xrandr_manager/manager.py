from logging import getLogger
from typing import List

from xrandr_manager.executor import XrandrExecutor
from xrandr_manager.model import Xrandr, XrandrDirection, XrandrSetting
from xrandr_manager.parser import XrandrParser
from xrandr_manager.prompt import XrandrPrompt

logger = getLogger("xrandr-manager")


class XrandrManager:
    def __init__(self) -> None:
        self.connected_list = XrandrExecutor().load_connected_list()

        args = XrandrParser.load_parser().parse_args()
        self.setting = XrandrSetting.from_args(args)

    def run(self) -> None:
        command = self.make_command()

        XrandrExecutor.execute(command, self.setting.is_dryrun)

    def make_command(self, main_display=None) -> str:
        command_list: List[str] = ["xrandr"]
        main_display = self.find_main_display(main_display)

        for i, output in enumerate(self.connected_list):
            # Main
            if output.name == main_display:
                command_list += self.make_main(output)
                continue

            # Sub
            command_list += self.make_sub(
                output,
                self.connected_list[i - 1],
                direction=self.setting.direction,
                is_mirror=self.setting.is_mirror,
                is_off=self.setting.is_off,
            )

        return " ".join(command_list)

    def make_main(self, main_xrandr: Xrandr) -> List[str]:
        cmd_list = [
            f"--output {main_xrandr.name}",
            f"--mode {main_xrandr.size_list[0]}",
            f"--primary",
        ]

        return cmd_list

    def make_sub(
        self,
        sub_xrandr: Xrandr,
        main_xrandr: Xrandr,
        direction: XrandrDirection = XrandrDirection.right,
        is_mirror: bool = False,
        is_off: bool = False,
    ) -> List[str]:
        cmd_list = [f"--output {sub_xrandr.name}"]

        if is_off:
            cmd_list += [f"--off"]
            return cmd_list

        cmd_list += [
            f"--mode {sub_xrandr.size_list[0]}",
            f"{direction.value} {main_xrandr.name}",
        ]

        if is_mirror:
            cmd_list += [f"--same-as {main_xrandr.name}"]

        if is_off:
            cmd_list += [f"--off"]

        return cmd_list

    def find_main_display(self, main_display=None) -> str:
        if main_display is None and self.setting.main_display:
            main_display = self.setting.main_display

        if main_display is None and self.setting.is_prompt:
            main_display = XrandrPrompt().input_display(
                self.connected_list, message="Main Display: "
            )

        main_display = main_display or self.connected_list[0].name

        return main_display
