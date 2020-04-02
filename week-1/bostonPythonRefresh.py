from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


boston = load_boston()
x = boston.data
y = boston.target
print(x.shape) 
print(y.shape)
print(boston.DESCR)
print(type(boston))
plt.hist(y, bins=30, color='b', normed=True)

#convert to pandas dataframe
df = pd.DataFrame(x,columns=boston.feature_names)
df['MEDV'] = pd.Series(y)
print(df)

g = sns.PairGrid(df,size=1)
g.map(plt.scatter)
plt.show()

fig=plt.figure(figsize=(12,12))
sns.heatmap(df.corr(),vmax=1,square=True,annot=True)

#sklearn model training and testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(pd.DataFrame(x,columns=boston.feature_names),pd.Series(y),test_size=0.1,random_state=1)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn import linear_model
from sklearn import svm
from sklearn.metrics import mean_squared_error, r2_score

#linear regression model
linear_reg = linear_model.LinearRegression()
linear_reg.fit(x_train,y_train)
print(linear_reg.coef_)
linear_reg_predict = linear_reg.predict(x_test)
print('The mean squared error and r^2 values for the linear regression prediction is')
print(mean_squared_error(y_test, linear_reg_predict))
print(r2_score(y_test, linear_reg_predict))

#ridge regression model
ridge_reg = linear_model.Ridge(alpha=1)
ridge_reg.fit(x_train,y_train)
print(ridge_reg.coef_)
ridge_reg_predict = ridge_reg.predict(x_test)
print('The mean squared error and r^2 values for the ridge regression prediction is')
print(mean_squared_error(y_test, ridge_reg_predict))
print(r2_score(y_test, ridge_reg_predict))

#support vector regression
svr = svm.SVR()
svr.fit(x_train,y_train)
svr_predict = svr.predict(x_test)
print('The mean squared error and r^2 values for the support vector regression prediction is')
print(mean_squared_error(y_test, svr_predict))
print(r2_score(y_test, svr_predict))

#support vector regression with RBF kernel
svr_rbf = svm.SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_rbf.fit(x_train,y_train)
svr_rbf_predict = svr_rbf.predict(x_test)
print('The mean squared error and r^2 values for the support vector regression with RBF kernel prediction is')
print(mean_squared_error(y_test, svr_rbf_predict))
print(r2_score(y_test, svr_rbf_predict))

#support vector regression with linear kernel
svr_linear = svm.SVR(kernel='linear')
svr_linear.fit(x_train,y_train)
svr_linear_predict = svr_linear.predict(x_test)
print('The mean squared error and r^2 values for the support vector regression with linear kernel prediction is')
print(mean_squared_error(y_test, svr_linear_predict))
print(r2_score(y_test, svr_linear_predict))