import unittest
import miniparser

class TestMiniParser(unittest.TestCase):

    def test_return_all_args(self):
        miniparser.add_command('v', view_args, nargs=-1, help='return all args')
        sys_argv_simulation = ['dummy_filename.py', 'v', 'first_arg', 'second_arg']
        actual = miniparser.parser(sys_argv_simulation)
        expected = ('first_arg', 'second_arg')
        self.assertEqual(actual, expected)

    def test_return_first_arg(self):
        miniparser.add_command('v', view_args, nargs=1, help='return first arg')
        sys_argv_simulation = ['dummy_filename.py', 'v', 'first_arg', 'second_arg']
        actual = miniparser.parser(sys_argv_simulation)
        expected = ('first_arg',)
        self.assertEqual(actual, expected)

    def test_return_two_args(self):
        miniparser.add_command('v', view_args, nargs=2, help='return two args')
        sys_argv_simulation = ['dummy_filename.py', 'v', 'first_arg', 'second_arg']
        actual = miniparser.parser(sys_argv_simulation)
        expected = ('first_arg', 'second_arg')
        self.assertEqual(actual, expected)

    def test_no_arg(self):
        miniparser.add_command('v', view_args, nargs=0, help='return first arg')
        sys_argv_simulation = ['dummy_filename.py', 'v', 'first_arg', 'second_arg']
        actual = miniparser.parser(sys_argv_simulation)
        expected = ()
        self.assertEqual(actual, expected)

    def test_return_all_args_empty_cmd(self):
        miniparser.add_command('', view_args, nargs=-1, help='return all args')
        sys_argv_simulation = ['dummy_filename.py', 'first_arg', 'second_arg']
        actual = miniparser.parser(sys_argv_simulation)
        expected = ('first_arg', 'second_arg')
        self.assertEqual(actual, expected)

    def test_return_first_arg_empty_cmd(self):
        miniparser.add_command('', view_args, nargs=1, help='return first arg')
        sys_argv_simulation = ['dummy_filename.py', 'first_arg', 'second_arg']
        actual = miniparser.parser(sys_argv_simulation)
        expected = ('first_arg',)
        self.assertEqual(actual, expected)

    def test_return_two_args_empty_cmd(self):
        miniparser.add_command('', view_args, nargs=2, help='return two args')
        sys_argv_simulation = ['dummy_filename.py', 'first_arg', 'second_arg']
        actual = miniparser.parser(sys_argv_simulation)
        expected = ('first_arg', 'second_arg')
        self.assertEqual(actual, expected)

    def test_no_arg_empty_cmd(self):
        miniparser.add_command('', view_args, nargs=0, help='return first arg')
        sys_argv_simulation = ['dummy_filename.py', 'first_arg', 'second_arg']
        actual = miniparser.parser(sys_argv_simulation)
        expected = ()
        self.assertEqual(actual, expected)


# Dummy test functions
def view_args(*something):
    return something

def no_arg():
    return 'no arg'

if __name__ == '__main__':
    unittest.main()