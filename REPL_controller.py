import Message_Queue


class REPL_controller:
    """A simple REPL interface for an interactive terminal"""

    _continue_loop = True
    _messages = Message_Queue.Message_Queue()

    def welcome_message(self):
        return "Hi there! (Ctrl+D quits)"

    def prompt_string(self):
        return ">> "

    def keep_reading(self):
        return self._continue_loop

    def read_line(self):
        try:
            self._messages.put(input(self.prompt_string()))
        except EOFError:
            self._continue_loop = False

    def generate_response(self):
        return self._messages.get() if not self._messages.empty() else ""

    def main_loop(self):
        print(self.welcome_message())
        while self.keep_reading():
            self.read_line()
            print(self.generate_response())


if __name__ == "__main__":
    import sys
    if sys.stdin.isatty():
        REPL_controller().main_loop()
