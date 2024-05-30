"""
https://stackoverflow.com/questions/73381902/running-unittest-with-modules-that-must-import-other-modules
"""

import sys

import project.utils as utils
sys.modules['utils'] = utils
