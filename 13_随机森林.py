# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:36:08 2019

@author: Administrator
"""
from sklearn.ensemble import RandomForestClassifier



# To support both python 2 and python 3
from sklearn.metrics import classification_report
# Common imports
import numpy as np
import pandas as pd

# to make this notebook's output stable across runs
np.random.seed(42)

####加载数据集
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
#鸢尾花数据集
iris = load_iris()
X = iris.data[:, 2:] # petal length and width
y = iris.target

#重复缺陷报告数据集
##直接用pands的csv方式读取有问题
#data=pd.read_csv('G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random.scaled.csv')
#print (data.shape)
import csv
import numpy as np
###处理CSV数据获取特征值和标签值
def processCSVForGetFeatureAndTagValues(csv_file_path,feature_dimensions):#第二个参数是特征维数
	with open(csv_file_path,'r') as csvfile:
#with open('G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random.scaled.csv','r') as csvfile:
		reader = csv.reader(csvfile)
		rows= [row for row in reader]
		#print (rows)#输出所有数据
		data=np.array(rows)#rows是数据类型是‘list',转化为数组类型好处理
		#print("out0=",type(data),data.shape)
		#print("out1=",data)
		Y=data[:,0]
		Y=Y.astype(np.int32)
		end=1+feature_dimensions
		X=data[:,1:end]
		X=X.astype(np.float64)
#		print (X_train[0])
#		print (X_train[4999])
		return X,Y


###决策树模型
#tree_clf = DecisionTreeClassifier(max_depth=2, random_state=42)
#tree_clf.fit(X, y)
#tree_clf = DecisionTreeClassifier(max_depth=27, random_state=42)
#tree_clf.fit(X_train, Y_train)
#
####获取测试数据
#with open('G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random_test.scaled.csv','r') as csvfile:
#	reader = csv.reader(csvfile)
#	rows= [row for row in reader]
##print (rows)#输出所有数据
#data=np.array(rows)#rows是数据类型是‘list',转化为数组类型好处理
#Y_test=data[:,0]
#Y_test=Y_test.astype(np.int32)
#X_test=data[:,1:28]
#X_test=X_test.astype(np.float64)
#print (X_test[0])
#print (X_test[242301])

##预测Predicting classes and class probabilities

#result1=tree_clf.predict_proba([[1,0.833333,0,0.368817,0.266667,0,0,0.238806,0.092308,0,0.268657,0.092308,0,0.540926,0.229708,0.260968,0.744719,0.722781,0.598735,0.44186,0.442344,1,1,1,1,0,7.81766e-05]])
#result2=tree_clf.predict([[1,0.833333,0,0.368817,0.266667,0,0,0.238806,0.092308,0,0.268657,0.092308,0,0.540926,0.229708,0.260968,0.744719,0.722781,0.598735,0.44186,0.442344,1,1,1,1,0,7.81766e-05]])
#
#
##result1=tree_clf.predict_proba([[5, 1.5]])
#print (result1)
##result2=tree_clf.predict([[5, 1.5]])
#print (result2)

#xxx=X_train[4999]
#xxx = xxx[np.newaxis, :]
#result1=tree_clf.predict_proba(xxx) ###返回的是某个样本的概率
#result2=tree_clf.predict(xxx)
#print (result1)
#print (result2)
#
#predicted_result_prob=tree_clf.predict_proba(X_test)
#predicted_result=tree_clf.predict(X_test)
#from sklearn.metrics import classification_report
#print (classification_report(Y_test,predicted_result,labels=[1,-1],target_names=['Duplicate','NonDuplicate'],digits=4))

if __name__ == "__main__":

##	训练集->测试目标->使用的模型
##	print ("使用TC特征")
#	train_dataset=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_5000_1_4_train_random.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_5000_1_4_train_random.scaled.csv']
#	eclipse_test_dataset=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_5000_1_4_train_random_test.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_complete.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_complete.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_complete.scaled.csv']
#	openOffice_test_dataset=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_5000_1_4_train_random.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_5000_1_4_train_random_test.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_complete.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_complete.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_complete.scaled.csv']
#	netBeans_test_dataset=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_5000_1_4_train_random.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_5000_1_4_train_random_test.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_complete.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_complete.scaled.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_complete.scaled.csv']
#	E_xxx=['E-ETr','E-ETe','E-EC','E-OC','E-NC']
#	O_xxx=['O-OTr','O-OTe','O-OC','O-EC','O-NC']
#	N_xxx=['N-NTr','N-NTe','N-NC','N-EC','N-OC']
##
##	#训练eclipse数据集
#	feature_dimensions=27
#	train_path=train_dataset[0]
#	X_train,Y_train=processCSVForGetFeatureAndTagValues(train_path,feature_dimensions)
#	rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1, random_state=42)
#	rnd_clf.fit(X_train, Y_train)
#	for index,term in enumerate(E_xxx):
#		print (term)
#		test_path=eclipse_test_dataset[index]
#		X_test,Y_test=processCSVForGetFeatureAndTagValues(test_path,feature_dimensions)
#		predicted_result=rnd_clf.predict(X_test)
#		print (classification_report(Y_test,predicted_result,labels=[1,-1],target_names=['Duplicate','NonDuplicate'],digits=4))
#	#训练openOffice数据集
#	feature_dimensions=27
#	train_path=train_dataset[1]
#	X_train,Y_train=processCSVForGetFeatureAndTagValues(train_path,feature_dimensions)
#	rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1, random_state=42)
#	rnd_clf.fit(X_train, Y_train)
#	for index,term in enumerate(O_xxx):
#		print (term)
#		test_path=openOffice_test_dataset[index]
#		X_test,Y_test=processCSVForGetFeatureAndTagValues(test_path,feature_dimensions)
#		predicted_result=rnd_clf.predict(X_test)
#		print (classification_report(Y_test,predicted_result,labels=[1,-1],target_names=['Duplicate','NonDuplicate'],digits=4))
#	#训练netBeans数据集
#	feature_dimensions=27
#	train_path=train_dataset[2]
#	X_train,Y_train=processCSVForGetFeatureAndTagValues(train_path,feature_dimensions)
#	rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1, random_state=42)
#	rnd_clf.fit(X_train, Y_train)
#	for index,term in enumerate(N_xxx):
#		print (term)
#		test_path=netBeans_test_dataset[index]
#		X_test,Y_test=processCSVForGetFeatureAndTagValues(test_path,feature_dimensions)
#		predicted_result=rnd_clf.predict(X_test)
#		print (classification_report(Y_test,predicted_result,labels=[1,-1],target_names=['Duplicate','NonDuplicate'],digits=4))
	
	
	print ("使用DTC特征")
	#训练集->测试目标->使用的模型
	train_dataset=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_5000_1_4_train_random.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_5000_1_4_train_random.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_5000_1_4_train_random.csv']
	eclipse_test_dataset=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_5000_1_4_train_random.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_5000_1_4_train_random_test.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_complete.csv']
	openOffice_test_dataset=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_5000_1_4_train_random.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_5000_1_4_train_random_test.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_complete.csv']
	netBeans_test_dataset=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_5000_1_4_train_random.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_5000_1_4_train_random_test.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_complete.csv']
	E_xxx=['E-ETr','E-ETe','E-EC','E-OC','E-NC']
	O_xxx=['O-OTr','O-OTe','O-OC','O-EC','O-NC']
	N_xxx=['N-NTr','N-NTe','N-NC','N-EC','N-OC']

	#训练eclipse数据集
	feature_dimensions=28
	train_path=train_dataset[0]
	X_train,Y_train=processCSVForGetFeatureAndTagValues(train_path,feature_dimensions)
	rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1, random_state=42)
	rnd_clf.fit(X_train, Y_train)
	for index,term in enumerate(E_xxx):
		print (term)
		test_path=eclipse_test_dataset[index]
		X_test,Y_test=processCSVForGetFeatureAndTagValues(test_path,feature_dimensions)
		predicted_result=rnd_clf.predict(X_test)
		print (classification_report(Y_test,predicted_result,labels=[1,-1],target_names=['Duplicate','NonDuplicate'],digits=4))
	#训练openOffice数据集
	feature_dimensions=28
	train_path=train_dataset[1]
	X_train,Y_train=processCSVForGetFeatureAndTagValues(train_path,feature_dimensions)
	rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1, random_state=42)
	rnd_clf.fit(X_train, Y_train)
	for index,term in enumerate(O_xxx):
		print (term)
		test_path=openOffice_test_dataset[index]
		X_test,Y_test=processCSVForGetFeatureAndTagValues(test_path,feature_dimensions)
		predicted_result=rnd_clf.predict(X_test)
		print (classification_report(Y_test,predicted_result,labels=[1,-1],target_names=['Duplicate','NonDuplicate'],digits=4))
	#训练netBeans数据集
	feature_dimensions=28
	train_path=train_dataset[2]
	X_train,Y_train=processCSVForGetFeatureAndTagValues(train_path,feature_dimensions)
	rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1, random_state=42)
	rnd_clf.fit(X_train, Y_train)
	for index,term in enumerate(N_xxx):
		print (term)
		test_path=netBeans_test_dataset[index]
		X_test,Y_test=processCSVForGetFeatureAndTagValues(test_path,feature_dimensions)
		predicted_result=rnd_clf.predict(X_test)
		print (classification_report(Y_test,predicted_result,labels=[1,-1],target_names=['Duplicate','NonDuplicate'],digits=4))