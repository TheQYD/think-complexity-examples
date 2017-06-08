#!/usr/bin/python

import sys
import uuid

def new_file(file_content):
  filename = str(uuid.uuid4()) + ".txt"
  file_object = open(filename, 'w')
  file_object.write(file_content)

if __name__ == "__main__":
  file_content = sys.argv[1]
  new_file(file_content)
