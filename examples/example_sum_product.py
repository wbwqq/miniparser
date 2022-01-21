import miniparser

# We define the functions that we want to call from the command line:

# Sum of an arbitrarily long list of numbers
def sum_num(*numbers):
    nums = [int(n) for n in numbers]
    print(sum(nums))

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
miniparser.add_command('sum3', sum_num, nargs=3, help='returns sum of the first three numbers')
miniparser.add_command('prod', product_num, nargs=-1, help='returns product of numbers')
miniparser.add_command('prod3', product_num, nargs=3, help='returns product of the first three numbers')
miniparser.add_command('', product_num, nargs=2, help='returns product numbers')
miniparser.parser()