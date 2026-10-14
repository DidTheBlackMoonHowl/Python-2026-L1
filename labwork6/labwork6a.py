import math
import matplotlib.pyplot as pl
x = []
y = []
for i in range(-5, 5):
    for j in range(0, 11):
        x.append(i + j/10)  # -5 and 5 already included
        y.append(2*(i + j/10) + math.sin(i + j/10)**2 + 3)
    
pl.plot(x, y)
pl.title("hello, po!")
pl.xlabel("x")
pl.ylabel("y = 2x + sin^2(x) + 3")
pl.grid(True)
pl.savefig("po.pdf")
