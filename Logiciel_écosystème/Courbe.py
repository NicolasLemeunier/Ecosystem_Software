import numpy as np
import matplotlib.pyplot as plt

creationTabTotal = np.array([creationTab1 , creationTab2 , creationTab3 , creationTab4])
np.sum(creationTabTotal)

fig, ax = plt.subplots(ncols=2, nrows=1, figsize=(15,5))

creationTabTotal = np.sum(creationTabTotal, axis=0)

x1 = np.array([compteur])
y1 = np.array([creationTab1])

ax[0].plot(x1, y1, "b", color= "red", label = "Tyrannosaure")

x2 = np.array([compteur])
y2 = np.array([creationTab2])

ax[0].plot(x2, y2, "b", color= "blue", label = "Triceratops")

x3 = np.array([compteur])
y3 = np.array([creationTab3])

ax[0].plot(x3, y3, "b", color= "green", label = "Allosaurus")

x4 = np.array([compteur])
y4 = np.array([creationTab4])

ax[0].plot(x4, y4, "b", color= "orange", label = "Stegosauridar")

ax[0].set_xlabel("Temps")
ax[0].set_ylabel("Nombres d'individues par espèces")

ax[0].legend()
ax[0].grid()
ax[0].yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))

x5 = np.array([compteur])
y5 = np.array([creationTabTotal])

ax[1].plot(x5, y5, "b", color= "black", label = "Total", linewidth=3)

ax[1].set_xlabel("Temps")
ax[1].set_ylabel("Nombres d'individues total")

ax[1].legend()
ax[1].grid()
ax[1].yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))

plt.title("Evolution de la population total")
plt.show()
