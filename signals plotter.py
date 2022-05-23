from scipy.interpolate import make_interp_spline, BSpline

T = [12, 10, 2, 3]
power = [2, 15, -2, 8]

# 300 represents number of points to make between T.min and T.max
xnew = np.linspace(T.min(), T.max(), 300) 

spl = make_interp_spline(T, power, k=3)  # type: BSpline
power_smooth = spl(xnew)

plt.plot(xnew, power_smooth)
plt.show()