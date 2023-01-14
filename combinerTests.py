import unittest
import os
import pandas as pd
from io import StringIO
from contextlib import redirect_stdout

class TestMergeCSV(unittest.TestCase):
    def test_merge_csv(self):
        # Create a StringIO object to capture the output of the script
        output = StringIO()
        # Redirect stdout to the StringIO object
        with redirect_stdout(output):
            # Call the script with a list of input files
            os.system("python3 combiner.py fixtures/accessories.csv fixtures/clothing.csv fixtures/household_cleaners.csv > output.csv")

        # Read the contents of the output file into a DataFrame
        output_df = pd.read_csv("output.csv")

        # Read the expected output file into a DataFrame
        expected_output_df = pd.read_csv("expected_output.csv")

        # Check if the output DataFrame has the same columns as the expected output DataFrame
        self.assertEqual(set(output_df.columns), set(expected_output_df.columns))

if __name__ == '__main__':
    unittest.main()
