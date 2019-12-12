from mpl_toolkits import mplot3d
from scipy.sparse.linalg import svds
from scipy.sparse import rand
import numpy as np
from matplotlib import pyplot

# Create sparse 3 dimensional matrix with 1random values

X = abs(rand(10000, 3, density=0.1))

# Preform truncated SVD, both GESDD and GESVD will be used to later determine which algorithm will be better for the eventual data that will be processed

U, S, V = svds(X,k=2)

singular_values = np.dot(U,np.diag(S))

#Plot singular value vectors
fig = pyplot.figure()
ax = pyplot.axes(projection='3d')
ax = pyplot.axes(projection='3d')
ax.plot3D(singular_values[:,0],singular_values[:,1], 'green')
print(singular_values)
pyplot.show()


