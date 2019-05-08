# Copyright (c) 2018-2019 by Srinivas Garlapati

import sys
from contextlib import contextmanager
 
 
@contextmanager
def write_to_file(fileobj):
    old = sys.stdout
    sys.stdout = fileobj
    try:
        yield fileobj
    finally:
        sys.stdout = old
