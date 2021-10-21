# calc.py
import argparse
import math

parser = argparse.ArgumentParser(description = "CLI Calculator.")

subparsers = parser.add_subparsers(help = "sub-command help", dest="command")

# Add
add = subparsers.add_parser("add", help = "add integers. Use as many digits as desired")
add.add_argument("ints_to_sum", nargs='*', type=int)

# Sub 
sub = subparsers.add_parser("sub", help='substaract integers.')
sub.add_argument("ints_to_sub", nargs=2, type=int)

def aec_subtract(ints_to_sub):
    our_sub = ints_to_sub[0] - ints_to_sub[1]
    if our_sub < 0:
        our_sub = 0
    print(f"The subtracted of values is  {our_sub}")
    return our_sub

# Multiplication
multiply = subparsers.add_parser("multiply", help='multiply integers. Use 4 digits')
multiply.add_argument("ints_to_multiply", nargs=4, type=int)

# Division
divide = subparsers.add_parser("divide", help='divide integers. Use 4 digits')
divide.add_argument("ints_to_divide", nargs=2, type=int)

def divide_func(ints_to_divide):
    our_division = (ints_to_divide[0] / ints_to_divide[1]) if ints_to_divide[1] != 0 else 0 
    print(f"The division of values is  {our_division}")
    return our_division

if __name__ == '__main__':
    args = parser.parse_args()

    if __name__ == "__main__":
        args = parser.parse_args()

    if args.command == "add":
        our_sum = sum(args.ints_to_sum)
        print(f"the sum of values is: {our_sum}")

    if args.command == 'sub':
        aec_subtract(args.ints_to_sub)

    if args.command == 'multiply':
        our_multiply = args.ints_to_multiply[0] * args.ints_to_multiply[1]
        print(f"The product of values is  {our_multiply}")

    if args.command == 'divide':
        divide_func(args.ints_to_divide)
    
    # if args.command == 'divide':
        # if args.ints_to_quotient[1] == 0:
        #     print("Cannot Divibe by 0")
        # else:
        #     our_quotient = math.floor(args.ints_to_quotient[0]/args.ints_to_quotient[1])
        #     our_remainder = args.ints_to_quotient[0] % args.ints_to_quotient[1]
        #     print(f"The quotient is  {our_quotient}, our remainder is {our_remainder}")