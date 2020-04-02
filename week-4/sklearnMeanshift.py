import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.cluster import MeanShift as ms

def confusionM(y_true,y_predict,target_names):
#function for visualisation
    cMatrix = confusion_matrix(y_true,y_predict)
    df_cm = pd.DataFrame(cMatrix,index=target_names,columns=target_names)
    plt.figure(figsize = (6,4))
    cm = sns.heatmap(df_cm,annot=True,fmt="d")
    cm.yaxis.set_ticklabels(cm.yaxis.get_ticklabels(),rotation=90)
    cm.xaxis.set_ticklabels(cm.xaxis.get_ticklabels(),rotation=0)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def convertCluster2Label(cluster_labels,original_labels,labels2convert):
    #both input arguments have the same dimensionality, the original labels are the labels in training set
    #cluster_labels are labels of clusters after clustering process
    #labels2convert are the predicted labels based on the clustering model
    #we need to convert them into the settings to comply with the original labels' definition
    converted_labels =np.full(labels2convert.size, -1)
    #converted_labels =np.full(labels2convert.size, np.nan) will generate float
    for i in np.unique(cluster_labels):
        temp_original_labels = original_labels[cluster_labels==i]
        temp_label = np.bincount(temp_original_labels).argmax()
        converted_labels[labels2convert==i] = temp_label
    return converted_labels
        

iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names
X_train, X_test, y_train, y_true = train_test_split(X, y)
meanshift = ms(bandwidth=10)
meanshift = ms(bandwidth=2)
meanshift = ms(bandwidth=1)
meanshift = ms(bandwidth=0.5)
meanshift = ms(bandwidth=0.1)
#change the bandwith to see the difference

meanshift.fit(X_train)
values = meanshift.cluster_centers_.squeeze()
trained_labels = meanshift.labels_
#labels' definitions are different from the Y_train, you have to convert them into the same
labels_predict = meanshift.predict(X_test)
print(labels_predict)
#labels_predict' definitions are different from the Y_test too, you have to convert them into the same
y_predict = convertCluster2Label(trained_labels,y_train,labels_predict)
print(y_predict)

confusionM(y_true,y_predict,target_names)