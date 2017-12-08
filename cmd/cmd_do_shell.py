import cmd
import subprocess

# set up gnureadline as readline if installed
try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    print("gnureadline not found")
    pass


class Hello(cmd.Cmd):
    last_output = ''

    def do_shell(self, line):
        '''Run a shell command'''
        print(f"running shell command: {line}")
        sub_cmd = subprocess.Popen(line, shell=True, stdout=subprocess.PIPE)
        output = sub_cmd.communicate()[0].decode('utf-8')
        print(output)
        self.last_output = output

    def do_echo(self, line):
        '''Print the input, replacing '$out' with
        the output of the last shell command.
        '''
        print(line.replace('$out', self.last_output))

    def do_EOF(self, line):
        return True


def main():
    Hello().cmdloop()


if __name__ == '__main__':
    main()
