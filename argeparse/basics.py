import argparse

parser = argparse.ArgumentParser()
# This is a positional argument that we have to add after the file name
# i.e., python basic.py echo_fun(or whatever here)
# parser.add_argument("echo", help="echo the string you use here")

# By default it treats the options we give it as strings
# parser.add_argument("square", help="computer the square of the given number",
#                     type=int)
# args = parser.parse_args()
# print(args.square ** 2)

# This is a optional argument :).
# when using --verbosity, one must also specify some value, any value
# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")


# Now it's like a flag, if we specify it, it will store true else false
# as action = "store_true", now we don't have to specify any value after this.
# parser.add_argument("-v", "--verbosity", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")



# parser = argparse.ArgumentParser()
# parser.add_argument("-s", "--square", type=int,
#                     help="display a square of a given number")
# this is a positional arg the down one, bcause of not added - or --
# you can only add -s, and --square, you can't do -s, -square. :(.
# and same goes for the verbose one.
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print(f"the square of {args.square} equals {answer}")
# else:
#     print(answer)
# Now the order does not matter i.e., 
# python basics.py -v 4 is same as ..... 4 -v





# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)




# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", action="count", default=0,
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity >= 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity >= 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)


# More at here -> https://docs.python.org/3/howto/argparse.html#argparse-tutorial

# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()

# it means we can only specify one either -v or -q
# group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")

print(argparse.__file__)
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count', required=False)
args = parser.parse_args()
print(args.count)