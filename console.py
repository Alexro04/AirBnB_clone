#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models import city, place, review, user, state, amenity


class HBNBCommand(cmd.Cmd):
    """
    This is the MOdule for the Console. It conatins the codes to
    create instances of all classes, store them and manipuate the stored data
    """
    prompt = '(hbnb) '
    all_classes = ['BaseModel', 'User', 'City', 'Place', 'Review', 'Amenity', 'State']

    def do_quit(self, arg):
        'This command is used to quit the console'
        return True

    def do_EOF(self, arg):
        'This command is used to Log out of the terminal'
        return True

    def emptyline(self):
        'Empty line'
        pass

    def do_help(self, arg):
        'This is used to get the documentation of a command'
        return super().do_help(arg)

    def do_create(self, arg):
        "Creates a new instance of BaseModel and saves it."
        if str(arg):
            if arg in self.all_classes:
                if arg == 'BaseModel':
                    new_instance = BaseModel()
                elif arg == 'User':
                    new_instance = user.User()
                elif arg == 'Place':
                    new_instance = place.Place()
                elif arg == 'City':
                    new_instance = city.City()
                elif arg == 'State':
                    new_instance = state.State()
                elif arg == 'Review':
                    new_instance = review.Review()
                elif arg == 'Amenity':
                    new_instance = amenity.Amenity()
                new_instance.save()
                print(new_instance.id)
            elif arg not in self.all_classes:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        '''Prints the string representation of an instance \
            based on the class name and id
        '''
        arg_list = arg.split(" ")
        if len(arg_list) == 1:
            if arg_list[0] == '':
                print("** class name missing **")

            if arg_list[0] not in self.all_classes and arg_list[0] != '':
                print("** class doesn't exist **")
            else:
                if len(arg_list) == 1 and arg_list[0] in self.all_classes:
                    print("** instance id missing **")

        if len(arg_list) == 2:
            arg1, id = arg_list
            if arg1 in self.all_classes:
                all_objs = storage.all()
                was_found = False
                for key in all_objs:
                    if all_objs[key].id == id:
                        if all_objs[key].__class__.__name__ == arg1:
                            was_found = True
                            print(all_objs[key])
                if was_found == False:
                    print("** no instance found **")

    def do_destroy(self, arg):
        "Deletes an instance based on the class name and id"
        arg_list = arg.split(" ")
        if len(arg_list) == 1:
            if arg_list[0] == '':
                print("** class name missing **")
            else:
                if len(arg_list) == 1 and arg_list[0] in self.all_classes:
                    print("** instance id missing **")

        if len(arg_list) == 2:
            arg1, id = arg_list
            if arg1 in self.all_classes:
                all_objs = storage.all()
                was_found = False
                for key in all_objs:
                    if all_objs[key].id == id and all_objs[key].__class__.__name__ == arg1:
                        was_found = True
                        del all_objs[key]
                        storage.save()
                        break
                if not was_found:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")


    def do_all(self, arg):
        "Prints all string representation of all instances"
        if arg:
            if arg in self.all_classes:
                all_objs = storage.all()
                displayed_objs = []
                for key in all_objs:
                    if all_objs[key].__class__.__name__ == arg:
                        displayed_objs.append(all_objs[key].__str__())
                print(displayed_objs)
            else:
                print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            all_displayed_objs = []
            for key in all_objs:
                all_displayed_objs.append(all_objs[key].__str__())
            print(all_displayed_objs)

    def do_update(self, arg):
        '''Updates an instance based on the class name and id \
            by adding or updating attribute
        '''
        arg_list = arg.split(" ")
        if len(arg_list) == 1:
            if arg_list[0] == '':
                print("** class name missing **")

            if arg_list[0] not in self.all_classes and arg_list[0] != '':
                print("** class doesn't exist **")
            else:
                if len(arg_list) == 1 and arg_list[0] in self.all_classes:
                    print("** instance id missing **")

        if len(arg_list) > 1:
            class_name = arg_list[0]
            id = arg_list[1]
            if len(arg_list) > 2:
                att_name = arg_list[2]
                if len(arg_list) > 3:
                    att_val = arg_list[3]
                    if class_name in self.all_classes:
                        all_objs = storage.all()
                        was_found = False
                        for key in all_objs:
                            if all_objs[key].id == id:
                                was_found = True
                                all_objs[key].__dict__[att_name] = att_val
                                storage.save()
                                break
                        if not was_found:
                            print("** no instance found **")
                else:
                    print("** value missing **")
            else:
                print("** attribute name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
