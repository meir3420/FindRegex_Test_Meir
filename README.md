# FindRegex_Test_Meir


Env Details:

Windows 10 64 bit
PyCharm - 2021.1
Docker Desktop for windows - 3.2.2 (Dockerfile - Windows OS oriented)
Testing automation framework - Pytest in Pycharm




The script searches one or more named input files for lines containing a match to a regular expression pattern. If a line matches, it is printed alongside the file name and the line number for every match.
Usage:
findregex.py [-c | -m] [infile [infile ...]] regex
Positional arguments:
infile - the name of the file(s) to search.
regex - the regular expression.


Optional arguments:
-c, --color - highlights matching text.
-m, --machine - generates machine readable output. (Format: file_name:no_line:start_pos:matched_text)
Example
-c first.txt second.txt [a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]
Searches for the regular expression (example result is: aBCDaAAAa) in the lines of the first.txt and second.txt files. 
The output will be the matching text highlighted.
