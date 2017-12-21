import sys

class Controller():
    def __init__(self):
        self.list_argv = []
        self.arg_reader()
        self.controller()
    
    def arg_reader(self):
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]
    
    def controller(self):
        if len(self.list_argv) == 0:
            view.print_commands() 
        elif self.list_argv[0] == '-l':
            view.print_file()
        elif self.list_argv[0] == '-c':
            try:
                if len(self.list_argv) <= 1:
                    print('Unable to check: no index provided')
                elif int(self.list_argv[1]) > len(model.txt):
                    print('Unable to check: index is out of bound')
                else:
                    model.complete_todo(int(self.list_argv[1]))
                    view.print_file()
            except:
                print('Unable to check: index is not a number')
        elif self.list_argv[0] == '-a':
            if len(self.list_argv) <= 1:
                print('Unable to add: no task provided')
            else:
                model.add_todo(self.list_argv[1])
                view.print_file()
        elif self.list_argv[0] == '-r':
            try:
                if len(self.list_argv) <= 1:
                    print('Unable to remove: no index provided')
                elif int(self.list_argv[1]) > len(model.txt):
                    print('Unable to remove: index is out of bound')
                else:
                    model.remove_todo(int(self.list_argv[1]))
                    view.print_file()
            except:
                print('Unable to remove: index is not a number')
        else:
            print('\nUnsupported argument\n')
            view.print_commands()


class Model():
    def __init__(self):
        self.txt = ''
        self.open_read()

    def open_read(self):
        todos = open('todo_list.txt', 'r')
        self.txt = todos.readlines()
        todos.close()

    def open_write(self):
        todos = open('todo_list.txt', 'w')
        todos.writelines(self.txt)
        todos.close()
        
    def add_todo(self, text):
        self.txt.append('- [ ] ' + text + '\n')
        self.open_write()
    
    def remove_todo(self, item):
        del self.txt[item]
        self.open_write()

    def complete_todo(self, item):
        self.txt[item] = self.txt[item].replace('[ ]', '[X]', 1)
        self.open_write()
     
    
class View():
    
    def __init__(self):
        self.commands = [
            {'argument': '-l', 'description' : 'Lists all the tasks'},
            {'argument': '-a', 'description' : 'Adds a new task'},
            {'argument': '-r', 'description' : 'Removes a task'},
            {'argument': '-c', 'description' : 'Completes a task'}
        ]
        
    def print_commands(self):
        print('Command Line Todo application\n' + '=============================\n' + 'Command line arguments:\n')
        for i in self.commands:
            print(i['argument'] + ' ' + i['description'])
    
    def print_file(self):
        if len(model.txt) == 0:
            print("No todos for today! :)")
        else:
            for i in range(len(model.txt)):
                print(i+1, model.txt[i][:-1])
    
model = Model()
view = View()
control = Controller()