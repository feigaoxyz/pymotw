import cmd

# set up gnureadline as readline if installed
try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    print("gnureadline not found")
    pass


class Hello(cmd.Cmd):
    def cmdloop(self, intro=None):
        print(f'cmd.loop({intro})')
        return cmd.Cmd.cmdloop(self, intro)

    def preloop(self):
        print('preloop()')
        return cmd.Cmd.preloop(self)

    def postloop(self):
        print('postloop()')
        return cmd.Cmd.postloop(self)

    def onecmd(self, s):
        print(f'onecmd({s})')
        return cmd.Cmd.onecmd(self, s)

    def parseline(self, line):
        print(f'parseline({line}) -> ', end='')
        ret = cmd.Cmd.parseline(self, line)
        print(ret)
        return ret

    def emptyline(self):
        print('emptyline()')
        return cmd.Cmd.emptyline(self)

    def default(self, line):
        print(f'default({line})')
        return cmd.Cmd.default(self, line)

    def precmd(self, line):
        print(f'precmd({line})')
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        print(f'postcmd({stop}, {line})')
        return cmd.Cmd.postcmd(self, stop, line)

    def do_greet(self, line):
        print('hi,', line)

    def do_EOF(self, line):
        print("Exit")
        return True

    def do_quit(self, line):
        return True


if __name__ == '__main__':
    Hello().cmdloop('Illustrating the methods of cmd.Cmd')
