"""
Nose tests.

Test five routes with strange edge case controle points against values from:
https://rusa.org/octime_acp.html
"""

import nose
import logging

from acp_times import *

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)
