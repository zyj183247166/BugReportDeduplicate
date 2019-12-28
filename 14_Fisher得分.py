# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:50:22 2019

@author: Administrator
"""
###基本计算原理 见https://stats.stackexchange.com/questions/277123/fisher-score-feature-selection-implementation
##即类间方差和类内方差的比。
#mu = mean(feature);
#
#n_1 = sum(label == 1);
#mu_1 = mean(feature(label == 1));
#var_1 = var(feature(label == 1));
#
#n_2 = sum(label == 2);
#mu_2 = mean(feature(label == 2));
#var_2 = var(feature(label == 2));
#
#inter_class = n_1*(mu_1-mu)^2 + n_2*(mu_2-mu)^2; 
#intra_class = (n_1-1)*var_1 + (n_2-1)*var_2;
#
#score = inter_class / intra_class;

###基本计算原理


import numpy as np

import pandas as pd


#pip install -U skfeature-chappers
import csv
def fscore_core(np,nn,xb,xbp,xbn,xkp,xkn):
    '''
    np: number of positive features
    nn: number of negative features
    xb: list of the average of each feature of the whole instances
    xbp: list of the average of each feature of the positive instances
    xbn: list of the average of each feature of the negative instances
    xkp: list of each feature which is a list of each positive instance
    xkn: list of each feature which is a list of each negatgive instance
    reference: http://link.springer.com/chapter/10.1007/978-3-540-35488-8_13
    '''

    def sigmap (i,np,xbp,xkp):
        return sum([(xkp[i][k]-xbp[i])**2 for k in range(np)])

    def sigman (i,nn,xbn,xkn):
#        print (sum([(xkn[i][k]-xbn[i])**2 for k in range(nn)]))
        return sum([(xkn[i][k]-xbn[i])**2 for k in range(nn)])

    n_feature = len(xb)
    fscores = []
    for i in range(n_feature):
        fscore_numerator = (xbp[i]-xb[i])**2 + (xbn[i]-xb[i])**2
        fscore_denominator = (1/float(np-1))*(sigmap(i,np,xbp,xkp))+ \
                             (1/float(nn-1))*(sigman(i,nn,xbn,xkn))
        fscores.append(fscore_numerator/fscore_denominator)

    return fscores

def fscore(feature,classindex):
    '''
    feature: a matrix whose row indicates instances, col indicates features
    classindex: 1 indicates positive and 0 indicates negative
	#修正为1表示正例子，然后-1表示负例子。
    '''
    n_instance = len(feature)
    n_feature  = len(feature[0])
#    np = sum(classindex) #这个用于统计1和0标签形式的数据。
    mask=(classindex==1)
    y_new=classindex[mask]
    np=y_new.size
#    print (np)
    nn = n_instance - np
    xkp =[];xkn =[];xbp =[];xbn =[];xb=[]
    for i in range(n_feature):
        xkp_i = [];xkn_i = []
        for k in range(n_instance):
            if classindex[k] == 1:
                xkp_i.append(feature[k][i])
            else:
                xkn_i.append(feature[k][i])
        xkp.append(xkp_i)
        xkn.append(xkn_i)
        sum_xkp_i = sum(xkp_i)
        sum_xkn_i = sum(xkn_i)
        xbp.append(sum_xkp_i/float(np))
        xbn.append(sum_xkn_i/float(nn))
        xb.append((sum_xkp_i+sum_xkn_i)/float(n_instance))
    return fscore_core(np,nn,xb,xbp,xbn,xkp,xkn)
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
print ("eclipse")
X_eclipse,Y_eclipse=processCSVForGetFeatureAndTagValues(dataset_path[0],feature_dimensions)

X_eclipse,Y_eclipse=processCSVForGetFeatureAndTagValues(dataset_path[0],feature_dimensions)
X_openOffice,Y_openOffice=processCSVForGetFeatureAndTagValues(dataset_path[1],feature_dimensions)
X_netBeans,Y_netBeans=processCSVForGetFeatureAndTagValues(dataset_path[2],feature_dimensions)
fscores_eclipse=fscore(X_eclipse,Y_eclipse)
fscores_openOffice=fscore(X_openOffice,Y_openOffice)
fscores_netBeans=fscore(X_netBeans,Y_netBeans)
for i in range(28):
	xx_e=fscores_eclipse[i]
	xx_o=fscores_openOffice[i]
	xx_n=fscores_netBeans[i]
	p=(xx_e+xx_o+xx_n)/3
	print (i+1," ", p)
#print (fscores_eclipse)



