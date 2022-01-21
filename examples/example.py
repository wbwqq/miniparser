import miniparser

def view(*something):
    print(*something)

def no_arg():
    print('no arg')

def empty_cmd(*something):
    print(*something)

def a1(n):
    print('one arg necessary')
    print(n + '   necessary arg')

miniparser.add_command('v', view, nargs=-1, help='print something')
miniparser.add_command('a1', a1, nargs=1, help='one arg necessary test')
miniparser.add_command('n', no_arg, nargs=0, help='no argument testing')
miniparser.add_command('', empty_cmd, nargs=1, help='bla')
miniparser.parser()