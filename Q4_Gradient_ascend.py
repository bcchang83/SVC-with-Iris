"""
def Jx(x, y):
    return -400*(x**3) - 400*x*(y**2) + 400*x + 1
def Jy(x, y):
    return -400*(y**3) - 400*y*(x**2) + 400*y + 1


x0=1
y0=1
lr = 0.0005
itr = 1000

x=x0
y=y0
for _ in range(itr):
    x = x + lr*Jx(x, y)
    y = y + lr*Jy(x, y)
print("Iteration={}, x={:.5}, y={:.5}".format(itr, x, y))
"""


# Increase penatly from 100 to 10000
def Jx(x, y):
    return -40000 * (x**3) - 40000 * x * (y**2) + 40000 * x + 1


def Jy(x, y):
    return -40000 * (y**3) - 40000 * y * (x**2) + 40000 * y + 1


x0 = 1
y0 = 1
lr = 0.0005
itr = 10

x = x0
y = y0
for i in range(itr):
    x = x + lr * Jx(x, y)
    y = y + lr * Jy(x, y)
    print("Iteration={}, x={:.5}, y={:.5}".format(i, x, y))
