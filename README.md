# Hemodynamics in a Stenosed Artery

## Overview
This project simulates blood flow behavior inside a stenosed (narrowed) artery using simplified biomechanical models in Python.

The simulation investigates:
- Arterial narrowing geometry
- Blood velocity changes
- Reynolds number variation
- Wall shear stress distribution

---

## Background
Arterial stenosis reduces vessel diameter and increases blood velocity due to conservation of mass. Elevated velocity may increase wall shear stress and alter flow stability.

---

## Governing Equations

### Reynolds Number
Re = rho*U*D/mu

Where:
- rho = blood density
- U = velocity
- D = vessel diameter
- mu = dynamic viscosity

---

### Wall Shear Stress
tau = 4*mu*U/D

---

## Features
- Gaussian-shaped stenosis geometry
- Velocity profile visualization
- Reynolds number analysis
- Wall shear stress estimation
- Scientific plotting with Matplotlib

---

## Technologies Used
- Python
- NumPy
- Matplotlib

---

## Results
The simulation shows:
- Increased velocity at the stenosis region
- Elevated Reynolds number
- Increased wall shear stress near narrowing

  

```bash
pip install numpy matplotlib
python stenosis_simulation.py

  
