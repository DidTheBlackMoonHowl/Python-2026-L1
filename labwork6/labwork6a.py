import math
import matplotlib.pyplot as pl
x = [(v + v1/10) for v in range(-5, 5) for v1 in range(0, 11)]
y = [(2*v + math.sin(v)**2 + 3) for v in x]

pl.plot(x, y)
pl.title("hello, po!")
pl.xlabel("x")
pl.ylabel("y = 2x + sin^2(x) + 3")
pl.grid(True)
#pl.show()
pl.savefig("po.pdf")
