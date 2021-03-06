"""
Adds the source files to the path for files in any subdirectory
"""
print("Importing source context manager")

import os
import sys
file_location = os.path.dirname(os.path.abspath(__file__))
source_location = os.path.abspath(os.path.join(file_location, '..', 'source/'))

sys.path.insert(0, source_location)
