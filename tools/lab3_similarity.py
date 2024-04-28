import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[0])
                )  # can import files based on the parents path

import Levenshtein as lev

from isub import isub
#https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a
#https://github.com/J535D165/FEBRL-fork-v0.4.2/blob/master/stringcmp.py

#Different lexical similarity methods
print(lev.distance('Congo', 'Republic of Congo'))
print(lev.jaro_winkler('Congo', 'Republic of Congo'))
print(lev.jaro_winkler('Congo', 'Congo Republic'))
print(isub('Congo', 'Republic of Congo'))
print(isub('Congo', 'Congo Republic'))
print()
print(isub('Congo', 'aaaaaaa'))
print(isub('Congo', 'Congo'))
print(isub('asfasdf', 'ertetet'))
print(lev.jaro_winkler('Congo', 'Congo'))
print(lev.jaro_winkler('Congo', 'aaaaaaa'))
