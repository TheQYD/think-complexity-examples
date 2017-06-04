#!/usr/bin/python

import Cdf
import matplotlib.pyplot as pyplot

cdf = Cdf.MakeCdfFromList([1,2,2,4,5])
prob = cdf.Prob(2)
value = cdf.Value(0.5)
xs, ps = cdf.Render()

for x, p in zip(xs, ps):
    print x, p
