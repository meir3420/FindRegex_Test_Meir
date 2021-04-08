import unittest
import subprocess


class Unit_Tests(unittest.TestCase):
    def test_error_if_no_regex_exist(self):
        output = subprocess.run(['python', 'findregex.py', '-c'], capture_output=True)
        is_expected_error = "error: the following arguments are required: regex" in str(output.stderr)
        self.assertEqual(is_expected_error, True)

    def test_check_error_if_invalid_arg(self):
        output = subprocess.run(['python', 'findregex.py', '-a','files_for_unittest/first.txt', 'files_for_unittest/second.txt', '[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]'], capture_output=True)
        is_expected_error = "error: unrecognized arguments: -a" in str(output.stderr)
        self.assertEqual(is_expected_error, True)

    def test_check_if_invalid_file_path(self):
        output = subprocess.run(['python', 'findregex.py', '-c','m:\\', '[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]$'], capture_output=True)
        is_expected_error = "error: argument infile: can't open" in str(output.stderr)
        self.assertEqual(is_expected_error, True)

    def test_check_if_valid_arg_valid_file_path_valid_regex(self):
        output = subprocess.run(['python', 'findregex.py', '-c','files_for_unittest/first.txt', 'files_for_unittest/second.txt', '[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]'], capture_output=True)
        lines_count = str(output.stdout).count('line number')
        self.assertEqual(lines_count, 14)

if __name__ == '__main__':
    unittest.main()