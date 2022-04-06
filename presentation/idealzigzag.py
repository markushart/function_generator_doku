import numpy as np

f = 100e3

if f == 100e3: # 100 khz
	Ul, Uh, T, T0 = 0.0, 3.3, 1e-5, -95e-7
	nump = 30
elif f == 350e3: # 350khz
	Ul, Uh, T, T0 = 0.0, 3.3, 3.4e-6, -1e-5
	nump = 30

p=np.array([[i*T/2 + T0, Ul * (i%2) + Uh * ((i+1)%2)] for i in range(nump)])

np.savetxt(f"idealzigzag{int(f/1e3)}.csv", p, fmt="%.10f", delimiter=',', header="x, y", comments="")


