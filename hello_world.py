#!/usr/bin/python3

import sys


def hello_world(name):
  print("Hello " + name)

argname = 'World'

if len(sys.argv) > 1:
    argname = sys.argv[1]

hello_world(argname)

