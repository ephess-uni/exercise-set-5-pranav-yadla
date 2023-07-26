"""ex_5_1.py"""
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count

import  argparse


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    parser = argparse.ArgumentParser(description="to input the file")
    parser.add_argument('file_name',help="input file name",type=str,nargs='?')
    args = parser.parse_args()
    print(args.file_name)
    main(args.file_name) if args.file_name else print('run with arguments to get output')