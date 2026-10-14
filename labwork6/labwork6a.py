import math
import matplotlib
import matplotlib.pyplot as pl
x = []
y = []
for i in range(-5, 6):
    x.append(i)
    y.append(2*i + math.sin(i)**2 + 3)
    # y.append(2*i + math.sin(math.radians(i))**2 + 3)
    
pl.plot(x, y)
pl.title("hello, po!")
pl.xlabel("x")
pl.ylabel("y = 2x + sin^2(x) + 3")
pl.savefig("po.pdf")
