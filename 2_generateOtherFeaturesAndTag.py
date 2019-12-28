# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:49:42 2019

@author: Administrator
"""
import pymongo

class MyMongo:
    def init(self):
        self.client=pymongo.MongoClient(host='localhost',port=27017)
client=pymongo.MongoClient(host='localhost',port=27017)
import re
import dateutil.parser as dparser
import pickle
import numpy as np
import os
import random
#########################################################################################################
#########辅助函数定义
#########################################################################################################
def save_to_pkl(python_content, pickle_name):
    with open(pickle_name, 'wb') as pickle_f:
        pickle.dump(python_content, pickle_f)
def read_from_pkl(pickle_name):
    with open(pickle_name, 'rb') as pickle_f:
        python_content = pickle.load(pickle_f)
    return python_content

#（7）以及存储非Takelab特征的其余7种特征的文件。以及生成标签数据文件。
# (7)-1处理netBeans
def generateOtherFeaturesAndTag_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    otherFeatures_test_path='./processedData_2014MSR_xiaojie/otherFeatures_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    tag_train_path='./processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'   ##gs表示standard groud也就是标签
    tag_test_path='./processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'   ##gs表示standard groud也就是标签
    otherFeatures_NoStartFrom1_train_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    otherFeatures_NoStartFrom1_test_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    ###先处理训练数据
    print ("先处理训练数据")
    all_pairs_forTrain=read_from_pkl(all_dataset_name1_forTrain)
    db=client.netBeans
    f1 = open(otherFeatures_train_path, 'w',encoding='UTF-8')
    f1_1 = open(otherFeatures_NoStartFrom1_train_path, 'w',encoding='UTF-8')
    f11 = open(tag_train_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTrain.keys():
        
        if (index%100==0):
            print ("index:",index)
        bug1=str(key[0])
        bug2=str(key[1])
        tag=all_pairs_forTrain[key]
#        if(tag==-1):
#           print (-1)
        f11.write(str(tag))
        f11.write('\n')
        f11.flush()
        index=index+1
#        print(bug1)
#        print(bug2)
#        ###测试用 当处理某个pair出现错误的时候
#        bug1="3820"
#        bug2="30090"
        #从数据库中取出第一个bug report
        condition1={'bug_id':bug1}
        bug_report1=db.clear.find_one(condition1)
        if bug_report1==None:
            bug_report1=db.initial.find_one(condition1)
        condition2={'bug_id':bug2}
        bug_report2=db.clear.find_one(condition2)
        if bug_report2==None:
            bug_report2=db.initial.find_one(condition2)
        
        #（1）product属性
        try:
            product1=bug_report1["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product1=''
        try:
            product2=bug_report2["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product2=''
        
        if(product1==product2):
            feature1=1
        else:
            feature1=0
        #（2）component
        try:
            component1=bug_report1["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component1=''
        try:
            component2=bug_report2["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component2=''
        
        if(component1==component2):
            feature2=1
        else:
            feature2=0
        
        #（3）bug.type的数据是缺失的
        #（4）优先级的数据
        try:
            priority1=bug_report1["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority1=''
        try:
            priority2=bug_report2["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority2=''        
        if (priority1==''):
            priority1=0 #如果优先级信息缺失，我们就设为0.
        else:
            priority1=(int)(priority1[-1])
        if (priority2==''):
            priority2=0
        else:
            priority2=(int)(priority2[-1])
        feature4=1/(1+abs(priority1-priority2))
        
        #（5）版本号的数据。这个版本号有3.x这种，也有2.2.1这种。我们直接取前两位。
        try:
            version1=bug_report1["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version1=''
        try:
            version2=bug_report2["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version2=''
        if (version1==''):
            version1=0 #如果版本信息缺失，我们就设为0.
        else:
            version1=re.findall(r'\d+',version1)
            if (version1==[]):
                version1=0 #没有提取出浮点数
            elif(len(version1)==1):
                version1=(float)(version1[0])
            else:
                version1=(float)(version1[0])+0.1*(float)(version1[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。

        if (version2==''):
            version2=0
        else:
            version2=re.findall(r'\d+',version2)
            if (version2==[]):
                version2=0 #没有提取出浮点数
            elif(len(version2)==1):
                version2=(float)(version2[0])
            else:
                version2=(float)(version2[0])+0.1*(float)(version2[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。
        feature5=1/(1+abs(version1-version2))
        
        #（6）日期 date
        try:
            date1=bug_report1["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date1=''
        try:
            date2=bug_report2["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date2=''
        
        date1=dparser.parse(date1)
        date2=dparser.parse(date2)
        #用相差的天数
        xx=abs((date1-date2).total_seconds()) #使用seconds有问题，要用total_seconds
        feature6=(int)(xx/86400) #不会四舍五入，比如0.6，就是0
        #（7）日期 bug_id 号
        try:
            bug_id1=bug_report1["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id1=''
        try:
            bug_id2=bug_report2["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id2=''
        
        bug_id1=(int)(bug_id1)
        bug_id2=(int)(bug_id2)
        feature7=abs(bug_id1-bug_id2)
        f1.write(' 22:%d' % (feature1))
        f1.write(' 23:%d' % (feature2))
        f1.write(' 24:%f' % (feature4))
        f1.write(' 25:%f' % (feature5))
        f1.write(' 26:%d' % (feature6))
        f1.write(' 27:%d' % (feature7))
        f1.write('\n')
        f1.flush()
        f1_1.write(' 1:%d' % (feature1))
        f1_1.write(' 2:%d' % (feature2))
        f1_1.write(' 3:%f' % (feature4))
        f1_1.write(' 4:%f' % (feature5))
        f1_1.write(' 5:%d' % (feature6))
        f1_1.write(' 6:%d' % (feature7))
        f1_1.write('\n')
        f1_1.flush()
        pass
    ###再处理测试数据
    print ("再处理测试数据")
    del(all_pairs_forTrain)
    all_pairs_forTest=read_from_pkl(all_dataset_name1_forTest)
    f2 = open(otherFeatures_test_path, 'w',encoding='UTF-8')
    f2_2 = open(otherFeatures_NoStartFrom1_test_path, 'w',encoding='UTF-8')
    f22 = open(tag_test_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTest.keys():
        
        if (index%100==0):
            print ("index:",index)
        bug1=str(key[0])
        bug2=str(key[1])
        tag=all_pairs_forTest[key]
        f22.write(str(tag))
        f22.write('\n')
        f22.flush()
        index=index+1
#        print(bug1)
#        print(bug2)
#        ###测试用 当处理某个pair出现错误的时候
#        bug1="3820"
#        bug2="30090"
        #从数据库中取出第一个bug report
        condition1={'bug_id':bug1}
        bug_report1=db.clear.find_one(condition1)
        if bug_report1==None:
            bug_report1=db.initial.find_one(condition1)
        condition2={'bug_id':bug2}
        bug_report2=db.clear.find_one(condition2)
        if bug_report2==None:
            bug_report2=db.initial.find_one(condition2)
        
        #（1）product属性
        try:
            product1=bug_report1["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product1=''
        try:
            product2=bug_report2["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product2=''
        
        if(product1==product2):
            feature1=1
        else:
            feature1=0
        #（2）component
        try:
            component1=bug_report1["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component1=''
        try:
            component2=bug_report2["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component2=''
        
        if(component1==component2):
            feature2=1
        else:
            feature2=0
        
        #（3）bug.type的数据是缺失的
        #（4）优先级的数据
        try:
            priority1=bug_report1["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority1=''
        try:
            priority2=bug_report2["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority2=''        
        if (priority1==''):
            priority1=0 #如果优先级信息缺失，我们就设为0.
        else:
            priority1=(int)(priority1[-1])
        if (priority2==''):
            priority2=0
        else:
            priority2=(int)(priority2[-1])
        feature4=1/(1+abs(priority1-priority2))
        
        #（5）版本号的数据。这个版本号有3.x这种，也有2.2.1这种。我们直接取前两位。
        try:
            version1=bug_report1["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version1=''
        try:
            version2=bug_report2["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version2=''
        if (version1==''):
            version1=0 #如果版本信息缺失，我们就设为0.
        else:
            version1=re.findall(r'\d+',version1)
            if (version1==[]):
                version1=0 #没有提取出浮点数
            elif(len(version1)==1):
                version1=(float)(version1[0])
            else:
                version1=(float)(version1[0])+0.1*(float)(version1[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。

        if (version2==''):
            version2=0
        else:
            version2=re.findall(r'\d+',version2)
            if (version2==[]):
                version2=0 #没有提取出浮点数
            elif(len(version2)==1):
                version2=(float)(version2[0])
            else:
                version2=(float)(version2[0])+0.1*(float)(version2[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。
        feature5=1/(1+abs(version1-version2))
        
        #（6）日期 date
        try:
            date1=bug_report1["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date1=''
        try:
            date2=bug_report2["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date2=''
        
        date1=dparser.parse(date1)
        date2=dparser.parse(date2)
        #用相差的天数
        xx=abs((date1-date2).total_seconds()) #使用seconds有问题，要用total_seconds
        feature6=(int)(xx/86400) #不会四舍五入，比如0.6，就是0
        #（7）日期 bug_id 号
        try:
            bug_id1=bug_report1["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id1=''
        try:
            bug_id2=bug_report2["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id2=''
        
        bug_id1=(int)(bug_id1)
        bug_id2=(int)(bug_id2)
        feature7=abs(bug_id1-bug_id2)
        f2.write(' 22:%d' % (feature1))
        f2.write(' 23:%d' % (feature2))
        f2.write(' 24:%f' % (feature4))
        f2.write(' 25:%f' % (feature5))
        f2.write(' 26:%d' % (feature6))
        f2.write(' 27:%d' % (feature7))
        f2.write('\n')
        f2.flush()
        f2_2.write(' 1:%d' % (feature1))
        f2_2.write(' 2:%d' % (feature2))
        f2_2.write(' 3:%f' % (feature4))
        f2_2.write(' 4:%f' % (feature5))
        f2_2.write(' 5:%d' % (feature6))
        f2_2.write(' 6:%d' % (feature7))
        f2_2.write('\n')
        f2_2.flush()
        pass

#（7）-2处理 eclipse
def generateOtherFeaturesAndTag_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    otherFeatures_test_path='./processedData_2014MSR_xiaojie/otherFeatures_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    tag_train_path='./processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'   ##gs表示standard groud也就是标签
    tag_test_path='./processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'   ##gs表示standard groud也就是标签
    otherFeatures_NoStartFrom1_train_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    otherFeatures_NoStartFrom1_test_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    ###先处理训练数据
    print ("先处理训练数据")
    all_pairs_forTrain=read_from_pkl(all_dataset_name1_forTrain)
    db=client.eclipse
    f1 = open(otherFeatures_train_path, 'w',encoding='UTF-8')
    f1_1 = open(otherFeatures_NoStartFrom1_train_path, 'w',encoding='UTF-8')
    f11 = open(tag_train_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTrain.keys():
        
        if (index%100==0):
            print ("index:",index)
        bug1=str(key[0])
        bug2=str(key[1])
        tag=all_pairs_forTrain[key]
#        if(tag==-1):
#           print (-1)
        f11.write(str(tag))
        f11.write('\n')
        f11.flush()
        index=index+1
#        print(bug1)
#        print(bug2)
#        ###测试用 当处理某个pair出现错误的时候
#        bug1="3820"
#        bug2="30090"
        #从数据库中取出第一个bug report
        condition1={'bug_id':bug1}
        bug_report1=db.clear.find_one(condition1)
        if bug_report1==None:
            bug_report1=db.initial.find_one(condition1)
        condition2={'bug_id':bug2}
        bug_report2=db.clear.find_one(condition2)
        if bug_report2==None:
            bug_report2=db.initial.find_one(condition2)
        
        #（1）product属性
        try:
            product1=bug_report1["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product1=''
        try:
            product2=bug_report2["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product2=''
        
        if(product1==product2):
            feature1=1
        else:
            feature1=0
        #（2）component
        try:
            component1=bug_report1["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component1=''
        try:
            component2=bug_report2["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component2=''
        
        if(component1==component2):
            feature2=1
        else:
            feature2=0
        
        #（3）bug.type的数据是缺失的
        #（4）优先级的数据
        try:
            priority1=bug_report1["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority1=''
        try:
            priority2=bug_report2["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority2=''        
        if (priority1==''):
            priority1=0 #如果优先级信息缺失，我们就设为0.
        else:
            priority1=(int)(priority1[-1])
        if (priority2==''):
            priority2=0
        else:
            priority2=(int)(priority2[-1])
        feature4=1/(1+abs(priority1-priority2))
        
        #（5）版本号的数据。这个版本号有3.x这种，也有2.2.1这种。我们直接取前两位。
        try:
            version1=bug_report1["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version1=''
        try:
            version2=bug_report2["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version2=''
        if (version1==''):
            version1=0 #如果版本信息缺失，我们就设为0.
        else:
            version1=re.findall(r'\d+',version1)
            if (version1==[]):
                version1=0 #没有提取出浮点数
            elif(len(version1)==1):
                version1=(float)(version1[0])
            else:
                version1=(float)(version1[0])+0.1*(float)(version1[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。

        if (version2==''):
            version2=0
        else:
            version2=re.findall(r'\d+',version2)
            if (version2==[]):
                version2=0 #没有提取出浮点数
            elif(len(version2)==1):
                version2=(float)(version2[0])
            else:
                version2=(float)(version2[0])+0.1*(float)(version2[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。
        feature5=1/(1+abs(version1-version2))
        
        #（6）日期 date
        try:
            date1=bug_report1["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date1=''
        try:
            date2=bug_report2["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date2=''
        
        date1=dparser.parse(date1)
        date2=dparser.parse(date2)
        #用相差的天数
        xx=abs((date1-date2).total_seconds()) #使用seconds有问题，要用total_seconds
        feature6=(int)(xx/86400) #不会四舍五入，比如0.6，就是0
        #（7）日期 bug_id 号
        try:
            bug_id1=bug_report1["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id1=''
        try:
            bug_id2=bug_report2["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id2=''
        
        bug_id1=(int)(bug_id1)
        bug_id2=(int)(bug_id2)
        feature7=abs(bug_id1-bug_id2)
        f1.write(' 22:%d' % (feature1))
        f1.write(' 23:%d' % (feature2))
        f1.write(' 24:%f' % (feature4))
        f1.write(' 25:%f' % (feature5))
        f1.write(' 26:%d' % (feature6))
        f1.write(' 27:%d' % (feature7))
        f1.write('\n')
        f1.flush()
        f1_1.write(' 1:%d' % (feature1))
        f1_1.write(' 2:%d' % (feature2))
        f1_1.write(' 3:%f' % (feature4))
        f1_1.write(' 4:%f' % (feature5))
        f1_1.write(' 5:%d' % (feature6))
        f1_1.write(' 6:%d' % (feature7))
        f1_1.write('\n')
        f1_1.flush()
        pass
    ###再处理测试数据
    print ("再处理测试数据")
    del(all_pairs_forTrain)
    all_pairs_forTest=read_from_pkl(all_dataset_name1_forTest)
    f2 = open(otherFeatures_test_path, 'w',encoding='UTF-8')
    f2_2 = open(otherFeatures_NoStartFrom1_test_path, 'w',encoding='UTF-8')
    f22 = open(tag_test_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTest.keys():
        
        if (index%100==0):
            print ("index:",index)
        bug1=str(key[0])
        bug2=str(key[1])
        tag=all_pairs_forTest[key]
        f22.write(str(tag))
        f22.write('\n')
        f22.flush()
        index=index+1
#        print(bug1)
#        print(bug2)
#        ###测试用 当处理某个pair出现错误的时候
#        bug1="3820"
#        bug2="30090"
        #从数据库中取出第一个bug report
        condition1={'bug_id':bug1}
        bug_report1=db.clear.find_one(condition1)
        if bug_report1==None:
            bug_report1=db.initial.find_one(condition1)
        condition2={'bug_id':bug2}
        bug_report2=db.clear.find_one(condition2)
        if bug_report2==None:
            bug_report2=db.initial.find_one(condition2)
        
        #（1）product属性
        try:
            product1=bug_report1["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product1=''
        try:
            product2=bug_report2["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product2=''
        
        if(product1==product2):
            feature1=1
        else:
            feature1=0
        #（2）component
        try:
            component1=bug_report1["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component1=''
        try:
            component2=bug_report2["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component2=''
        
        if(component1==component2):
            feature2=1
        else:
            feature2=0
        
        #（3）bug.type的数据是缺失的
        #（4）优先级的数据
        try:
            priority1=bug_report1["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority1=''
        try:
            priority2=bug_report2["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority2=''        
        if (priority1==''):
            priority1=0 #如果优先级信息缺失，我们就设为0.
        else:
            priority1=(int)(priority1[-1])
        if (priority2==''):
            priority2=0
        else:
            priority2=(int)(priority2[-1])
        feature4=1/(1+abs(priority1-priority2))
        
        #（5）版本号的数据。这个版本号有3.x这种，也有2.2.1这种。我们直接取前两位。
        try:
            version1=bug_report1["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version1=''
        try:
            version2=bug_report2["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version2=''
        if (version1==''):
            version1=0 #如果版本信息缺失，我们就设为0.
        else:
            version1=re.findall(r'\d+',version1)
            if (version1==[]):
                version1=0 #没有提取出浮点数
            elif(len(version1)==1):
                version1=(float)(version1[0])
            else:
                version1=(float)(version1[0])+0.1*(float)(version1[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。

        if (version2==''):
            version2=0
        else:
            version2=re.findall(r'\d+',version2)
            if (version2==[]):
                version2=0 #没有提取出浮点数
            elif(len(version2)==1):
                version2=(float)(version2[0])
            else:
                version2=(float)(version2[0])+0.1*(float)(version2[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。
        feature5=1/(1+abs(version1-version2))
        
        #（6）日期 date
        try:
            date1=bug_report1["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date1=''
        try:
            date2=bug_report2["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date2=''
        
        date1=dparser.parse(date1)
        date2=dparser.parse(date2)
        #用相差的天数
        xx=abs((date1-date2).total_seconds()) #使用seconds有问题，要用total_seconds
        feature6=(int)(xx/86400) #不会四舍五入，比如0.6，就是0
        #（7）日期 bug_id 号
        try:
            bug_id1=bug_report1["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id1=''
        try:
            bug_id2=bug_report2["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id2=''
        
        bug_id1=(int)(bug_id1)
        bug_id2=(int)(bug_id2)
        feature7=abs(bug_id1-bug_id2)
        f2.write(' 22:%d' % (feature1))
        f2.write(' 23:%d' % (feature2))
        f2.write(' 24:%f' % (feature4))
        f2.write(' 25:%f' % (feature5))
        f2.write(' 26:%d' % (feature6))
        f2.write(' 27:%d' % (feature7))
        f2.write('\n')
        f2.flush()
        f2_2.write(' 1:%d' % (feature1))
        f2_2.write(' 2:%d' % (feature2))
        f2_2.write(' 3:%f' % (feature4))
        f2_2.write(' 4:%f' % (feature5))
        f2_2.write(' 5:%d' % (feature6))
        f2_2.write(' 6:%d' % (feature7))
        f2_2.write('\n')
        f2_2.flush()
        pass

#（7）-3处理 openOffice
def generateOtherFeaturesAndTag_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    otherFeatures_test_path='./processedData_2014MSR_xiaojie/otherFeatures_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    tag_train_path='./processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'   ##gs表示standard groud也就是标签
    tag_test_path='./processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'   ##gs表示standard groud也就是标签
    otherFeatures_NoStartFrom1_train_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    otherFeatures_NoStartFrom1_test_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    ###先处理训练数据
    print ("先处理训练数据")
    all_pairs_forTrain=read_from_pkl(all_dataset_name1_forTrain)
    db=client.openOffice
    f1 = open(otherFeatures_train_path, 'w',encoding='UTF-8')
    f1_1 = open(otherFeatures_NoStartFrom1_train_path, 'w',encoding='UTF-8')
    f11 = open(tag_train_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTrain.keys():
        
        if (index%100==0):
            print ("index:",index)
        bug1=str(key[0])
        bug2=str(key[1])
        tag=all_pairs_forTrain[key]
#        if(tag==-1):
#           print (-1)
        f11.write(str(tag))
        f11.write('\n')
        f11.flush()
        index=index+1
#        print(bug1)
#        print(bug2)
#        ###测试用 当处理某个pair出现错误的时候
#        bug1="3820"
#        bug2="30090"
        #从数据库中取出第一个bug report
        condition1={'bug_id':bug1}
        bug_report1=db.clear.find_one(condition1)
        if bug_report1==None:
            bug_report1=db.initial.find_one(condition1)
        condition2={'bug_id':bug2}
        bug_report2=db.clear.find_one(condition2)
        if bug_report2==None:
            bug_report2=db.initial.find_one(condition2)
        
        #（1）product属性
        try:
            product1=bug_report1["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product1=''
        try:
            product2=bug_report2["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product2=''
        
        if(product1==product2):
            feature1=1
        else:
            feature1=0
        #（2）component
        try:
            component1=bug_report1["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component1=''
        try:
            component2=bug_report2["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component2=''
        
        if(component1==component2):
            feature2=1
        else:
            feature2=0
        
        #（3）bug.type的数据是缺失的
        #（4）优先级的数据
        try:
            priority1=bug_report1["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority1=''
        try:
            priority2=bug_report2["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority2=''        
        if (priority1==''):
            priority1=0 #如果优先级信息缺失，我们就设为0.
        else:
            priority1=(int)(priority1[-1])
        if (priority2==''):
            priority2=0
        else:
            priority2=(int)(priority2[-1])
        feature4=1/(1+abs(priority1-priority2))
        
        #（5）版本号的数据。这个版本号有3.x这种，也有2.2.1这种。我们直接取前两位。
        try:
            version1=bug_report1["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version1=''
        try:
            version2=bug_report2["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version2=''
        if (version1==''):
            version1=0 #如果版本信息缺失，我们就设为0.
        else:
            version1=re.findall(r'\d+',version1)
            if (version1==[]):
                version1=0 #没有提取出浮点数
            elif(len(version1)==1):
                version1=(float)(version1[0])
            else:
                version1=(float)(version1[0])+0.1*(float)(version1[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。

        if (version2==''):
            version2=0
        else:
            version2=re.findall(r'\d+',version2)
            if (version2==[]):
                version2=0 #没有提取出浮点数
            elif(len(version2)==1):
                version2=(float)(version2[0])
            else:
                version2=(float)(version2[0])+0.1*(float)(version2[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。
        feature5=1/(1+abs(version1-version2))
        
        #（6）日期 date
        try:
            date1=bug_report1["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date1=''
        try:
            date2=bug_report2["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date2=''
        
        date1=dparser.parse(date1)
        date2=dparser.parse(date2)
        #用相差的天数
        xx=abs((date1-date2).total_seconds()) #使用seconds有问题，要用total_seconds
        feature6=(int)(xx/86400) #不会四舍五入，比如0.6，就是0
        #（7）日期 bug_id 号
        try:
            bug_id1=bug_report1["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id1=''
        try:
            bug_id2=bug_report2["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id2=''
        
        bug_id1=(int)(bug_id1)
        bug_id2=(int)(bug_id2)
        feature7=abs(bug_id1-bug_id2)
        f1.write(' 22:%d' % (feature1))
        f1.write(' 23:%d' % (feature2))
        f1.write(' 24:%f' % (feature4))
        f1.write(' 25:%f' % (feature5))
        f1.write(' 26:%d' % (feature6))
        f1.write(' 27:%d' % (feature7))
        f1.write('\n')
        f1.flush()
        f1_1.write(' 1:%d' % (feature1))
        f1_1.write(' 2:%d' % (feature2))
        f1_1.write(' 3:%f' % (feature4))
        f1_1.write(' 4:%f' % (feature5))
        f1_1.write(' 5:%d' % (feature6))
        f1_1.write(' 6:%d' % (feature7))
        f1_1.write('\n')
        f1_1.flush()
        pass
    ###再处理测试数据
    print ("再处理测试数据")
    del(all_pairs_forTrain)
    all_pairs_forTest=read_from_pkl(all_dataset_name1_forTest)
    f2 = open(otherFeatures_test_path, 'w',encoding='UTF-8')
    f2_2 = open(otherFeatures_NoStartFrom1_test_path, 'w',encoding='UTF-8')
    f22 = open(tag_test_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTest.keys():
        
        if (index%100==0):
            print ("index:",index)
        bug1=str(key[0])
        bug2=str(key[1])
        tag=all_pairs_forTest[key]
        f22.write(str(tag))
        f22.write('\n')
        f22.flush()
        index=index+1
#        print(bug1)
#        print(bug2)
#        ###测试用 当处理某个pair出现错误的时候
#        bug1="3820"
#        bug2="30090"
        #从数据库中取出第一个bug report
        condition1={'bug_id':bug1}
        bug_report1=db.clear.find_one(condition1)
        if bug_report1==None:
            bug_report1=db.initial.find_one(condition1)
        condition2={'bug_id':bug2}
        bug_report2=db.clear.find_one(condition2)
        if bug_report2==None:
            bug_report2=db.initial.find_one(condition2)
        
        #（1）product属性
        try:
            product1=bug_report1["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product1=''
        try:
            product2=bug_report2["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            product2=''
        
        if(product1==product2):
            feature1=1
        else:
            feature1=0
        #（2）component
        try:
            component1=bug_report1["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component1=''
        try:
            component2=bug_report2["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            component2=''
        
        if(component1==component2):
            feature2=1
        else:
            feature2=0
        
        #（3）bug.type的数据是缺失的
        #（4）优先级的数据
        try:
            priority1=bug_report1["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority1=''
        try:
            priority2=bug_report2["priority"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            priority2=''        
        if (priority1==''):
            priority1=0 #如果优先级信息缺失，我们就设为0.
        else:
            priority1=(int)(priority1[-1])
        if (priority2==''):
            priority2=0
        else:
            priority2=(int)(priority2[-1])
        feature4=1/(1+abs(priority1-priority2))
        
        #（5）版本号的数据。这个版本号有3.x这种，也有2.2.1这种。我们直接取前两位。
        try:
            version1=bug_report1["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version1=''
        try:
            version2=bug_report2["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            version2=''
        if (version1==''):
            version1=0 #如果版本信息缺失，我们就设为0.
        else:
            version1=re.findall(r'\d+',version1)
            if (version1==[]):
                version1=0 #没有提取出浮点数
            elif(len(version1)==1):
                version1=(float)(version1[0])
            else:
                version1=(float)(version1[0])+0.1*(float)(version1[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。

        if (version2==''):
            version2=0
        else:
            version2=re.findall(r'\d+',version2)
            if (version2==[]):
                version2=0 #没有提取出浮点数
            elif(len(version2)==1):
                version2=(float)(version2[0])
            else:
                version2=(float)(version2[0])+0.1*(float)(version2[1]) ##比如从“1.2.3”在提取浮点数，会提取出1.2和3两个数。我们只用前面的。
        feature5=1/(1+abs(version1-version2))
        
        #（6）日期 date
        try:
            date1=bug_report1["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date1=''
        try:
            date2=bug_report2["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            date2=''
        
        date1=dparser.parse(date1)
        date2=dparser.parse(date2)
        #用相差的天数
        xx=abs((date1-date2).total_seconds()) #使用seconds有问题，要用total_seconds
        feature6=(int)(xx/86400) #不会四舍五入，比如0.6，就是0
        #（7）日期 bug_id 号
        try:
            bug_id1=bug_report1["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id1=''
        try:
            bug_id2=bug_report2["bug_id"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            bug_id2=''
        
        bug_id1=(int)(bug_id1)
        bug_id2=(int)(bug_id2)
        feature7=abs(bug_id1-bug_id2)
        f2.write(' 22:%d' % (feature1))
        f2.write(' 23:%d' % (feature2))
        f2.write(' 24:%f' % (feature4))
        f2.write(' 25:%f' % (feature5))
        f2.write(' 26:%d' % (feature6))
        f2.write(' 27:%d' % (feature7))
        f2.write('\n')
        f2.flush()
        f2_2.write(' 1:%d' % (feature1))
        f2_2.write(' 2:%d' % (feature2))
        f2_2.write(' 3:%f' % (feature4))
        f2_2.write(' 4:%f' % (feature5))
        f2_2.write(' 5:%d' % (feature6))
        f2_2.write(' 6:%d' % (feature7))
        f2_2.write('\n')
        f2_2.flush()
        pass

if __name__ == "__main__":
#    trainset_num_list=[5000,10000,15000,20000]
    trainset_num_list=[5000]
    ratio_TrueFlag=1
    ratio_FalseFlag=4
    for trainset_num in trainset_num_list:
#        generateOtherFeaturesAndTag_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        generateOtherFeaturesAndTag_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        generateOtherFeaturesAndTag_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag)

