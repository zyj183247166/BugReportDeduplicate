# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:54:10 2019

@author: Administrator
"""

import numpy as np
import math
####信息增益https://www.cnblogs.com/bhlsheji/p/4580439.html

import pandas as pd
import csv
from info_gain import info_gain
#! python2
import numpy as np
from math import log
###简单的示例
#data_feature_matrix = np.array([[1, 1],
#[1, 1],
#[1, 0],
#[0, 1],
#[0, 1]]) # 特征矩阵
#category = ['yes', 'yes', 'no', 'no', 'no'] # 5个对象分别所属的类别
#best_feature = choose_best_feature(data_feature_matrix, category)
#print ('最好用于划分数据集的特征为：', best_feature)
def calc_shannon_ent(category_list): #计算熵。
#:param category_list: 类别列表
#:return: 该类别列表的熵值
    label_count = {} # 统计数据集中每个类别的个数
    num = len(category_list) # 数据集个数
    for i in range(num):
        try:
            label_count[category_list[i]] += 1
        except KeyError:
            label_count[category_list[i]] = 1
            shannon_ent = 0.
    for k in label_count:
        prob = float(label_count[k]) / num
        shannon_ent -= prob * log(prob, 2) # 计算信息熵
    return shannon_ent
def split_data(feature_matrix, category_list, feature_index, value):
#筛选出指定特征值所对应的类别列表
#:param category_list: 类别列表
#:param feature_matrix: 特征矩阵
#:param feature_index: 指定特征索引
#:param value: 指定特征属性的特征值
#:return: 符合指定特征属性的特征值的类别列表
# feature_matrix = np.array(feature_matrix)
    ret_index = np.where(feature_matrix[:, feature_index] == value)[0] # 获取符合指定特征值的索引 （这个库）
    ret_category_list = [category_list[i] for i in ret_index] # 根据索引取得指定的所属类别，构建为列表
    return ret_category_list
def choose_best_feature(feature_matrix, category_list):
#根据信息增益获取最优特征
#:param feature_matrix: 特征矩阵
#:param category_list: 类别列表
#:return: 最优特征对应的索引
    feature_num = len(feature_matrix[0]) # 特征个数
    data_num = len(category_list) # 数据集的个数
    base_shannon_ent = calc_shannon_ent(category_list=category_list) # 原始数据的信息熵
    best_info_gain = 0 # 最优信息增益
    best_feature_index = -1 # 最优特征对应的索引
    for f in range(feature_num):
        print (f)
        uni_value_list = set(feature_matrix[:, f]) # 该特征属性所包含的特征值 #去除了重复，形成了一个集合。
        new_shannon_ent = 0.
        for value in uni_value_list:
            sub_cate_list = split_data(feature_matrix=feature_matrix, category_list=category_list, feature_index=f, value=value)
            prob = float(len(sub_cate_list)) / data_num
            new_shannon_ent += prob * calc_shannon_ent(sub_cate_list) #for循环计算的是这个变量的熵 而calc_shannon_ent计算的是变量取特定值后的熵。
        info_gain = base_shannon_ent - new_shannon_ent # 信息增益 #因此特征T给系统带来的信息增益就能够写成系统原本的熵与固定特征T后的条件熵之差：
        print ('初始信息熵为：', base_shannon_ent, '按照特征%i分类后的信息熵为：' % f, new_shannon_ent, '信息增益为：', info_gain)
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature_index = f
    return best_feature_index

def cal_IG(feature_matrix,category_list):
    feature_num = len(feature_matrix[0]) # 特征个数
    data_num = len(category_list) # 数据集的个数
    base_shannon_ent = calc_shannon_ent(category_list=category_list) # 原始数据的信息熵
    best_info_gain = 0 # 最优信息增益
    ig=[]
    for f in range(feature_num):
#        print (f)
        uni_value_list = set(feature_matrix[:, f]) # 该特征属性所包含的特征值 #去除了重复，形成了一个集合。
        new_shannon_ent = 0.
        for value in uni_value_list:
            sub_cate_list = split_data(feature_matrix=feature_matrix, category_list=category_list, feature_index=f, value=value)
            prob = float(len(sub_cate_list)) / data_num
            new_shannon_ent += prob * calc_shannon_ent(sub_cate_list) #for循环计算的是这个变量的熵 而calc_shannon_ent计算的是变量取特定值后的熵。
        info_gain = base_shannon_ent - new_shannon_ent # 信息增益 #因此特征T给系统带来的信息增益就能够写成系统原本的熵与固定特征T后的条件熵之差：
        print ('初始信息熵为：', base_shannon_ent, '按照特征%i分类后的信息熵为：' % (f+1), new_shannon_ent, '信息增益为：', info_gain)
        ig.append(info_gain)
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature_index = f
    return best_feature_index,ig
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

if __name__ == '__main__':
    dataset_path=['G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_complete.csv','G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_complete.csv']
    feature_dimensions=28
    X_eclipse,Y_eclipse=processCSVForGetFeatureAndTagValues(dataset_path[0],feature_dimensions)
    X_openOffice,Y_openOffice=processCSVForGetFeatureAndTagValues(dataset_path[1],feature_dimensions)
    X_netBeans,Y_netBeans=processCSVForGetFeatureAndTagValues(dataset_path[2],feature_dimensions)
    best_eclipse,ig_eclipse=cal_IG(X_eclipse,Y_eclipse)
    best_openOffice,ig_openOffice=cal_IG(X_openOffice,Y_openOffice)
    best_netBeans,ig_netBeans=cal_IG(X_netBeans,Y_netBeans)
    print (best_eclipse,best_openOffice,best_netBeans)
    for i in range(feature_dimensions):
    	xx_e=ig_eclipse[i]
    	xx_o=ig_openOffice[i]
    	xx_n=ig_netBeans[i]
    	p=(xx_e+xx_o+xx_n)/3
    	print (i+1," ", p)