from sys import maxsize

POINTER_SIZE = 8 if maxsize > 2**32 else 4
