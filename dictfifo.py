#!/usr/bin/python

class dictfifo(object):
  def __init__(self):
    self.nextin = 0
    self.nextout = 0
    self.data = {}

  def append(self, value):
    self.data[self.nextin] = value
    self.nextin += 1

  def pop(self, n=1):
    value = self.data.pop(self.nextout)
    self.nextout += 1
    return value

def bfs(top_node, visit):
  visited = set()
  queue = [top_node]
  while len(queue):
    curr_node = queue.pop(0)
    visit(curr_node)
    visited.add(curr_node)

    queue.extend(c for c in  curr_node.children if c not in visited and c not in queue)


if __name__ == '__main__':
  dictfifo = dictfifo()
  dictfifo.append(17)


