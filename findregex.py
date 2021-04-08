#import an existing python's module for argument parser
import argparse
#import an existing python's module for regular expression
import re


#define function that print the line result
def print_line(filename, linenumber, linetoprint):
    print(linetoprint, end="")
    print(f" | line number: {linenumber} | file name: {filename} ")

#define function that colored the line result
def color_output(filename, linenumber, line, string):
    newline = line.replace(string, "\033[44;33m{}\033[m".format(string))
    print_line(filename, linenumber, newline[:-1])

#define function that print machine readable output result
def machine_output(filename, linenumber, start, string):
    print(f"{filename}:{linenumber}:{start}:{string}")

#define an argument parser and initialization (infile & regex)
def init_parser():
    parser = argparse.ArgumentParser(description="The script searches one or \
                                     more named input files for lines \
                                     containing a match to a regular \
                                     expression pattern.")
    parser.add_argument('infile', nargs='*', type=argparse.FileType('r'))
    parser.add_argument('regex')
# validate mutually_exclusive arguments (-c | -m)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--color', action='store_true')
    group.add_argument('-m', '--machine', action='store_true')

    return parser

# for loop condition to search regex pattern in files
# substring == don't stop the searching process after 1 result is found, keep searching till the end of the file.

args = init_parser().parse_args()
# enumerate loop condition
for file in args.infile:
    for i, line in enumerate(file):
# finditer== as part of RE module, Return an iterator yielding MatchObject instances over all non-overlapping matches for the RE pattern in string. The string is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result.
        substrings = re.finditer(args.regex, line)
        if substrings:
            for substring in substrings:
# if condition for chosen argument
                if args.color:
                    color_output(file.name, i + 1, line[:-1],
                                 substring.group())
                elif args.machine:
                    machine_output(file.name, i + 1, substring.start(),
                                   substring.group())
                else:
                    print_line(file.name, i + 1, line[:-1])