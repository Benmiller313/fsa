import sys, getopt

from finite_state_machine.division_machine import DivisionMachine

def main(argv):
    help_string = 'divide_by_three.py <input>'
    try:
        _, args = getopt.getopt(argv, "")
    except getopt.GetoptError:
        print(help_string)
        sys.exit(1)

    if not args or len(args) > 1:
        print(help_string)
        sys.exit(1)

    try:
        print(DivisionMachine().evaluate(args[0]))
        sys.exit(0)
    except ValueError as e:
        print(e)
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])

