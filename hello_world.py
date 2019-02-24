#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    name = sys.argv[1]
else:
    name = 'World'

def hello_world(name):
  print("Hello" + name)

hello_world()

