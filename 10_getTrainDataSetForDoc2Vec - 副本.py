###第一步：读出所有的pairs对。然后建立映射关系。同时将其生成的文本写入到文件中去。
###输出文件格式：
#eclipse_bug_id_Map_lineNumber.pkl #lineNumber就是eclipse_text_for_trainingDoc2Vec.txt中的行号，属于从0开始编号。其余项目类似
#netBeans_bug_id_Map_lineNumber.pkl
#oppenOffice_bug_id_Map_lineNumber.pkl
#eclipse_text_for_trainingDoc2Vec.txt
#netBeans_text_for_trainingDoc2Vec.txt
#oppenOffice_text_for_trainingDoc2Vec.txt


import pickle
import numpy as np
import os
import random
import pymongo
import nltk
import re
import string
class MyMongo:
    def init(self):
        self.client=pymongo.MongoClient(host='localhost',port=27017)
client=pymongo.MongoClient(host='localhost',port=27017)

def save_to_pkl(python_content, pickle_name):
    with open(pickle_name, 'wb') as pickle_f:
        pickle.dump(python_content, pickle_f)
def read_from_pkl(pickle_name):
    with open(pickle_name, 'rb') as pickle_f:
        python_content = pickle.load(pickle_f)
    return python_content

def getText(bug_id,db):#从数据库中取出文本
    condition={'bug_id':bug_id}
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
    sentence1 = ' '.join(new_tokens)
    return sentence1

def getTrainDataSetForDoc2Vec_eclipse():
    bug_id_Map_lineNumber_dict={}
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_Eclipse_XIAOJIE.pkl'
    text_for_trainingDoc2Vec='./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/eclipse_text_for_trainingDoc2Vec.txt'
    bug_id_Map_lineNumber_pkl='./processedData_2014MSR_xiaojie/bug_id_Map_lineNumber_pkl/eclipse_bug_id_Map_lineNumber.pkl'
    db=client.eclipse
    all_pairs = read_from_pkl(all_dataset_name1)
    lineNumber=0
    f1 = open(text_for_trainingDoc2Vec, 'w',encoding='UTF-8')
    for key in all_pairs.keys():
        #测试用
#        print (lineNumber)
#        if(lineNumber==10):
#            break
        #测试用
        if (lineNumber %1000 ==0):
            print ('eclipse lineNumber {}:'.format(lineNumber))
        bug1=key[0]
        bug2=key[1]
        #先判断是否在字典中。
        if bug1 in bug_id_Map_lineNumber_dict.keys():
            pass
        else:
            bug_id_Map_lineNumber_dict[bug1]=lineNumber
            lineNumber=lineNumber+1
            ###同时将文本数据写入到文本中去。
            sentence1=getText(str(bug1),db)
            f1.write(sentence1)
            f1.write('\n')
            f1.flush()
            
        if bug2 in bug_id_Map_lineNumber_dict.keys():
            pass
        else:
            bug_id_Map_lineNumber_dict[bug2]=lineNumber
            lineNumber=lineNumber+1
            sentence2=getText(str(bug2),db)
            ###同时将文本数据写入到文本中去。
            f1.write(sentence2)
            f1.write('\n')
            f1.flush()
    print ('eclipse lines={}:'.format(lineNumber))
    save_to_pkl(bug_id_Map_lineNumber_dict, bug_id_Map_lineNumber_pkl)

def getTrainDataSetForDoc2Vec_netBeans():
    bug_id_Map_lineNumber_dict={}
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_netBeans_XIAOJIE.pkl'
    text_for_trainingDoc2Vec='./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/netBeans_text_for_trainingDoc2Vec.txt'
    bug_id_Map_lineNumber_pkl='./processedData_2014MSR_xiaojie/bug_id_Map_lineNumber_pkl/netBeans_bug_id_Map_lineNumber.pkl'
    db=client.netBeans
    all_pairs = read_from_pkl(all_dataset_name1)
    lineNumber=0
    f1 = open(text_for_trainingDoc2Vec, 'w',encoding='UTF-8')
    for key in all_pairs.keys():
        if (lineNumber %1000 ==0):
            print ('netBeans lineNumber {}:'.format(lineNumber))
        bug1=key[0]
        bug2=key[1]
        #先判断是否在字典中。
        if bug1 in bug_id_Map_lineNumber_dict.keys():
            pass
        else:
            bug_id_Map_lineNumber_dict[bug1]=lineNumber
            lineNumber=lineNumber+1
            ###同时将文本数据写入到文本中去。
            sentence1=getText(str(bug1),db)
            f1.write(sentence1)
            f1.write('\n')
            f1.flush()
            
        if bug2 in bug_id_Map_lineNumber_dict.keys():
            pass
        else:
            bug_id_Map_lineNumber_dict[bug2]=lineNumber
            lineNumber=lineNumber+1
            sentence2=getText(str(bug2),db)
            ###同时将文本数据写入到文本中去。
            f1.write(sentence2)
            f1.write('\n')
            f1.flush()
    print ('netBeans lines={}:'.format(lineNumber))
    save_to_pkl(bug_id_Map_lineNumber_dict, bug_id_Map_lineNumber_pkl)
    
def getTrainDataSetForDoc2Vec_openOffice():
    bug_id_Map_lineNumber_dict={}
    all_dataset_name1 = './processedData_2014MSR_xiaojie/all_pairs_id_openOffice_XIAOJIE.pkl'
    text_for_trainingDoc2Vec='./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/openOffice_text_for_trainingDoc2Vec.txt'
    bug_id_Map_lineNumber_pkl='./processedData_2014MSR_xiaojie/bug_id_Map_lineNumber_pkl/openOffice_bug_id_Map_lineNumber.pkl'
    db=client.openOffice
    all_pairs = read_from_pkl(all_dataset_name1)
    lineNumber=0
    f1 = open(text_for_trainingDoc2Vec, 'w',encoding='UTF-8')
    for key in all_pairs.keys():
        if (lineNumber %1000 ==0):
            print ('openOffice lineNumber {}:'.format(lineNumber))
        bug1=key[0]
        bug2=key[1]
        #先判断是否在字典中。
        if bug1 in bug_id_Map_lineNumber_dict.keys():
            pass
        else:
            bug_id_Map_lineNumber_dict[bug1]=lineNumber
            lineNumber=lineNumber+1
            ###同时将文本数据写入到文本中去。
            sentence1=getText(str(bug1),db)
            f1.write(sentence1)
            f1.write('\n')
            f1.flush()
            
        if bug2 in bug_id_Map_lineNumber_dict.keys():
            pass
        else:
            bug_id_Map_lineNumber_dict[bug2]=lineNumber
            lineNumber=lineNumber+1
            sentence2=getText(str(bug2),db)
            ###同时将文本数据写入到文本中去。
            f1.write(sentence2)
            f1.write('\n')
            f1.flush()
    print ('openOffice lines={}:'.format(lineNumber))
    save_to_pkl(bug_id_Map_lineNumber_dict, bug_id_Map_lineNumber_pkl)
if __name__ == "__main__":
#    getTrainDataSetForDoc2Vec_eclipse()
    getTrainDataSetForDoc2Vec_netBeans()
#    getTrainDataSetForDoc2Vec_openOffice()