import matplotlib.pyplot as plt
import numpy as np

# input
original=input("enter exp: ")
range_u=int(input("enter upper limit: "))
range_l=int(input("enter lower limit: "))
# ##########################
exp=original.replace("exp","np.exp")
exp=exp.replace(".*","*")
exp=exp.replace("sqrt","np.sqrt")
exp=exp.replace("sin","np.sin")
exp=exp.replace("cos","np.cos")
exp=str(exp)
# ##########################

x = np.linspace(range_l,range_u,(100*(abs(range_u)+abs(range_l))))
y =eval(exp)

plt.plot(x,y)

plt.title(original)
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()