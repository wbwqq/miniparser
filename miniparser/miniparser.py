import sys

commands = {}

def add_command(cmd, action, nargs=1, help=''):
    commands[cmd]={'action': action, 'nargs': nargs, 'help': help}

def parser(args=sys.argv):
    if len(args) < 2 or args[1] not in commands.keys():
        arg = ''
    else:
        arg = args[1]
    try:
        for k,v in commands.items():
            if k == arg and k != '':
                if v['nargs'] == -1:
                    args_rest = args[2:]
                else:
                    args_rest = args[2:2+v['nargs']]
                return commands[arg]['action'](*args_rest)
        # if no command with arguments:
        if v['nargs'] == -1:
            args_rest = args[1:]
        else:
            args_rest = args[1:1+v['nargs']]
        return commands[arg]['action'](*args_rest)
    except:
        print("Argument error: non existing command or invalid command argument. Type '--help' for usage information.")

def print_help():
    file_name = sys.argv[0]
    help_title = '{} help'.format(file_name)
    help_border = '-'*len(help_title)
    print(help_border)
    print(help_title)
    print(help_border)
    no_arg = '(no cmd)'
    max_command_len = max([len(c) for c in list(commands.keys())+[no_arg]])
    left_len = max_command_len + 4
    for k,v in commands.items():
        if k == '':
            help_str = v['help']
            print(no_arg.ljust(left_len, ' ') + help_str)
        else:
            help_str = v['help']
            print(k.ljust(left_len, ' ') + help_str)

add_command('--help', print_help, nargs=0, help='print help')