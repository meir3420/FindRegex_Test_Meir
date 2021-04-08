import argparse
import re
import os
import os.path

# Define the files_path that you want to search for text files and results
files_path = input("1. Insert a valid files path:\nex: C:\\Users\\meir3\\Desktop:\nex: C:\\\n")
isExist = os.path.exists(files_path)
print(f"Chosen files path is: " + files_path)
print(isExist)

if isExist == True:
    print("Path exists")
    for file in os.listdir(files_path):
        if file.endswith(".txt"):
            print(os.path.join(files_path, file))
else:
    print("Invalid Path, No results")
# I need to learn how to return to start, if invalid
print("\n")

#describes the valid\invalid arguments
print(f"2. script accepts mutually exclusive parameters as an arguments.\n-c ( --color ) which highlight matching text\n-m ( --machine ) which generate machine-readable output ")
valid_inputs = ["-c","-m"]
inp = input()
if inp not in valid_inputs:
        print("Invalid argument, try again")
# I need to learn how to return to start, if invalid
else:
        print("chosen argument is: " + inp)
print("\n")


regex = input("insert a valid regex to find:\nex: [a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]\nex: ^A\n")
print(f"chosen regex: " + regex)

# I need to learn & add IsRegexValid function

#import re
#try:
#    re.compile('[')
#   is_valid = True
#except re.error:
#    is_valid = False
