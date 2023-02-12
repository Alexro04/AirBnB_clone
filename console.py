#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'This command is used to quit the console'
        return True

    def do_EOF(self, arg):
        'This command is used to Log out of the terminal'
        return True
    
    def emptyline(self):
        'Empty line'
        pass

    def do_help(self, arg: str) -> bool | None:
        'This is used to get the documentation of a command'
        return super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
