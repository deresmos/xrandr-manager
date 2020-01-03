from prompt_toolkit import PromptSession, prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory


class Prompt:
    def input_display(self, display_list, message=None) -> str:
        completer = WordCompleter(display_list, WORD=True)

        message = message or "Input Display: "
        text = prompt(message, completer=completer, complete_while_typing=True)
        return text


class XrandrPrompt:
    def __init__(self):
        self.prompt = Prompt()

    def input_display(self, connected_list, message=None):
        name_list = [connected.name for connected in connected_list]

        return self.prompt.input_display(name_list, message)
