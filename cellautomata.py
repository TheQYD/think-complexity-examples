#!/usr/bin/python

import numpy

class CA(object):

  def __init__(self, rule, n=100, ratio=2):
    self.table = make_table(rule)
    self.n = n
    self.m = ratio*n + 1
    self.array = numpy.zeros((n, self.m), dtype=numpy.int8)
    self.next = 0

  def step(self):
    i = self.next
    self.next += 1

    a = self.array
    t = self.table
    for j in xrange(1,self.m-1):
      a[i,j] = t[tuple(a[i-1, j-1:j+2])]

class CADrawer(object):

  def __init__(self):
    msg = 'Abstract type  should not be instantiated.'
    raise UnimplementedMethodException, msg

  def draw(self, ca):
    raise UnimplementedMethodException

  def draw_arry(self, a):
    for i in xrange(self.rows):
      for j in xrange(self.cols):
        if a[i,j]:
          self.draw_cell(j, self.rows-i-1)

  def draw_cell(self, ca):
    raise UnimplementedMethodException

  def show(self):
    raise UnimplementedMethodException

  def save(self, filename):
    raise UnimplementedMethodException


