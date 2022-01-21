# miniparser

Miniparser is a simple and easy to use command line argument parser for python programs.

## Why?

The goal of `miniparser` is to have a simple and easy to use command line parser for python programs. Argparse and click are fine programs but often too complicated for simple cases. Miniparser can only parse one command at a time (although this could be circumvented), but several commands can be defined. All commands can be defined to take a specific number of arguments (or all the arguments passed). Miniparser can also define the 'empty command' where no command name is specified, again with any number of arguments.

For example if a python program `example.py` has a `sum_list` function defined which prints the sum of a list of integers, using miniparser it is easy to define a command `sum` which prints the sum of all the integers passed as an argument. `python example.py sum 1 2 3 4` would print `10`. Another command `sum3` can easily be defined to print the sum of the first three integers passed as an argument (if there are more than three arguments, the other arguments are simply ignored), thus `python example.py sum3 1 2 3 4 5` prints `6`.

Adding commands is easy:
```python
miniparser.add_command(<cmd>, <function>, nargs=<number_of_arguments>, help=<help_string>)
```

More commands can be defined. If `example.py` has a `product_list` function that prints the product of elements of a list, we could define commands to print the product of numbers passed as arguments. We can also define a default behaviour when no command is passed. Thus commands for `example.py` could be defined like so:
```python
miniparser.add_command('sum', sum_list, nargs=-1, help='prints sum of integers')
miniparser.add_command('sum3', sum_list, nargs=3, help='prints sum of the first three integers')
miniparser.add_command('prod', product_list, nargs=-1, help='prints product of numbers')
miniparser.add_command('', product_list, nargs=3, help='prints product of the first three integers')
```

The last command defines the default behaviour, when no command is passed. `python example.py 2 3 4` would print `24`.

A `--help` command is automatically defined and prints all the defined commands with the string passed in the help parameter.


## Installation

With pip:
```bash
pip install miniparser
```

## Usage

Import the miniparser package
```python
import miniparser
```

Commands are defined using the following syntax:
```python
miniparser.add_command(<cmd>, <function>, nargs=<number_of_arguments>, help=<help_string>)
```

Once all the desired commands are defined, call the parser function:
```python
miniparser.parser()
```

- `<cmd>` : is a string, which corresponds to the command called in the cli.
- `<function>` : the name of the function to be called by the command, without parenthesis (we don't want to call the function in defining the command)
- `<number_of_arguments>` : an integer which specifies the number of arguments that should be passed to the called function. If we want to pass all the arguments specified after the command we set it to `-1`. When the command is called, if more arguments are given than should be passed (specified by the `nargs` parameter), miniparser will simply ignore all the additional arguments and only pass the number of arguments specified in the command definition.
- `<help_string>` : a string that is printed next to the command name when `--help` is called.

When you run your script with `<cmd>` the function `<function>` is called and the arguments specified after `<cmd>` are passed into `<function>`. The number of arguments passed to the function is defined by `<number_of_arguments>`. If `<number_of_arguments>` is set to `-1` then all the arguments that follow `<cmd>` are passed to `<function>`.

If more arguments follow `<cmd>` than is specified by `<number_of_arguments>`, then only the number of arguments specified are passed to `<function>`, the following arguments are simply ignored.

An automatic help page is generated and can be called by typing the name of your script followed by `--help`.

That's it.


## Detailed usage examples

Given a script `sum_prod.py`:
```python
# sum_prod.py

import miniparser

# We define the functions that we want to call from the command line:

# Sum of an arbitrarily long list of numbers
def sum_num(*numbers):
    nums = [int(n) for n in numbers]
    print(sum(list(nums)))

# Product of an arbitrarily long list of numbers
def product_num(*numbers):
    prod = 1
    nums = [int(n) for n in numbers]
    for n in nums:
        prod = prod*n
    print(prod)

# Prints whatever is passed into it
def echo(*args):
    print(*args)

miniparser.add_command('view', echo, nargs=-1, help="echo/print arguments")
miniparser.add_command('sum', sum_num, nargs=-1, help='returns sum of numbers')
miniparser.add_command('', product_num, nargs=2, help='returns product numbers')
miniparser.parser()
```

Then:

```bash
$ python sum_prod.py view bla bla bla
bla bla bla
```

```bash
$ python sum_prod.py sum 1 2 3 4 5
15
```

```bash
$ python sum_prod.py 2 3
6
```

```bash
$ python sum_prod.py --help
----------------
sum_prod.py help
----------------
--help      print help
view        echo/print arguments
sum         returns sum of numbers
(no cmd)    returns product numbers
```

In this example the commands print something to the screen, but the usage is of course not limited to that. You can call any defined function.

Any command defined (including the empty command, ie default behaviour if no command is passed), can take any number of argument: 0, 1, 2, etc. or all the arguments passed (in which case we specify `nargs=-1`)