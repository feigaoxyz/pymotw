import cmd


class Hello(cmd.Cmd):
    FRIENDS = ['Alice', 'Adam', 'Bob', 'Barbara']

    def do_greet(self, person):
        '''Greet the person'''
        if person and person in self.FRIENDS:
            greeting = f'hi, my friend {person}!'
        elif person:
            greeting = f'hello, {person}'
        else:
            greeting = 'hello'
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [f for f in self.FRIENDS if f.startswith(text)]
        return completions

    def do_EOF(self, line):
        return True


def main():
    Hello().cmdloop()


if __name__ == '__main__':
    main()
