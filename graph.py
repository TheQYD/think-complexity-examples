#!/usr/bin/python

class graph(dict):
  def __init__(self, verticies=[], edges=[]):
    for vertex in verticies:
      self.add_vertex(vertex)
    for edge in edges:
      self.add_edge(edge)
  def add_vertex(self, vertex):
    self[vertex] = {}
  def add_edge(self, edge):
    v,w = e
    self[v][w] = e
    self[w][v] = e

  def get_edge(self, vertex1, vertex2, graph):
    edges = None
    for vertex_one in graph:
      if vertex_one.label == vertex1:
        graph_inner = graph[vertex_one]
        for vertex_two in graph_inner:
          if vertex_two.label == vertex2:
            graph_value = graph_inner[vertex_two]
    return edges

class vertex(object):
  def __init__(self, label=''):
    self.label = label
  def __repr__(self):
    return 'vertex(%s)' % repr(self.label)

  __str__ = __repr__

class edge(tuple):
  def __new__(cls, edge1, edge2):
    return tuple.__new__(cls, (edge1, edge2))

  def __repr__(self):
    return 'edge(%s, %s)' % (repr(self[0]), repr(self[1]))
  __str__ = __repr__

if __name__ == '__main__':
  v = vertex('v')
  w = vertex('w')
  e = edge(v,w)
  g = graph([v,w], [e])
  print g.get_edge('v','w',g)
