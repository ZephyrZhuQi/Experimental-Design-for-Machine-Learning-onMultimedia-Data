import matplotlib.pyplot as plt
from math import log
import numpy as np

x = [37761034, 148234, 33162, 9418]
x = reversed(x)
x = [log(i) for i in x]
x = np.array(x)
y = [86.9, 86.7, 85.67, 10]
# y = reversed(y)
# y = np.array(y)
y2 = [85.7, 85.48, 84.58, 10]


from scipy.interpolate import make_interp_spline
X_Y_Spline = make_interp_spline(x, y)
X_Y2_Spline = make_interp_spline(x, y2)
# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)
Y2_ = X_Y2_Spline(X_)
Y_ = reversed(Y_)
Y_ = [i for i in Y_]
Y2_ = reversed(Y2_)
Y2_ = [i for i in Y2_]

fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(8)
# ax.plot(x,y)
# ax.plot(x,y2)
ax.plot(X_,Y_, label="Train Accuracy")
ax.plot(X_,Y2_, label="Val Accuracy")
ax.set_xlim(19, 8) 
plt.xlabel("Log MEC (bits)")
plt.ylabel("Accuracy (%)")
plt.legend()
plt.savefig("/content/drive/MyDrive/Colab Notebooks/mec_acc.jpg")
plt.show()