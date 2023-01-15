# PMG-CSV-Combiner
PMG Programming Challenge Solution
A solution to PMG's csv-combiner challenge. a command line program that takes several CSV files as arguments. Each CSV file (found in the fixtures directory of this repo) will have the same columns. The script outputs a new CSV file to stdout that contains the rows from each of the inputs along with an additional column that has the filename from which the row came (only the file's basename, not the entire path). The script uses 'filename' as the header for the additional column.

Language and Third-party Library
Python 3.10.9
pandas


combiner.py Usage
Through command line:
$ python3 combiner.py fixtures/accessories.csv fixtures/clothing.csv > new.csv

combinerTests.py Usage
Through command line:
$ python3 combinerTests.py