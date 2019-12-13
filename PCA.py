from mpl_toolkits import mplot3d
from scipy.sparse.linalg import svds
from scipy.sparse import rand, coo_matrix
import numpy as np
from matplotlib import pyplot

# Create sparse 3 dimensional matrix with random values

def data(m,n):

    X = abs(rand(m, n, density=0.1,dtype=float))

    k = min(X.shape) - 1

    return X ,k

# Preform truncated SVD

def svd(X,k):

    U, S, V = svds(X,k=k)

    singular_values = np.dot(U,np.diag(S))

    return singular_values

#Plot singular value vectors

def graph(X,singular_values):

    fig = pyplot.figure()

    ax = pyplot.axes(projection='3d')

    ax = pyplot.axes(projection='3d')

    ax.plot3D(singular_values[:,0],singular_values[:,1], 'green')

    print(singular_values)

    pyplot.show()

def main():

    m = int(input('Choose the number of rows in your sparse random matrix:\n'))

    print('For now there is only 3 dimensional capability, in the future there will be added functionality for higher dimensions.')

    X,k = data(m,3)

    print(X,"\n This is your sparse random matrix")

    singular_values = svd(X,k)

    print('Now a graph will be displayed with your singular vectors plotted along with the singular value matrix')

    graph(X,singular_values)

if __name__ == '__main__':
    main()

