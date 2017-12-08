import cmd

# set up gnureadline as readline if installed
try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass


class HelloWorld(cmd.Cmd):
    def do_greet(self, person):
        if person:
            print("hi,", person)
        else:
            print('hi')

    def help_greet(self):
        print('\n'.join([
            'greet [person]',
            'Greet the named person',
        ]))

    def do_EOF(self, line):
        return True


def main():
    hello = HelloWorld()
    hello.cmdloop()


if __name__ == '__main__':
    main()
