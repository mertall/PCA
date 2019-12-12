import scipy as sp
import numpy as np
import matplotlib as mpl
def data():

# Create sparse 3 dimensional matrix with 1random values, random state has been fixed to ensure the results are replicable

    X = sp.sparse.random(500,3,density=0.01,random_state=42)

#Store dimensions of matrix

    m, n = X.np.matrix.shape()

    return X,m,n

def SVD(X,lapack_setting,truncated,singular):

# Preform SVD, both GESDD and GESVD will be used to later determine which algorithm will be better for the eventual data that will be processed

    if truncated == 0 :

        if lapack_setting == 'gesdd' :

            U, S, V = sp.linalg.svd(X,lapack_driver=gesdd)

        else :

            U, S, GV = sp.linalg.svd(X, lapack_driver=gesvd)

    else:

        if singular == 'largest':

            U, S, V = sp.sparse.linalg.svds(X,which=LM)

        else :

            U, S, V = sp.sparse.linalg.svds(X,which=SM)
    return U, S, V

def main():

    X,m,n=data()

    lapack_setting=input('Type "gesdd" to use gsdd algorithm for SVD, otherwise type any character in order to use gesvd algorithm')
    truncated=input('Type "0" if full matrix calcuation is requied, otherwise type another character in order to find truncated SVD')
    singular=input('Type "largest" if you want to find largest singular values otherwise type any charcter in order to find smallest singular values')

    U,S,V=SVD(X,lapack_setting,truncated,singular)

    singular_values = np.dot(U,np.diag(S))

    fig = mpl.pyplot.figure()
    ax = mpl.pyplot.axes(projection='3d')
    ax.plot3D(singular_values[:,1],singular_values[:,2],singular_values[:,3])
    ax.scatter3D(X[:,1],X[:,2],X[:,3])

if __name__ == '__main__':
    main()



