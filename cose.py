from math import cos
import matplotlib.pyplot as plt
import numpy as np

def graf_coseno(x, f, A, corr):
    cose = np.zeros(len(x))
    for i in range(0, len(x)):
        cose[i] = A * cos(f * x[i]) + corr
    fig = plt.figure()
    plt.scatter(x, cose)
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.title('A * cos(f * x) + c')
    plt.show()

x = np.linspace(0, 2 * 3.1415, 100)

graf_coseno(x, 1, 3, -1)