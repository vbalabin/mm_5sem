from math import *
 
def f1(x, y1, y2):
    return (x**2 + y1**2) / y2**2
def f2(x, y1, y2):
    return x + y1 + y2
 
class CF:
    def __init__(self, n ,f):
        self.n, self.f = n, f
    def step(self, x, h, y1, y2):
        y[self.n] += h * self.f(x, y1, y2)
"string"
a = 0
b = 1
n = 100.0 
h = (b-a)/n
x = a
l = 4
y = [0.0,0.0]
F = [f1,f2]
Y = []

for i in range(l): 
    Y += [CF(i, F[i])]
while x <= b:
    for i in Y: 
        i.step(x, h, y[0], y[1])
    x += h
    print (x, y[0], y[1])
