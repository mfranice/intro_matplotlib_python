# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Alumnos: Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Graficar la función utilizando "scatter"
    # utilizando "x" e "y"
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(x,y, marker='.', label='y=tanh(x)')

    # Colocar la leyenda y el label con el nombre de la función

    fig.suptitle('Gráfico de función y=tanh(x) con scatter')

    # Elegir un marker a elección

    # Crear acá su gráfico

    plt.show()
    print("terminamos")