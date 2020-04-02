import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model

anscombe = sns.load_dataset("anscombe")
print(anscombe)

# create subsets and subplots of the anscombe data
dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2= anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

#linear regression model
regr = linear_model.LinearRegression()
regr.fit(dataset_1['x'].values.reshape(-1,1), dataset_1['y'].values.reshape(-1,1))
axes1.plot(dataset_1['x'].values.reshape(-1,1), regr.predict(dataset_1['x'].values.reshape(-1,1)), 'r')
#only give 1 subplot fitting results

print(anscombe.groupby("dataset").describe())