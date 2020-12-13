from six import StringIO

import pandas as pd
import numpy as np
import graphviz
from IPython.display import Image
from sklearn import tree
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from pandas import Series, DataFrame

# Put xlsx file in folder ./
InputData = pd.read_excel("./Preliminary Data Analysis.xlsx"
                      ,"Input Data")

OutputData = pd.read_excel("./Preliminary Data Analysis.xlsx"
                      ,"Output Data")

Sustainability = {'N':'0','Y':'1'}
#利用匿名函数进行依次更改
InputData['Sustainability']=InputData['Sustainability'].apply(lambda x:Sustainability[x])

RDCapability = {'Low':'0','High':'1'}
#利用匿名函数进行依次更改
InputData['RDCapability']=InputData['RDCapability'].apply(lambda x:RDCapability[x])

dist_dict = {'中型企业':'1','大型企业':'2','小型企业':'0'}
#利用匿名函数进行依次更改
InputData['CompanySize']=InputData['CompanySize'].apply(lambda x:dist_dict[x])

ReputationNegative = {'N':'0','Y':'1'}
#利用匿名函数进行依次更改
InputData['ReputationNegative']=InputData['ReputationNegative'].apply(lambda x:ReputationNegative[x])


Xtrain, Xtest, Ytrain, Ytest = train_test_split(InputData, OutputData, test_size = 0.3)
clf = tree.DecisionTreeClassifier(criterion = "entropy"
                          ,random_state = 30
                          ,splitter = "random"
                          ,min_samples_leaf=5
                          )

clf = clf.fit(Xtrain, Ytrain)
result = clf.score(Xtest, Ytest)

print (result)

import pydotplus

dot_data=StringIO()
#
# tree.export_graphviz(clf,out_file=dot_data,filled=True, rounded=True, special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf("wine.pdf")


attribute_name = ["Company Size", "Reputation Negative", "Reputation Positive", "RD Capability", "Development Strategy Direction", "Sustainability"]
tree.export_graphviz(clf,out_file=dot_data,feature_names = attribute_name,class_names = ["Recommend", "Depends"],filled = True,rounded = True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("stock-entropy.pdf")

# tree.export_graphviz(clf,out_file=dot_data,filled=True, rounded=True, special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
#
# Image(graph.create_png())
#*zip(attribute_name, clf.feature_importances_)