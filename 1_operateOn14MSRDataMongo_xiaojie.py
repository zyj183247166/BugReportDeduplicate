# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 07:20:34 2019

@author: xiaojie
"""
import pymongo
class MyMongo:
    def init(self):
        self.client=pymongo.MongoClient(host='localhost',port=27017)
client=pymongo.MongoClient(host='localhost',port=27017)


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



##(1)输出集合数目
#db=client.openOffice
#openOfficeDuplicateBugPairsNum=db.pairs.estimated_document_count()
#print (openOfficeDuplicateBugPairsNum)


##(2)尝试性输出内容
#cursor=db.pairs.find()
#i=0
#for document in cursor:
#    #print (("%d:"%(i)),_student_)
#    if(i==10):
#        break
#    i=i+1
#    bug1=document['bug1']
#    bug2=document['bug2']
#    print (bug1,bug2)
##    new_file_path=filepath.replace("./weixin_article/","./")
##    result=db["picture_urlMd5_filepath"].update_many({'filepath':filepath},{'$set':{'filepath':new_file_path}})

##(3)数据库去重
#(3)_1 openOffice数据集去重

def eliminate_duplicateRecords_in_openOffice():
    db=client.openOffice
    openOfficeDuplicateBugPairsNum=db.pairs.estimated_document_count()
    print (openOfficeDuplicateBugPairsNum)
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_openOffice_XIAOJIE.pkl'
    duplicate_true_pair_record_path='./processedData_2014MSR_xiaojie/duplicate_true_pair_record_openOffice.txt' #openOffice的pairs集合中重复的正标签数据。
    duplicate_false_pair_record_path='./processedData_2014MSR_xiaojie/duplicate_false_pair_record_openOffice.txt'#openOffice的pairs集合中重复的负标签数据。
    if not os.path.exists('./processedData_2014MSR_xiaojie/'):
            os.mkdir('./processedData_2014MSR_xiaojie/')
    
    all_data1 = {}
    f1 = open(duplicate_true_pair_record_path, 'w')
    duplicate_trueduplicatepair_num=0
    f1.write('id1,id2,is_duplicateReport\n')
    f2 = open(duplicate_false_pair_record_path, 'w')
    duplicate_falseduplicatepair_num=0
    f2.write('id1,id2,is_duplicateReport\n')
    
    cursor=db.pairs.find()
    for document in cursor:
        
        bug1=(int)(document['bug1'])
        bug2=(int)(document['bug2'])
        isDuplicate=(int)(document['dec'])
    #    print (bug1,bug2)
        key = (bug1, bug2)
        key2= (bug2, bug1)
        if((key in all_data1.keys())or(key2 in all_data1.keys())):
            if(isDuplicate==1):
                duplicate_trueduplicatepair_num=duplicate_trueduplicatepair_num+1
                f1.write('%s,%s,%s\n'%(str(bug1),str(bug2),str(isDuplicate)))
                #写入文件
                continue
            if(isDuplicate==-1):
                duplicate_falseduplicatepair_num=duplicate_falseduplicatepair_num+1
                f2.write('%s,%s,%s\n'%(str(bug1),str(bug2),str(isDuplicate)))
                #写入文件
                continue
        all_data1[key] = isDuplicate  
    save_to_pkl(all_data1, all_dataset_name1)
    f1.close()
    f2.close()
    print('openOffice的pairs集合中重复的正标签数据{}个，openOffice的pairs集合中重复的负标签数据{}个'.format(duplicate_trueduplicatepair_num,duplicate_falseduplicatepair_num))
    print('openOffice的pairs集合中最后标签数据集的大小为{}'.format(len(all_data1)))
#eliminate_duplicateRecords_in_openOffice()
    
    
#(3)_2 netBeans数据集去重

def Eliminate_duplicateRecords_in_netBeans():
    db=client.netBeans
    netBeansDuplicateBugPairsNum=db.pairs.estimated_document_count()
    print (netBeansDuplicateBugPairsNum)
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_netBeans_XIAOJIE.pkl'
    duplicate_true_pair_record_path='./processedData_2014MSR_xiaojie/duplicate_true_pair_record_netBeans.txt' #openOffice的pairs集合中重复的正标签数据。
    duplicate_false_pair_record_path='./processedData_2014MSR_xiaojie/duplicate_false_pair_record_netBeans.txt'#openOffice的pairs集合中重复的负标签数据。
    if not os.path.exists('./processedData_2014MSR_xiaojie/'):
            os.mkdir('./processedData_2014MSR_xiaojie/')
    
    all_data1 = {}
    f1 = open(duplicate_true_pair_record_path, 'w')
    duplicate_trueduplicatepair_num=0
    f1.write('id1,id2,is_duplicateReport\n')
    f2 = open(duplicate_false_pair_record_path, 'w')
    duplicate_falseduplicatepair_num=0
    f2.write('id1,id2,is_duplicateReport\n')
    
    cursor=db.pairs.find()
    for document in cursor:
        
        bug1=(int)(document['bug1'])
        bug2=(int)(document['bug2'])
        isDuplicate=(int)(document['dec'])
    #    print (bug1,bug2)
        key = (bug1, bug2)
        key2= (bug2, bug1)
        if((key in all_data1.keys())or(key2 in all_data1.keys())):
            if(isDuplicate==1):
                duplicate_trueduplicatepair_num=duplicate_trueduplicatepair_num+1
                f1.write('%s,%s,%s\n'%(str(bug1),str(bug2),str(isDuplicate)))
                #写入文件
                continue
            if(isDuplicate==-1):
                duplicate_falseduplicatepair_num=duplicate_falseduplicatepair_num+1
                f2.write('%s,%s,%s\n'%(str(bug1),str(bug2),str(isDuplicate)))
                #写入文件
                continue
        all_data1[key] = isDuplicate  
    save_to_pkl(all_data1, all_dataset_name1)
    f1.close()
    f2.close()
    print('netBeans的pairs集合中重复的正标签数据{}个，netBeans的pairs集合中重复的负标签数据{}个'.format(duplicate_trueduplicatepair_num,duplicate_falseduplicatepair_num))
    print('netBeans的pairs集合中最后标签数据集的大小为{}'.format(len(all_data1)))
#Eliminate_duplicateRecords_in_netBeans()

#(3)_3 Eclipse数据集去重

def Eliminate_duplicateRecords_in_Eclipse():
    db=client.eclipse
    EclipseDuplicateBugPairsNum=db.pairs.estimated_document_count()
    print (EclipseDuplicateBugPairsNum)
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_Eclipse_XIAOJIE.pkl'
    duplicate_true_pair_record_path='./processedData_2014MSR_xiaojie/duplicate_true_pair_record_Eclipse.txt' #openOffice的pairs集合中重复的正标签数据。
    duplicate_false_pair_record_path='./processedData_2014MSR_xiaojie/duplicate_false_pair_record_Eclipse.txt'#openOffice的pairs集合中重复的负标签数据。
    if not os.path.exists('./processedData_2014MSR_xiaojie/'):
            os.mkdir('./processedData_2014MSR_xiaojie/')
    
    all_data1 = {}
    f1 = open(duplicate_true_pair_record_path, 'w')
    duplicate_trueduplicatepair_num=0
    f1.write('id1,id2,is_duplicateReport\n')
    f2 = open(duplicate_false_pair_record_path, 'w')
    duplicate_falseduplicatepair_num=0
    f2.write('id1,id2,is_duplicateReport\n')
    
    cursor=db.pairs.find()
    for document in cursor:
        
        bug1=(int)(document['bug1'])
        bug2=(int)(document['bug2'])
        isDuplicate=(int)(document['dec'])
    #    print (bug1,bug2)
        key = (bug1, bug2)
        key2= (bug2, bug1)
        if((key in all_data1.keys())or(key2 in all_data1.keys())):
            if(isDuplicate==1):
                duplicate_trueduplicatepair_num=duplicate_trueduplicatepair_num+1
                f1.write('%s,%s,%s\n'%(str(bug1),str(bug2),str(isDuplicate)))
                #写入文件
                continue
            if(isDuplicate==-1):
                duplicate_falseduplicatepair_num=duplicate_falseduplicatepair_num+1
                f2.write('%s,%s,%s\n'%(str(bug1),str(bug2),str(isDuplicate)))
                #写入文件
                continue
        all_data1[key] = isDuplicate  
    save_to_pkl(all_data1, all_dataset_name1)
    f1.close()
    f2.close()
    print('Eclipse的pairs集合中重复的正标签数据{}个，Eclipse的pairs集合中重复的负标签数据{}个'.format(duplicate_trueduplicatepair_num,duplicate_falseduplicatepair_num))
    print('Eclipse的pairs集合中最后标签数据集的大小为{}'.format(len(all_data1)))
#Eliminate_duplicateRecords_in_Eclipse()
    
##(4)能够依据一个报告id，查询出其摘要和描述，并且concatenated摘要和描述,然后经过标准化处理后，并输出。
def processExampleBugReport():
    bug_id="13060"
    condition={'bug_id':bug_id}
    db=client.openOffice
    bug_report=db.clear.find_one(condition)
    #print (bug_report["short_desc"])
    #print (bug_report["description"])
    testSTR=bug_report["short_desc"]+' '+bug_report["description"]
    print(testSTR)
    #分词
    import nltk
    import re
    import string
    tokens=nltk.word_tokenize(testSTR)
    print (tokens)
    #去除标点符号
    x=re.compile('[%s]'%re.escape(string.punctuation))
    new_tokens=[]
    for token in tokens:
        new_token=x.sub(u'',token)
        if not new_token==u'':
            new_tokens.append(new_token)
    print (new_tokens)
#processExampleBugReport()

##(5)划分数据集为训练集合验证集。
##由于原始数据库中的标签数据中存在重复。我们读取我们去重后的数据。
##由于使用的是LIBSVM，给入训练数据以后，可以自动进行十则交叉验证。因此，不需要另外划分验证集
##(5)_1 划分Eclipse数据集为训练集和测试集
def divideDataSet_Eclipse(ratio): #ratio为训练集的比例 设为0.8
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_Eclipse_XIAOJIE.pkl'
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_test_Eclipse_XIAOJIE.pkl'
    all_pairs = read_from_pkl(all_dataset_name1)
    all_pairs_num=len(all_pairs)
    print ("划分Eclipse训练数据")
    print ("训练数据一共{}组".format(all_pairs_num))
    all_pairs_trueTag={}
    all_pairs_falseTag={}
    for key in all_pairs.keys():
        isDuplicateReport = all_pairs[key]
        if isDuplicateReport==1:
            all_pairs_trueTag[key]=isDuplicateReport
        elif isDuplicateReport==-1:
            all_pairs_falseTag[key]=isDuplicateReport
        else:
            print ('wrong tag!')
    all_pairs_trueTag_num=len(all_pairs_trueTag)
    all_pairs_falseTag_num=len(all_pairs_falseTag)
    print ("正标签数据一共{}组".format(all_pairs_trueTag_num))
    print ("负标签数据一共{}组".format(all_pairs_falseTag_num))
    
    ###按指定比例划分正标签数据。
    print ("正标签训练数据占比{}".format(ratio))
    train_true_num=(int)(all_pairs_trueTag_num*ratio)
    test_true_num=all_pairs_trueTag_num-train_true_num
    
    print (train_true_num)
    print (test_true_num)
    
    all_pairs_trueTag_forTrain_keys=random.sample(all_pairs_trueTag.keys(), train_true_num)
    all_pairs_trueTag_forTrain={}
    for key in all_pairs_trueTag_forTrain_keys:
        all_pairs_trueTag_forTrain[key]=all_pairs_trueTag[key]
        del all_pairs_trueTag[key]
    
    all_pairs_trueTag_forTest={}
    for key in all_pairs_trueTag:
        all_pairs_trueTag_forTest[key]=all_pairs_trueTag[key]
    del(all_pairs_trueTag)
    
    print ("正标签训练数据{}组".format(len(all_pairs_trueTag_forTrain)))
    print ("正标签测试数据{}组".format(len(all_pairs_trueTag_forTest)))
    
    ###按指定比例划分负标签数据。
    print ("负标签训练数据占比{}".format(ratio))
    train_false_num=(int)(all_pairs_falseTag_num*ratio)
    test_false_num=all_pairs_falseTag_num-train_false_num
    
    print (train_false_num)
    print (test_false_num)
    
    all_pairs_falseTag_forTrain_keys=random.sample(all_pairs_falseTag.keys(), train_false_num)
    all_pairs_falseTag_forTrain={}
    for key in all_pairs_falseTag_forTrain_keys:
        all_pairs_falseTag_forTrain[key]=all_pairs_falseTag[key]
        del all_pairs_falseTag[key]
    
    all_pairs_falseTag_forTest={}
    for key in all_pairs_falseTag:
        all_pairs_falseTag_forTest[key]=all_pairs_falseTag[key]
    del(all_pairs_falseTag)
    
    print ("负标签训练数据{}组".format(len(all_pairs_falseTag_forTrain)))
    print ("负标签测试数据{}组".format(len(all_pairs_falseTag_forTest)))
    
    ##将正标签训练数据与负标签训练数据拼接为训练数据文件
    all_pairs_trueTag_forTrain.update(all_pairs_falseTag_forTrain)
    all_pairs_forTrain=all_pairs_trueTag_forTrain.copy()
    del (all_pairs_falseTag_forTrain)
    del (all_pairs_trueTag_forTrain)
    print ("训练数据{}组".format(len(all_pairs_forTrain)))
    ##将正标签测试数据与负标签测试数据拼接为测试数据文件
    all_pairs_trueTag_forTest.update(all_pairs_falseTag_forTest)
    all_pairs_forTest=all_pairs_trueTag_forTest.copy()
    del (all_pairs_falseTag_forTest)
    del (all_pairs_trueTag_forTest)
    print ("测试数据{}组".format(len(all_pairs_forTest)))
    
    save_to_pkl(all_pairs_forTest, all_dataset_name1_forTest)
    save_to_pkl(all_pairs_forTrain, all_dataset_name1_forTrain)
#divideDataSet_Eclipse(ratio=0.8)
    
def divideDataSet_Eclipse_2(trainset_num,ratio_TrueFlag,ratio_FalseFlag): #直接传入训练集的总样本数目和其中的正标签数据与负标签数据的比例是ratio_TrueFlag：ratio_FalseFlag
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_Eclipse_XIAOJIE.pkl'
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    all_pairs = read_from_pkl(all_dataset_name1)
    all_pairs_num=len(all_pairs)
    print ("划分Eclipse训练数据")
    print ("训练数据一共{}组".format(all_pairs_num))
    all_pairs_trueTag={}
    all_pairs_falseTag={}
    for key in all_pairs.keys():
        isDuplicateReport = all_pairs[key]
        if isDuplicateReport==1:
            all_pairs_trueTag[key]=isDuplicateReport
        elif isDuplicateReport==-1:
            all_pairs_falseTag[key]=isDuplicateReport
        else:
            print ('wrong tag!')
    all_pairs_trueTag_num=len(all_pairs_trueTag)
    all_pairs_falseTag_num=len(all_pairs_falseTag)
    print ("正标签数据一共{}组".format(all_pairs_trueTag_num))
    print ("负标签数据一共{}组".format(all_pairs_falseTag_num))
    
    ###按指定比例划分正标签数据。
    print ("需要抽取训练数据{}，其中正标签与负标签的比例是{}:{}".format(trainset_num,ratio_TrueFlag,ratio_FalseFlag))
    ratio=ratio_TrueFlag/(ratio_TrueFlag+ratio_FalseFlag)
    train_true_num=(int)(trainset_num*ratio)
    train_false_num=trainset_num-train_true_num
    print (train_true_num)
    print (train_false_num)
    
    all_pairs_trueTag_forTrain_keys=random.sample(all_pairs_trueTag.keys(), train_true_num)#从正标签数据中抽取出train_true_num个样本
    all_pairs_trueTag_forTrain={}
    for key in all_pairs_trueTag_forTrain_keys:
        all_pairs_trueTag_forTrain[key]=all_pairs_trueTag[key]
        del all_pairs_trueTag[key]
    
    
    all_pairs_falseTag_forTrain_keys=random.sample(all_pairs_falseTag.keys(), train_false_num)#从正标签数据中抽取出train_true_num个样本
    all_pairs_falseTag_forTrain={}
    for key in all_pairs_falseTag_forTrain_keys:
        all_pairs_falseTag_forTrain[key]=all_pairs_falseTag[key]
        del all_pairs_falseTag[key]
    
    ###上面的过程分别从正标签数据和负标签数据中抽样出一定数目的数据。
    ###将余下的数据集全部归入测试集
    all_pairs_forTest={}
    for key in all_pairs_trueTag:
        all_pairs_forTest[key]=all_pairs_trueTag[key]
    del(all_pairs_trueTag)
    for key in all_pairs_falseTag:
        all_pairs_forTest[key]=all_pairs_falseTag[key]
    del(all_pairs_falseTag)
    
    print ("训练数据中正标签{}组".format(len(all_pairs_trueTag_forTrain)))
    print ("训练数据中负标签{}组".format(len(all_pairs_falseTag_forTrain)))
    ##将正标签训练数据与负标签训练数据拼接为训练数据文件
    all_pairs_trueTag_forTrain.update(all_pairs_falseTag_forTrain)
    all_pairs_forTrain=all_pairs_trueTag_forTrain.copy()
    del (all_pairs_falseTag_forTrain)
    del (all_pairs_trueTag_forTrain)
    print ("训练数据{}组".format(len(all_pairs_forTrain)))
    print ("测试数据{}组".format(len(all_pairs_forTest)))
    save_to_pkl(all_pairs_forTest, all_dataset_name1_forTest)
    save_to_pkl(all_pairs_forTrain, all_dataset_name1_forTrain)
#divideDataSet_Eclipse_2(5000, ratio_TrueFlag=1,ratio_FalseFlag=4)


##(5)_2 划分openOffice数据集为训练集和测试集
def divideDataSet_openOffice(ratio): #ratio为训练集的比例 设为0.8
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_openOffice_XIAOJIE.pkl'
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_test_openOffice_XIAOJIE.pkl'
    all_pairs = read_from_pkl(all_dataset_name1)
    all_pairs_num=len(all_pairs)
    print ("划分openOffice训练数据")
    print ("训练数据一共{}组".format(all_pairs_num))
    all_pairs_trueTag={}
    all_pairs_falseTag={}
    for key in all_pairs.keys():
        isDuplicateReport = all_pairs[key]
        if isDuplicateReport==1:
            all_pairs_trueTag[key]=isDuplicateReport
        elif isDuplicateReport==-1:
            all_pairs_falseTag[key]=isDuplicateReport
        else:
            print ('wrong tag!')
    all_pairs_trueTag_num=len(all_pairs_trueTag)
    all_pairs_falseTag_num=len(all_pairs_falseTag)
    print ("正标签数据一共{}组".format(all_pairs_trueTag_num))
    print ("负标签数据一共{}组".format(all_pairs_falseTag_num))
    
    ###按指定比例划分正标签数据。
    print ("正标签训练数据占比{}".format(ratio))
    train_true_num=(int)(all_pairs_trueTag_num*ratio)
    test_true_num=all_pairs_trueTag_num-train_true_num
    
    print (train_true_num)
    print (test_true_num)
    
    all_pairs_trueTag_forTrain_keys=random.sample(all_pairs_trueTag.keys(), train_true_num)
    all_pairs_trueTag_forTrain={}
    for key in all_pairs_trueTag_forTrain_keys:
        all_pairs_trueTag_forTrain[key]=all_pairs_trueTag[key]
        del all_pairs_trueTag[key]
    
    all_pairs_trueTag_forTest={}
    for key in all_pairs_trueTag:
        all_pairs_trueTag_forTest[key]=all_pairs_trueTag[key]
    del(all_pairs_trueTag)
    
    print ("正标签训练数据{}组".format(len(all_pairs_trueTag_forTrain)))
    print ("正标签测试数据{}组".format(len(all_pairs_trueTag_forTest)))
    
    ###按指定比例划分负标签数据。
    print ("负标签训练数据占比{}".format(ratio))
    train_false_num=(int)(all_pairs_falseTag_num*ratio)
    test_false_num=all_pairs_falseTag_num-train_false_num
    
    print (train_false_num)
    print (test_false_num)
    
    all_pairs_falseTag_forTrain_keys=random.sample(all_pairs_falseTag.keys(), train_false_num)
    all_pairs_falseTag_forTrain={}
    for key in all_pairs_falseTag_forTrain_keys:
        all_pairs_falseTag_forTrain[key]=all_pairs_falseTag[key]
        del all_pairs_falseTag[key]
    
    all_pairs_falseTag_forTest={}
    for key in all_pairs_falseTag:
        all_pairs_falseTag_forTest[key]=all_pairs_falseTag[key]
    del(all_pairs_falseTag)
    
    print ("负标签训练数据{}组".format(len(all_pairs_falseTag_forTrain)))
    print ("负标签测试数据{}组".format(len(all_pairs_falseTag_forTest)))
    
    ##将正标签训练数据与负标签训练数据拼接为训练数据文件
    all_pairs_trueTag_forTrain.update(all_pairs_falseTag_forTrain)
    all_pairs_forTrain=all_pairs_trueTag_forTrain.copy()
    del (all_pairs_falseTag_forTrain)
    del (all_pairs_trueTag_forTrain)
    print ("训练数据{}组".format(len(all_pairs_forTrain)))
    ##将正标签测试数据与负标签测试数据拼接为测试数据文件
    all_pairs_trueTag_forTest.update(all_pairs_falseTag_forTest)
    all_pairs_forTest=all_pairs_trueTag_forTest.copy()
    del (all_pairs_falseTag_forTest)
    del (all_pairs_trueTag_forTest)
    print ("测试数据{}组".format(len(all_pairs_forTest)))
    
    save_to_pkl(all_pairs_forTest, all_dataset_name1_forTest)
    save_to_pkl(all_pairs_forTrain, all_dataset_name1_forTrain)
#divideDataSet_openOffice(ratio=0.8)

def divideDataSet_openOffice_2(trainset_num,ratio_TrueFlag,ratio_FalseFlag): #直接传入训练集的总样本数目和其中的正标签数据与负标签数据的比例是ratio_TrueFlag：ratio_FalseFlag
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_openOffice_XIAOJIE.pkl'
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    all_pairs = read_from_pkl(all_dataset_name1)
    all_pairs_num=len(all_pairs)
    print ("划分openOffice训练数据")
    print ("训练数据一共{}组".format(all_pairs_num))
    all_pairs_trueTag={}
    all_pairs_falseTag={}
    for key in all_pairs.keys():
        isDuplicateReport = all_pairs[key]
        if isDuplicateReport==1:
            all_pairs_trueTag[key]=isDuplicateReport
        elif isDuplicateReport==-1:
            all_pairs_falseTag[key]=isDuplicateReport
        else:
            print ('wrong tag!')
    all_pairs_trueTag_num=len(all_pairs_trueTag)
    all_pairs_falseTag_num=len(all_pairs_falseTag)
    print ("正标签数据一共{}组".format(all_pairs_trueTag_num))
    print ("负标签数据一共{}组".format(all_pairs_falseTag_num))
    
    ###按指定比例划分正标签数据。
    print ("需要抽取训练数据{}，其中正标签与负标签的比例是{}:{}".format(trainset_num,ratio_TrueFlag,ratio_FalseFlag))
    ratio=ratio_TrueFlag/(ratio_TrueFlag+ratio_FalseFlag)
    train_true_num=(int)(trainset_num*ratio)
    train_false_num=trainset_num-train_true_num
    print (train_true_num)
    print (train_false_num)
    
    all_pairs_trueTag_forTrain_keys=random.sample(all_pairs_trueTag.keys(), train_true_num)#从正标签数据中抽取出train_true_num个样本
    all_pairs_trueTag_forTrain={}
    for key in all_pairs_trueTag_forTrain_keys:
        all_pairs_trueTag_forTrain[key]=all_pairs_trueTag[key]
        del all_pairs_trueTag[key]
    
    
    all_pairs_falseTag_forTrain_keys=random.sample(all_pairs_falseTag.keys(), train_false_num)#从正标签数据中抽取出train_true_num个样本
    all_pairs_falseTag_forTrain={}
    for key in all_pairs_falseTag_forTrain_keys:
        all_pairs_falseTag_forTrain[key]=all_pairs_falseTag[key]
        del all_pairs_falseTag[key]
    
    ###上面的过程分别从正标签数据和负标签数据中抽样出一定数目的数据。
    ###将余下的数据集全部归入测试集
    all_pairs_forTest={}
    for key in all_pairs_trueTag:
        all_pairs_forTest[key]=all_pairs_trueTag[key]
    del(all_pairs_trueTag)
    for key in all_pairs_falseTag:
        all_pairs_forTest[key]=all_pairs_falseTag[key]
    del(all_pairs_falseTag)
    
    print ("训练数据中正标签{}组".format(len(all_pairs_trueTag_forTrain)))
    print ("训练数据中负标签{}组".format(len(all_pairs_falseTag_forTrain)))
    ##将正标签训练数据与负标签训练数据拼接为训练数据文件
    all_pairs_trueTag_forTrain.update(all_pairs_falseTag_forTrain)
    all_pairs_forTrain=all_pairs_trueTag_forTrain.copy()
    del (all_pairs_falseTag_forTrain)
    del (all_pairs_trueTag_forTrain)
    print ("训练数据{}组".format(len(all_pairs_forTrain)))
    print ("测试数据{}组".format(len(all_pairs_forTest)))
    save_to_pkl(all_pairs_forTest, all_dataset_name1_forTest)
    save_to_pkl(all_pairs_forTrain, all_dataset_name1_forTrain)
#divideDataSet_openOffice_2(5000, ratio_TrueFlag=1,ratio_FalseFlag=4)

##(5)_3 划分netBeans数据集为训练集和测试集
def divideDataSet_netBeans(ratio): #ratio为训练集的比例 设为0.8
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_netBeans_XIAOJIE.pkl'
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_test_netBeans_XIAOJIE.pkl'
    all_pairs = read_from_pkl(all_dataset_name1)
    all_pairs_num=len(all_pairs)
    print ("划分netBeans训练数据")
    print ("训练数据一共{}组".format(all_pairs_num))
    all_pairs_trueTag={}
    all_pairs_falseTag={}
    for key in all_pairs.keys():
        isDuplicateReport = all_pairs[key]
        if isDuplicateReport==1:
            all_pairs_trueTag[key]=isDuplicateReport
        elif isDuplicateReport==-1:
            all_pairs_falseTag[key]=isDuplicateReport
        else:
            print ('wrong tag!')
    all_pairs_trueTag_num=len(all_pairs_trueTag)
    all_pairs_falseTag_num=len(all_pairs_falseTag)
    print ("正标签数据一共{}组".format(all_pairs_trueTag_num))
    print ("负标签数据一共{}组".format(all_pairs_falseTag_num))
    
    ###按指定比例划分正标签数据。
    print ("正标签训练数据占比{}".format(ratio))
    train_true_num=(int)(all_pairs_trueTag_num*ratio)
    test_true_num=all_pairs_trueTag_num-train_true_num
    
    print (train_true_num)
    print (test_true_num)
    
    all_pairs_trueTag_forTrain_keys=random.sample(all_pairs_trueTag.keys(), train_true_num)
    all_pairs_trueTag_forTrain={}
    for key in all_pairs_trueTag_forTrain_keys:
        all_pairs_trueTag_forTrain[key]=all_pairs_trueTag[key]
        del all_pairs_trueTag[key]
    
    all_pairs_trueTag_forTest={}
    for key in all_pairs_trueTag:
        all_pairs_trueTag_forTest[key]=all_pairs_trueTag[key]
    del(all_pairs_trueTag)
    
    print ("正标签训练数据{}组".format(len(all_pairs_trueTag_forTrain)))
    print ("正标签测试数据{}组".format(len(all_pairs_trueTag_forTest)))
    
    ###按指定比例划分负标签数据。
    print ("负标签训练数据占比{}".format(ratio))
    train_false_num=(int)(all_pairs_falseTag_num*ratio)
    test_false_num=all_pairs_falseTag_num-train_false_num
    
    print (train_false_num)
    print (test_false_num)
    
    all_pairs_falseTag_forTrain_keys=random.sample(all_pairs_falseTag.keys(), train_false_num)
    all_pairs_falseTag_forTrain={}
    for key in all_pairs_falseTag_forTrain_keys:
        all_pairs_falseTag_forTrain[key]=all_pairs_falseTag[key]
        del all_pairs_falseTag[key]
    
    all_pairs_falseTag_forTest={}
    for key in all_pairs_falseTag:
        all_pairs_falseTag_forTest[key]=all_pairs_falseTag[key]
    del(all_pairs_falseTag)
    
    print ("负标签训练数据{}组".format(len(all_pairs_falseTag_forTrain)))
    print ("负标签测试数据{}组".format(len(all_pairs_falseTag_forTest)))
    
    ##将正标签训练数据与负标签训练数据拼接为训练数据文件
    all_pairs_trueTag_forTrain.update(all_pairs_falseTag_forTrain)
    all_pairs_forTrain=all_pairs_trueTag_forTrain.copy()
    del (all_pairs_falseTag_forTrain)
    del (all_pairs_trueTag_forTrain)
    print ("训练数据{}组".format(len(all_pairs_forTrain)))
    ##将正标签测试数据与负标签测试数据拼接为测试数据文件
    all_pairs_trueTag_forTest.update(all_pairs_falseTag_forTest)
    all_pairs_forTest=all_pairs_trueTag_forTest.copy()
    del (all_pairs_falseTag_forTest)
    del (all_pairs_trueTag_forTest)
    print ("测试数据{}组".format(len(all_pairs_forTest)))
    
    save_to_pkl(all_pairs_forTest, all_dataset_name1_forTest)
    save_to_pkl(all_pairs_forTrain, all_dataset_name1_forTrain)
#divideDataSet_netBeans(ratio=0.8)  

def divideDataSet_netBeans_2(trainset_num,ratio_TrueFlag,ratio_FalseFlag): #直接传入训练集的总样本数目和其中的正标签数据与负标签数据的比例是ratio_TrueFlag：ratio_FalseFlag
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_netBeans_XIAOJIE.pkl'
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    all_pairs = read_from_pkl(all_dataset_name1)
    all_pairs_num=len(all_pairs)
    print ("划分netBeans训练数据")
    print ("训练数据一共{}组".format(all_pairs_num))
    all_pairs_trueTag={}
    all_pairs_falseTag={}
    for key in all_pairs.keys():
        isDuplicateReport = all_pairs[key]
        if isDuplicateReport==1:
            all_pairs_trueTag[key]=isDuplicateReport
        elif isDuplicateReport==-1:
            all_pairs_falseTag[key]=isDuplicateReport
        else:
            print ('wrong tag!')
    all_pairs_trueTag_num=len(all_pairs_trueTag)
    all_pairs_falseTag_num=len(all_pairs_falseTag)
    print ("正标签数据一共{}组".format(all_pairs_trueTag_num))
    print ("负标签数据一共{}组".format(all_pairs_falseTag_num))
    
    ###按指定比例划分正标签数据。
    print ("需要抽取训练数据{}，其中正标签与负标签的比例是{}:{}".format(trainset_num,ratio_TrueFlag,ratio_FalseFlag))
    ratio=ratio_TrueFlag/(ratio_TrueFlag+ratio_FalseFlag)
    train_true_num=(int)(trainset_num*ratio)
    train_false_num=trainset_num-train_true_num
    print (train_true_num)
    print (train_false_num)
    
    all_pairs_trueTag_forTrain_keys=random.sample(all_pairs_trueTag.keys(), train_true_num)#从正标签数据中抽取出train_true_num个样本
    all_pairs_trueTag_forTrain={}
    for key in all_pairs_trueTag_forTrain_keys:
        all_pairs_trueTag_forTrain[key]=all_pairs_trueTag[key]
        del all_pairs_trueTag[key]
    
    
    all_pairs_falseTag_forTrain_keys=random.sample(all_pairs_falseTag.keys(), train_false_num)#从正标签数据中抽取出train_true_num个样本
    all_pairs_falseTag_forTrain={}
    for key in all_pairs_falseTag_forTrain_keys:
        all_pairs_falseTag_forTrain[key]=all_pairs_falseTag[key]
        del all_pairs_falseTag[key]
    
    ###上面的过程分别从正标签数据和负标签数据中抽样出一定数目的数据。
    ###将余下的数据集全部归入测试集
    all_pairs_forTest={}
    for key in all_pairs_trueTag:
        all_pairs_forTest[key]=all_pairs_trueTag[key]
    del(all_pairs_trueTag)
    for key in all_pairs_falseTag:
        all_pairs_forTest[key]=all_pairs_falseTag[key]
    del(all_pairs_falseTag)
    
    print ("训练数据中正标签{}组".format(len(all_pairs_trueTag_forTrain)))
    print ("训练数据中负标签{}组".format(len(all_pairs_falseTag_forTrain)))
    ##将正标签训练数据与负标签训练数据拼接为训练数据文件
    all_pairs_trueTag_forTrain.update(all_pairs_falseTag_forTrain)
    all_pairs_forTrain=all_pairs_trueTag_forTrain.copy()
    del (all_pairs_falseTag_forTrain)
    del (all_pairs_trueTag_forTrain)
    print ("训练数据{}组".format(len(all_pairs_forTrain)))
    print ("测试数据{}组".format(len(all_pairs_forTest)))
    save_to_pkl(all_pairs_forTest, all_dataset_name1_forTest)
    save_to_pkl(all_pairs_forTrain, all_dataset_name1_forTrain)
#divideDataSet_netBeans_2(5000, ratio_TrueFlag=1,ratio_FalseFlag=4)


##(6)处理训练集和验证集，并且生成TakeLab需要的格式。
import nltk
import re
import string
###(6)_1处理eclipse数据
def generateTakeLabText_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
                                                                                                       
    txtTrain_forTakeLab_path='./processedData_2014MSR_xiaojie/textForTakeLab_to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    txtTest_forTakeLab_path='./processedData_2014MSR_xiaojie/textForTakeLab_to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    ###先处理训练数据
    print ("先处理训练数据")
    all_pairs_forTrain=read_from_pkl(all_dataset_name1_forTrain)
    db=client.eclipse
    f1 = open(txtTrain_forTakeLab_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTrain.keys():
        if (index%100==0):
            print ("index:",index)

        bug1=str(key[0])
        bug2=str(key[1])
        index=index+1
#        print (index)

#        print(bug1)
#        print(bug2)
#        ###测试用 当处理某个pair出现错误的时候
#        bug1="33824"
#        bug2="33989"
        #从数据库中取出第一个bug report
        condition={'bug_id':bug1}
        bug_report=db.clear.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        if(bug_report["short_desc"]==[]):
            short_desc=''
        else:
            short_desc=bug_report["short_desc"]
        if(bug_report["description"]==[]):
            description=''
        else:
            description=bug_report["description"]
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence1 = ' '.join(new_tokens)
        sentence1 = sentence1+'.'
        
        #从数据库中取出第二个bug report
        condition={'bug_id':bug2}
        bug_report=db.clear.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        if(bug_report["short_desc"]==[]):
            short_desc=''
        else:
            short_desc=bug_report["short_desc"]
        if(bug_report["description"]==[]):
            description=''
        else:
            description=bug_report["description"]
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence2 = ' '.join(new_tokens)
        sentence2 = sentence2+'.'
#        print(bug1)
#        print(bug2) 
#        print(sentence1)
#        print(sentence2)
        sentence = sentence1+'\t'+sentence2
#        print(sentence)
        f1.write(sentence)
        f1.write('\n')
        f1.flush()
        pass
    ###再处理测试数据
    print ("再处理测试数据")
    all_pairs_forTest=read_from_pkl(all_dataset_name1_forTest)
    f2 = open(txtTest_forTakeLab_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTest.keys():
        
        if (index%100==0):
            print ("index:",index)
        bug1=str(key[0])
        bug2=str(key[1])
        index=index+1
        #从数据库中取出第一个bug report
        condition={'bug_id':bug1}
        bug_report=db.clear.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        if(bug_report["short_desc"]==[]):
            short_desc=''
        else:
            short_desc=bug_report["short_desc"]
        if(bug_report["description"]==[]):
            description=''
        else:
            description=bug_report["description"]
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence1 = ' '.join(new_tokens)
        sentence1 = sentence1+'.'
        
        #从数据库中取出第二个bug report
        condition={'bug_id':bug2}
        bug_report=db.clear.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        if(bug_report["short_desc"]==[]):
            short_desc=''
        else:
            short_desc=bug_report["short_desc"]
        if(bug_report["description"]==[]):
            description=''
        else:
            description=bug_report["description"]
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence2 = ' '.join(new_tokens)
        sentence2 = sentence2+'.'
#            print(bug1)
#            print(bug2) 
#            print(sentence1)
#            print(sentence2)
        sentence = sentence1+'\t'+sentence2
#            print(sentence)
        f2.write(sentence)
        f2.write('\n')
        f2.flush()
        pass
#generateTakeLabText_Eclipse()

###(6)_2处理openOffice数据
def generateTakeLabText_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
                                                                                                       
    txtTrain_forTakeLab_path='./processedData_2014MSR_xiaojie/textForTakeLab_to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    txtTest_forTakeLab_path='./processedData_2014MSR_xiaojie/textForTakeLab_to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    ###先处理训练数据
    print ("先处理训练数据")
    all_pairs_forTrain=read_from_pkl(all_dataset_name1_forTrain)
    db=client.openOffice
    f1 = open(txtTrain_forTakeLab_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTrain.keys():
        
        if (index%100==0):
            print ("index:",index)
        bug1=str(key[0])
        bug2=str(key[1])
        index=index+1
#        print(bug1)
#        print(bug2)
#        ###测试用 当处理某个pair出现错误的时候
#        bug1="33824"
#        bug2="33989"
        #从数据库中取出第一个bug report
        condition={'bug_id':bug1}
        bug_report=db.clear.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        if(bug_report["short_desc"]==[]):
            short_desc=''
        else:
            short_desc=bug_report["short_desc"]
        if(bug_report["description"]==[]):
            description=''
        else:
            description=bug_report["description"]
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence1 = ' '.join(new_tokens)
        sentence1 = sentence1+'.'
        
        #从数据库中取出第二个bug report
        condition={'bug_id':bug2}
        bug_report=db.clear.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        if(bug_report["short_desc"]==[]):
            short_desc=''
        else:
            short_desc=bug_report["short_desc"]
        if(bug_report["description"]==[]):
            description=''
        else:
            description=bug_report["description"]
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence2 = ' '.join(new_tokens)
        sentence2 = sentence2+'.'
#        print(bug1)
#        print(bug2) 
#        print(sentence1)
#        print(sentence2)
        sentence = sentence1+'\t'+sentence2
#        print(sentence)
        f1.write(sentence)
        f1.write('\n')
        f1.flush()
        pass
    ###再处理测试数据
    print ("再处理测试数据")
    all_pairs_forTest=read_from_pkl(all_dataset_name1_forTest)
    f2 = open(txtTest_forTakeLab_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTest.keys():
        
        if (index%100==0):
            print ("index:",index)
        bug1=str(key[0])
        bug2=str(key[1])
        index=index+1
        #从数据库中取出第一个bug report
        condition={'bug_id':bug1}
        bug_report=db.clear.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        if(bug_report["short_desc"]==[]):
            short_desc=''
        else:
            short_desc=bug_report["short_desc"]
        if(bug_report["description"]==[]):
            description=''
        else:
            description=bug_report["description"]
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence1 = ' '.join(new_tokens)
        sentence1 = sentence1+'.'
        
        #从数据库中取出第二个bug report
        condition={'bug_id':bug2}
        bug_report=db.clear.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        if(bug_report["short_desc"]==[]):
            short_desc=''
        else:
            short_desc=bug_report["short_desc"]
        if(bug_report["description"]==[]):
            description=''
        else:
            description=bug_report["description"]
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence2 = ' '.join(new_tokens)
        sentence2 = sentence2+'.'
#            print(bug1)
#            print(bug2) 
#            print(sentence1)
#            print(sentence2)
        sentence = sentence1+'\t'+sentence2
#            print(sentence)
        f2.write(sentence)
        f2.write('\n')
        f2.flush()
        pass
#generateTakeLabText_openOffice()



###(6)_3处理netBeans数据
def generateTakeLabText_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
                                                                                                       
    txtTrain_forTakeLab_path='./processedData_2014MSR_xiaojie/textForTakeLab_to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    txtTest_forTakeLab_path='./processedData_2014MSR_xiaojie/textForTakeLab_to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    
    ###先处理训练数据
    print ("先处理训练数据")
    all_pairs_forTrain=read_from_pkl(all_dataset_name1_forTrain)
    print (len(all_pairs_forTrain))
    db=client.netBeans
    f1 = open(txtTrain_forTakeLab_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTrain.keys():
        
        if (index%100==0):
            print ("index:",index)
#        if (index==4999):
#            print ("debug")
        bug1=str(key[0])
        bug2=str(key[1])
        index=index+1
#        continue
#        print(bug1)
#        print(bug2)
#        ###测试用 当处理某个pair出现错误的时候
#        bug1="3820"
#        bug2="30090"
        #从数据库中取出第一个bug report
        condition={'bug_id':bug1}
        bug_report=db.clear.find_one(condition) ##对于netbeans而言，有一些数据去clear集合中找不到。只能在initial集合中找。
        if bug_report==None:
            bug_report=db.initial.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        try:
            short_desc=bug_report["short_desc"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            short_desc=''
        if(short_desc==[]):
            short_desc=''
        try:
            description=bug_report["description"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            description=''
        if(description==[]):
            description=''

#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence1 = ' '.join(new_tokens)
        sentence1 = sentence1+'.'
        
        #从数据库中取出第二个bug report
        condition={'bug_id':bug2}
        bug_report=db.clear.find_one(condition) ##对于netbeans而言，有一些数据去clear集合中找不到。只能在initial集合中找。
        if bug_report==None:
            bug_report=db.initial.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        try:
            short_desc=bug_report["short_desc"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            short_desc=''
        if(short_desc==[]):
            short_desc=''
        try:
            description=bug_report["description"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            description=''
        if(description==[]):
            description=''
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence2 = ' '.join(new_tokens)
        sentence2 = sentence2+'.'
#        print(bug1)
#        print(bug2) 
#        print(sentence1)
#        print(sentence2)
        sentence = sentence1+'\t'+sentence2
#        print(sentence)
        if(sentence==''):
            print ('debug')
            print (index)
            
        f1.write(sentence)
        f1.write('\n')
        f1.flush()
        pass
    ###再处理测试数据
    print ("再处理测试数据")
    all_pairs_forTest=read_from_pkl(all_dataset_name1_forTest)
    print (len(all_pairs_forTest))
    f2 = open(txtTest_forTakeLab_path, 'w',encoding='UTF-8')
    index=0
    for key in all_pairs_forTest.keys():
        
        if (index%100==0):
            print ("index:",index)
        bug1=str(key[0])
        bug2=str(key[1])
        index=index+1
        #从数据库中取出第一个bug report
        condition={'bug_id':bug1}
        bug_report=db.clear.find_one(condition) ##对于netbeans而言，有一些数据去clear集合中找不到。只能在initial集合中找。
        if bug_report==None:
            bug_report=db.initial.find_one(condition)
        #print (bug_report["short_desc"])
        #print (bug_report["description"])
        try:
            short_desc=bug_report["short_desc"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            short_desc=''
        if(short_desc==[]):
            short_desc=''
        try:
            description=bug_report["description"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            description=''
        if(description==[]):
            description=''
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence1 = ' '.join(new_tokens)
        sentence1 = sentence1+'.'
        
        #从数据库中取出第二个bug report
        condition={'bug_id':bug2}
        bug_report=db.clear.find_one(condition) ##对于netbeans而言，有一些数据去clear集合中找不到。只能在initial集合中找。
        if bug_report==None:
            bug_report=db.initial.find_one(condition)
        try:
            short_desc=bug_report["short_desc"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            short_desc=''
        if(short_desc==[]):
            short_desc=''
        try:
            description=bug_report["description"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
        except KeyError:
            description=''
        if(description==[]):
            description=''
#        testSTR=bug_report["short_desc"]+' '+bug_report["description"] #注意：实际使用的时候，存在这个属性为空的情形。
        testSTR=short_desc+' '+description
        #分词
        tokens=nltk.word_tokenize(testSTR)
#        print (tokens)
        #去除标点符号
        x=re.compile('[%s]'%re.escape(string.punctuation))
        new_tokens=[]
        for token in tokens:
            new_token=x.sub(u'',token)
            if not new_token==u'':
                new_tokens.append(new_token)
#        print (new_tokens)
        #将单词列表按空格拼接起来。
        sentence2 = ' '.join(new_tokens)
        sentence2 = sentence2+'.'
#            print(bug1)
#            print(bug2) 
#            print(sentence1)
#            print(sentence2)
        sentence = sentence1+'\t'+sentence2
#            print(sentence)
        f2.write(sentence)
        f2.write('\n')
        f2.flush()
        pass
#generateTakeLabText_netBeans()
if __name__ == "__main__":
#    trainset_num_list=[5000,10000,15000,20000]
    trainset_num_list=[5000]
    ratio_TrueFlag=1
    ratio_FalseFlag=4
    for trainset_num in trainset_num_list:
#        print (trainset_num)
        ##采样训练数据
#        divideDataSet_Eclipse_2(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        divideDataSet_openOffice_2(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        divideDataSet_netBeans_2(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        ##生成Takelab能够处理的文本
        generateTakeLabText_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        generateTakeLabText_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        generateTakeLabText_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag)