import math
import matplotlib
import matplotlib.pyplot as pl
x = []
y = []
for i in range(-5, 6):
    for j in range(0, 10):
        x1 = i + j/10
        x.append(x1)
        y.append(2*x1 + math.sin(x1)**2 + 3)
        # y.append(2*i + math.sin(math.radians(i))**2 + 3)
    
pl.plot(x, y)
pl.title("hello, po!")
pl.xlabel("x")
pl.ylabel("y = 2x + sin^2(x) + 3")
pl.savefig("po.pdf")
