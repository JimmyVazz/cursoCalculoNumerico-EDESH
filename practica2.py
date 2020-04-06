import numpy as np
import matplotlib.pylab as plt
 
x = np.linspace(-1, 1, 50)
y1 = 2*x
y2 = 2*(x)**2 + 1
y3 = 2*(x)**3 - 2
 
plt.figure(num='MiPrimerGrafico')
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xlabel('Abcisas')
plt.ylabel('Ordenadas')
plt.title('Mi primera figura')
plt.show()
