import ctypes
import sys
from ctypes import *
import os

_load_lib = ctypes.cdll.LoadLibrary(sys.argv[2] + "/libdigitalcontent.so")
try:
    foo = sys.argv[1]
    foo2 = sys.argv[2]
except:
    print("Wrong params")
else:
    _load_lib.setTime(int(sys.argv[1]))
