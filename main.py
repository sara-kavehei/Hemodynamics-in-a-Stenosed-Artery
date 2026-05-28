# Hemodynamics in a Stenosed Artery
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# artery length
x = np.linspace(0, 10, 200)

# stenosis geometry
radius = 1 - 0.5 * np.exp(-((x - 5)**2) / 1.5)

# simplified velocity
velocity = 1 / radius

# blood properties
rho = 1060      # kg/m^3
mu = 0.004      # Pa.s
D = 2 * radius * 0.003

# Reynolds number
Re = rho * velocity * D / mu

# Wall shear stress
tau = 4 * mu * velocity / D

# =========================
# PLOTS
# =========================

plt.figure(figsize=(10,5))
plt.plot(x, radius, linewidth=3)
plt.title("Artery Radius Along Length")
plt.xlabel("Length of Artery")
plt.ylabel("Normalized Radius")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,5))
plt.plot(x, velocity, color='r', linewidth=3)
plt.title("Blood Velocity in Stenosed Artery")
plt.xlabel("Length of Artery")
plt.ylabel("Velocity")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,5))
plt.plot(x, Re, color='g', linewidth=3)
plt.title("Reynolds Number Along Artery")
plt.xlabel("Length of Artery")
plt.ylabel("Re")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,5))
plt.plot(x, tau, color='purple', linewidth=3)
plt.title("Wall Shear Stress")
plt.xlabel("Length of Artery")
plt.ylabel("Shear Stress (Pa)")
plt.grid(True)
plt.show()
