# Rotational-Volume-Visualizer

A high-performance Python engine for calculating and visualizing **Solids of Revolution** using numerical integration. This project demonstrates the bridge between **Calculus** and **Computational Geometry**.

## 🚀 Features
* **Numerical Integration:** Uses Riemann Sums ($O(n)$ complexity) to approximate volume.
* **Disk & Washer Methods:** Supports both solid and hollow rotational bodies.
* **3D Rendering:** Utilizes `NumPy` meshgrids and `Matplotlib` to transform 2D functions into 3D parametric surfaces.
* **Dynamic Input:** Evaluates string-based mathematical functions in real-time.

## 🛠️ Technical Logic
The engine transforms a 2D function $f(x)$ into a 3D coordinate system $(X, Y, Z)$ using:
- $X = x$
- $Y = f(x) \cdot \cos(\theta)$
- $Z = f(x) \cdot \sin(\theta)$

Where $\theta$ is the rotation angle $[0, 2\pi]$.

## 📦 Requirements
`pip install numpy matplotlib`# Washer-And-Disk-Method
