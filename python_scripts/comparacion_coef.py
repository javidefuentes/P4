import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Abrimos y cargamos los ficheros
lp_filename = 'lp_2_3.txt'
lpcc_filename = 'lpcc_2_3.txt'
mfcc_filename = 'mfcc_2_3.txt'
lp = np.loadtxt(lp_filename, delimiter='\t', skiprows=0,)
lpcc = np.loadtxt(lpcc_filename, delimiter='\t', skiprows=0,)
mfcc = np.loadtxt(mfcc_filename, delimiter='\t', skiprows=0,)

# Mostrar los coeficientes LPC
plt.plot(lp[:,0], lp[:,1],'.c')
plt.xlabel("Coeficiente 2", fontsize=10)
plt.ylabel("Coeficiente 3", fontsize=10)
plt.title("LPC", fontsize=14)
plt.show()

# Mostrar los coeficientes LPCC
plt.plot(lpcc[:,0], lpcc[:,1],'c.')
plt.xlabel("Coeficiente 2", fontsize=10)
plt.ylabel("Coeficiente 3", fontsize=10)
plt.title("LPCC", fontsize=14)
plt.show()

# Mostrar los coeficientes MFCC
plt.plot(mfcc[:,0], mfcc[:,1],'c.')
plt.xlabel("Coeficiente 2", fontsize=10)
plt.ylabel("Coeficiente 3", fontsize=10)
plt.title("MFCC", fontsize=14)
plt.show()