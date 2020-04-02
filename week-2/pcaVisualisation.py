import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn import datasets
import numpy as np
#refer to https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
#for more details about principal component analysis

iris = datasets.load_iris()
x=iris.data
pca = PCA().fit_transform(x)
#PCA
y = iris.target

fig = plt.figure()
plt.scatter(x[:,0],x[:,1], c=y, edgecolor='r')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Without PCA')
plt.colorbar()
plt.show()

fig = plt.figure()
plt.scatter(pca[:,0],pca[:,1], c=y, edgecolor='r')
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.title('First 2 PCs')
plt.colorbar()
plt.show()
#2-dimensional

fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(pca[:,0], pca[:,1], pca[:,2], c=y, cmap=plt.cm.Set1, edgecolor='b', s=40)
ax.set_title('First 3 PCs')
ax.set_xlabel('PC 1')
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel('PC 2')
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel('PC 3')
ax.w_zaxis.set_ticklabels([])
#3-dimensional 

fig = plt.figure()
plt.plot(np.cumsum(PCA().fit(x).explained_variance_ratio_))
plt.xlabel('No. of PCs')
plt.ylabel('Explained variance ratio')
plt.show()
#from 0% to 100% reflection of the variance