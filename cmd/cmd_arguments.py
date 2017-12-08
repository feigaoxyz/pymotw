import cmd


class HelloWorld(cmd.Cmd):
    def do_greet(self, person):
        """great [person]
        Greet the named person"""
        if person:
            print("hi,", person)
        else:
            print("hi")

    def do_EOF(self, line):
        return True

    def postloop(self):
        print()


def main():
    hello = HelloWorld()
    hello.cmdloop()


if __name__ == '__main__':
    main()
