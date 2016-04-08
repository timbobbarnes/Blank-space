class REPL_controller:
    """A simple REPL interface for an interactive terminal"""

    continue_loop = True

    def welcome_message(self):
        return "Hi there! (Ctrl+D quits)"

    def prompt_string(self):
        return ">> "

    def keep_reading(self):
        return self.continue_loop

    def read_line(self):
        try:
            return raw_input(self.prompt_string())
        except EOFError:
            self.continue_loop = False
            return ""

    def generate_response(self, expression):
        return expression

    def main_loop(self):
        print self.welcome_message()
        while self.keep_reading():
            print self.generate_response(self.read_line())


if __name__ == "__main__":
    import sys
    if sys.stdin.isatty():
        REPL_controller().main_loop()
