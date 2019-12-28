# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:50:22 2019

@author: Administrator
"""

import numpy as np
from scipy.stats import pearsonr
import csv
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
dataset_path=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_complete.csv']
feature_dimensions=28
#print ("eclipse")
#X_eclipse,Y_eclipse=processCSVForGetFeatureAndTagValues(dataset_path[0],feature_dimensions)
#for i in range(28):
#	print (i)
#	xx=X_eclipse[:,i]
#	print (i," ", pearsonr(xx, Y_eclipse))
#print ("openOffice")
#X_openOffice,Y_openOffice=processCSVForGetFeatureAndTagValues(dataset_path[1],feature_dimensions)
#for i in range(28):
#	print (i)
#	xx=X_openOffice[:,i]
#	print (i," ", pearsonr(xx, Y_openOffice))
#print ("netBeans")
#X_netBeans,Y_netBeans=processCSVForGetFeatureAndTagValues(dataset_path[2],feature_dimensions)
#for i in range(28):
#	xx=X_netBeans[:,i]
#	print (i+1," ", pearsonr(xx, Y_netBeans))
	
###计算均值
print ("计算均值")
X_eclipse,Y_eclipse=processCSVForGetFeatureAndTagValues(dataset_path[0],feature_dimensions)
X_openOffice,Y_openOffice=processCSVForGetFeatureAndTagValues(dataset_path[1],feature_dimensions)
X_netBeans,Y_netBeans=processCSVForGetFeatureAndTagValues(dataset_path[2],feature_dimensions)
for i in range(28):
	xx_e=X_eclipse[:,i]
	xx_o=X_openOffice[:,i]
	xx_n=X_netBeans[:,i]
	ec=pearsonr(xx_e, Y_eclipse)
	ec=ec[0]
	oo=pearsonr(xx_o, Y_openOffice)
	oo=oo[0]
	ne=pearsonr(xx_n, Y_netBeans)
	ne=ne[0]
	p=(ec+oo+ne)/3
	print (i+1," ", p)

