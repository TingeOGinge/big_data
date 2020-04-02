import matplotlib.pyplot as plt
from sklearn import datasets
#refer to https://scikit-learn.org/stable/datasets/index.html
#for more details about the most popular benchmarks for machine learning

iris = datasets.load_iris()
print(iris)
irisx = iris.data
print(irisx.shape)
irisy = iris.target
print(irisx.shape)

digits = datasets.load_digits()
print(digits)
digitsx = digits.data
print(digitsx.shape)
#1797 samples/records
#each ssample/record is an 8x8 image of digits
#the 8x8 matrix is stored as a vector
digitsy = digits.target
print(digitsy.shape)
#the label of each sample/record
plt.gray()
plt.matshow(digits.images[1796])
#The images are kept
plt.show() 