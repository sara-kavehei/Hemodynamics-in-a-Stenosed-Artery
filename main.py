# Hemodynamics in a Stenosed Artery
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# artery length
x = np.linspace(0, 10, 200)

# healthy artery radius
r0 = 0.003

# stenosis geometry
radius = r0 * (1 - 0.5 * np.exp(-((x - 5)**2) / 1.5))

# diameter
D = 2 * radius

# continuity equation
Q = 1e-5
velocity = Q / (np.pi * radius**2)


# blood properties
rho = 1060      # kg/m^3
mu = 0.004      # Pa.s

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
