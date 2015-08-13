"""
Eve playground
"""

from eve import Eve

import settings

app = Eve(settings=vars(settings))
