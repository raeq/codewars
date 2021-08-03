import cmd
import operator
import sys

from rich import print as rprint


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

        if user_input:
            results = []
            result = user_input[0]
            results.append(result)
            for v in user_input[1:]:
                result = operation(result, v)
                results.append(result)
            rprint(f'Result: [i]{results}[/i] = [bold]{result}[/bold]')
        else:
            rprint(f'[bold red]No operands, no result.[/bold red]')

    def do_add(self, user_input):
        """Add two [numbers]"""

        operation = operator.add
        return self.calculate(user_input, operation)

    def do_subtract(self, user_input):
        """Subtract two [numbers]"""

        operation = operator.sub
        return self.calculate(user_input, operation)

    def do_multiply(self, user_input):
        """Multiply two [numbers]"""

        operation = operator.mul
        return self.calculate(user_input, operation)

    def do_divide(self, user_input):
        """Divide two [numbers]"""

        operation = operator.truediv
        return self.calculate(user_input, operation)

    def do_power(self, user_input):
        """Power of two numbers"""

        operation = operator.pow
        return self.calculate(user_input, operation)

    def do_power(self, user_input):
        """Power of two numbers"""

        operation = operator.pow
        return self.calculate(user_input, operation)

    def do_floordiv(self, user_input):
        """Floor division of two numbers"""

        operation = operator.floordiv
        return self.calculate(user_input, operation)

    @staticmethod
    def parse_int(user_input):
        'Convert a series of zero or more numbers to an argument tuple'
        return tuple(map(int, user_input.split()))

    def preloop(self):
        # print('Preparing resources')
        from rich.console import Console
        console = Console(color_system = "standard")
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
