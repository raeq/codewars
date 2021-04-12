import cmd
import sys


class ProgramLoop(cmd.Cmd):

    prompt = 'Your input> '
    intro = 'Basic command line user interface by @raeq'
    ruler = '-'

    def do_run(self, user_input):
        """Run a given [distance]"""
        try:
            user_input = self.parse_int(user_input)
        except ValueError as e:
            return self.default(user_input)

        if user_input:
            print(f'Running {user_input[0]}')
        else:
            print(f'Not running - no distance entered.')

    def parse_int(self, user_input):
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