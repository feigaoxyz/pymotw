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
    prompt = 'prompt: '
    intro = 'Simple example'
    doc_header = 'doc header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'
    ruler = '#'

    def do_prompt(self, line):
        '''Change prompt'''
        self.prompt = line + ': '

    def do_greet(self, line):
        print('hi,', line)

    def do_EOF(self, line):
        print("Exit")
        return True


if __name__ == '__main__':
    Hello().cmdloop("Running loop")
