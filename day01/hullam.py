import numpy as np
import matplotlib.pyplot as plt

def wave_propagation(c, dx, dt, T, L):
    # Initialize the grid and set initial conditions
    x = np.linspace(0, L, int(L/dx)+1)
    t = np.linspace(0, T, int(T/dt)+1)
    u = np.zeros((len(x), len(t)))
    u[int(len(x)/2), 0] = 1

    # Solve the wave equation
    for n in range(len(t)-1):
        for i in range(1, len(x)-1):
            u[i, n+1] = u[i, n] - c*dt/dx * (u[i, n] - u[i-1, n])

    # Plot the wave propagation
    plt.imshow(u, origin='lower', aspect='auto', extent=[0, T, 0, L])
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title('Wave Propagation')
    plt.colorbar()
    plt.show()

# Set the wave speed, space and time steps, and total time and space
c = 0.1
dx = 0.1
dt = 0.01
T = 2
L = 1

# Call the wave_propagation function
wave_propagation(c, dx, dt, T, L)
