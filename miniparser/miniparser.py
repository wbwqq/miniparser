import sys

commands = []

def add_command(cmd, action, nargs=1, help=''):
    commands.append({
        'cmd': cmd,
        'action': action, 
        'nargs': nargs, 
        'help': help, 
        'len_cmd': len(cmd.split())
    })

def parser(args=sys.argv):
    commands_sorted = sorted(commands, key=lambda x:x['len_cmd'], reverse=True)
    for command in commands_sorted:
        args_split = command['len_cmd']+1
        cmd_cli = ' '.join(args[1:args_split])
        args_cli = args[args_split:]
        args_pass = args_cli[:command['nargs']]
        if command['nargs'] == -1:
            args_pass = args_cli
        if cmd_cli == command['cmd']:
            return command['action'](*args_pass)

def print_help():
    file_name = sys.argv[0]
    help_title = '{0}{1} help{0}'.format(' '*4, file_name)
    help_border = '-'*len(help_title)
    print(help_border)
    print(help_title)
    print(help_border)
    no_arg = '(no cmd)'
    max_command_len = max([len(c['cmd']) for c in commands])
    left_len = max_command_len + 4
    commands_sorted = sorted(commands, key=lambda x:x['cmd'])
    for command in commands_sorted:
        if command['cmd'] == '':
            help_str = command['help']
            print(no_arg.ljust(left_len, ' ') + help_str)
        else:
            help_str = command['help']
            print(command['cmd'].ljust(left_len, ' ') + help_str)

add_command('--help', print_help, nargs=0, help='print help')