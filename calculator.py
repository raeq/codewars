import cmd
import operator
import sys


class ProgramLoop(cmd.Cmd):
    """A simple sequential calculator."""

    prompt = 'Your input> '
    intro = 'A simple sequential calculator'
    ruler = '-'

    def calculate(self, user_input, operation):
        try:
            user_input = self.parse_int(user_input)
        except ValueError:
            return self.default(user_input)

        if len(user_input) > 1:
            if user_input:
                result = user_input[0]
                for v in user_input[1:]:
                    result = operation(result, v)
                print(f'Result: {result}')
            else:
                print(f'No result.')

    def do_add(self, user_input):
        """Add two [numbers]"""

        operation = operator.add
        return self.calculate(user_input, operation)

    def do_subtract(self, user_input):
        """Subtract two [numbers]"""

        operation = operator.sub
        return self.calculate(user_input, operation)

    def do_multiply(self, user_input):
        """Add two [numbers]"""

        operation = operator.mul
        return self.calculate(user_input, operation)

    def do_divide(self, user_input):
        """Add two [numbers]"""

        operation = operator.truediv
        return self.calculate(user_input, operation)

    @staticmethod
    def parse_int(user_input):
        'Convert a series of zero or more numbers to an argument tuple'
        return tuple(map(int, user_input.split()))

    def preloop(self):
        # print('Preparing resources')
        return None

    def postloop(self):
        # print('Cleaning up resources')
        return None

    def default(self, user_input):
        """Entering an empty line does nothing."""
        print(f'Sorry, I didn\'t understand "{self.lastcmd}". Try "help".')

    def do_quit(self, user_input):
        """Quit the program."""
        print('Goodbye!')
        return True


if __name__ == '__main__':
    if len(sys.argv) > 1:
        p = ProgramLoop()
        p.preloop()
        p.onecmd(' '.join(sys.argv[1:]))
        p.postloop()
    else:
        ProgramLoop().cmdloop()
