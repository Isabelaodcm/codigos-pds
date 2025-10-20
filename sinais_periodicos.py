# frequencia de 0 a pi - sinal oscila mais rapido
# frequencia de pi a 2pi - sinal vai oscilando mais devagar
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-25, 25)

def f(x):
    return np.cos(x)

f1 = f(0*n) # omega0 = 0 ou 2pi
f2 = f(n*np.pi/8) # omega0 = pi/8 ou 15pi/8
f3 = f(n*np.pi/4)
f4 = f(n*np.pi)
f5 = f(n*2*np.pi)
f6 = f(n*15*np.pi/8)
f7 = f(n*7*np.pi/4)

fig, ax = plt.subplots(4, 2)
ax[0,0].stem(n, f1, linefmt="blue", label = r"$\omega_0 = 0$")
ax[1,0].stem(n, f2, linefmt="blue", label = r"$\omega_0 = \pi/8$")
ax[2,0].stem(n, f3, linefmt="blue", label = r"$\omega0 = \pi/4")
ax[3,0].stem(n, f4, linefmt="blue", label = r"$\omega0 = \pi")

ax[0,1].stem(n, f4, linefmt="red", label = r"$\omega0 = \pi$")
ax[1,1].stem(n, f5, linefmt="red", label = r"$\omega_0 = 2\pi$")
ax[2,1].stem(n, f6, linefmt="red", label = r"$\omega_0 = 15\pi/8$")
ax[3,1].stem(n, f7, linefmt="red", label = r"$\omega_0 = 7\pi/4$")

# plt.stem(n, f1)
for linha in ax:
    for a in linha:
        a.legend()

plt.tight_layout()
plt.show()
