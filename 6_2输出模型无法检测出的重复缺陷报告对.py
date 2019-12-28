# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:39:15 2019

@author: Administrator
"""
import pickle
from sklearn.metrics import classification_report
def save_to_pkl(python_content, pickle_name):
    with open(pickle_name, 'wb') as pickle_f:
        pickle.dump(python_content, pickle_f)
def read_from_pkl(pickle_name):
    with open(pickle_name, 'rb') as pickle_f:
        python_content = pickle.load(pickle_f)
    return python_content


import pymongo
class MyMongo:
    def init(self):
        self.client=pymongo.MongoClient(host='localhost',port=27017)
client=pymongo.MongoClient(host='localhost',port=27017)
###读入模型预测后的结果文件
###读入被预测数据集的标签文件
###逐行比对，记录行号。有两种情况。
###第一种情况：真实标签为1，被预测为-1，表示真实为重复缺陷报告对，却被预测为非负缺陷报告对。将这种的行号放入列表中。
###第二种情况：真实标签为-1，被预测为1，表示真实为非重复缺陷报告对，却被预测为重复缺陷报告对。将这种的行号放入列表。
###如果被预测数据集是训练集或者测试集，则直接定位到对应的pkl中，即可找到原始的id号，再查询数据库，即可输出详细信息。
###如果是complete数据集，则判定行号是否小于等于trainset_num（行号从1开始编号），如果是，则去train的pkl中寻找。如果超过了，则减去trainset_num，再去test的pkl中寻找。
###根据上面的设定，确定函数的参数为:训练用数据集名称，被测试数据集名称，被测试数据集对应项目的训练集的pkl，被测试数据集对应项目的测试集的pkl，被测试数据集是train、test、还是complete
####根据pair的id号，访问数据库，并且将信息写入文件。
def writeBugInformation(bug1,bug2,db,f_write):
    f_write.write('bug1 信息\n')
    condition={'bug_id':bug1}
    bug_report1=db.clear.find_one(condition) ##，有一些数据去clear集合中找不到。只能在initial集合中找。
    if bug_report1==None:
        bug_report1=db.initial.find_one(condition)
    condition2={'bug_id':bug2}
    bug_report2=db.clear.find_one(condition2)
    if bug_report2==None:
        bug_report2=db.initial.find_one(condition2)
    ###(1)product信息
    try:
        product1=bug_report1["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        product1=''
    try:
        product2=bug_report2["product"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        product2=''
    f_write.write('bug1_product:{} <--> bug2_product:{} \n'.format(product1,product2))
    ###(2)component信息
    try:
        component1=bug_report1["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        component1=''
    try:
        component2=bug_report2["component"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        component2=''
    f_write.write('bug1_component:{} <--> bug2_component:{} \n'.format(component1,component2))

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
    f_write.write('bug1_priority:{} <--> bug2_priority:{} \n'.format(priority1,priority2))
    #（5）版本号的数据。这个版本号有3.x这种，也有2.2.1这种。我们直接取前两位。
    try:
        version1=bug_report1["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        version1=''
    try:
        version2=bug_report2["version"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        version2=''
    f_write.write('bug1_version:{} <--> bug2_version:{} \n'.format(version1,version2))
        
    #（6）日期 date
    try:
        date1=bug_report1["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        date1=''
    try:
        date2=bug_report2["creation_ts"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        date2=''
    f_write.write('bug1_date:{} <--> bug2_date:{} \n'.format(date1,date2))
    
    ###摘要和详细描述
    try:
        short_desc1=bug_report1["short_desc"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        short_desc1=''
    if(short_desc1==[]):
        short_desc1=''
    try:
        description1=bug_report1["description"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        description1=''
    if(description1==[]):
        description1=''
    
    try:
        short_desc2=bug_report2["short_desc"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        short_desc2=''
    if(short_desc2==[]):
        short_desc2=''
    try:
        description2=bug_report2["description"]#实际调试的时候存在一些Keyerror也就是字典数据中没有这个description属性。见3820编号的缺陷报告就是这样
    except KeyError:
        description2=''
    if(description2==[]):
        description2=''
    f_write.write('bug1_short_desc:\n')
    f_write.write('{{{->short_desc----------------------------------------------short_desc\n')
    f_write.write(short_desc1)
    f_write.write('\n')
    f_write.write('}}}->short_desc----------------------------------------------short_desc\n')
    
    f_write.write('bug2_short_desc:\n')
    f_write.write('{{{->short_desc----------------------------------------------short_desc\n')
    f_write.write(short_desc2)
    f_write.write('\n')
    f_write.write('}}}->short_desc----------------------------------------------short_desc\n')
    
    f_write.write('bug1_desc:\n')
    f_write.write('{->desc----------------------------------------------desc\n')
    f_write.write(description1)
    f_write.write('\n')
    f_write.write('}->desc----------------------------------------------desc\n')
    
    f_write.write('bug2_desc:\n')
    f_write.write('{->desc----------------------------------------------desc\n')
    f_write.write(description2)
    f_write.write('\n')
    f_write.write('}->desc----------------------------------------------desc\n')
    
    f_write.flush()


def outputrightPredictedReportPairs(gs_of_data_for_testing_model,predicted_of_data_for_testing_model,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path):
    f_gs=open(gs_of_data_for_testing_model)
    gs=[line.strip('\n').strip(' ') for line in f_gs.readlines()] #如果不做处理，容易出错。会出现异常标签，比如'1 '即带上空格或者回车的。
    f_gs.close()
    f_predicted=open(predicted_of_data_for_testing_model)
    predict=[line.strip('\n').strip(' ') for line in f_predicted.readlines()]
    f_predicted.close()
    f_write=open(outputFile_path, 'w',encoding='UTF-8')
    DupIsPredictedAsDup=[]
    NonDupIsPredictedAsNonDup=[]
    index=0
    for gs_item in gs:
        predict_item=predict[index]
        if gs_item == predict_item:#预测和实际一致
            if gs_item=='1' and predict_item=='1':
                lineNumber=index+1 #行号从下标1开始
                DupIsPredictedAsDup.append(lineNumber)
            elif gs_item=='-1' and predict_item=='-1':
                lineNumber=index+1 #行号从下标1开始
                NonDupIsPredictedAsNonDup.append(lineNumber)
            else:
                print ("wrong!")
        index=index+1
    if (project_of_data_for_testing_model=='eclipse'):
        db=client.eclipse
    elif (project_of_data_for_testing_model=='netBeans'):
        db=client.netBeans
    elif (project_of_data_for_testing_model=='openOffice'):
        db=client.openOffice
    else:
        print ("wrong project_of_data_for_testing_model!")
    f_write.write("统计：真实为重复缺陷报告对，预测正确{}个\n".format(len(DupIsPredictedAsDup)))
    f_write.write("统计：真实为非重复缺陷报告对，预测正确{}个\n".format(len(NonDupIsPredictedAsNonDup)))
#    f_write.write('共计{}个这样的\n'.format(len(DupIsPredictedAsNonDup)))
    
    if propertyInProject_of_data_for_testing_model=='complete':
        trainDict=read_from_pkl(trainPKL_project_of_data_for_testing_model)
        testDict=read_from_pkl(testPKL_project_of_data_for_testing_model)
        f_write.write("输出：真实为重复缺陷报告对，预测也正确。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(DupIsPredictedAsDup)))
        i=0
        for lineNumber in DupIsPredictedAsDup:
            i=i+1
            if (lineNumber<=trainset_num):
                index=lineNumber-1
                key=((list)(trainDict.keys()))[index]
                bug1=str(key[0])
                bug2=str(key[1])
            elif(lineNumber>trainset_num):
                index=lineNumber-trainset_num-1
                key=((list)(testDict.keys()))[index]
                bug1=str(key[0])
                bug2=str(key[1])
            else:
                print ("wrong lineNumber!")
                break
            ####取出缺陷对的数据

            f_write.write('index in DupIsPredictedAsDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            pass
        f_write.write("输出：真实为非重复缺陷报告对，预测也正确。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(NonDupIsPredictedAsNonDup)))
        i=0
        for lineNumber in NonDupIsPredictedAsNonDup:
            i=i+1
            if (lineNumber<=trainset_num):
                index=lineNumber-1
                key=((list)(trainDict.keys()))[index]
                bug1=str(key[0])
                bug2=str(key[1])
            elif(lineNumber>trainset_num):
                index=lineNumber-trainset_num-1
                key=((list)(testDict.keys()))[index]
                bug1=str(key[0])
                bug2=str(key[1])
            else:
                print ("wrong lineNumber!")
                break
            ####取出缺陷对的数据
            f_write.write('----------------------------------------------------------------------------\n')
            f_write.write('index in NonDupIsPredictedAsNonDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            f_write.write('----------------------------------------------------------------------------\n')
            pass
    elif (propertyInProject_of_data_for_testing_model=='train'):
        trainDict=read_from_pkl(trainPKL_project_of_data_for_testing_model)
        f_write.write("输出：真实为重复缺陷报告对，预测也正确。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(DupIsPredictedAsDup)))
        i=0
        for lineNumber in DupIsPredictedAsDup:
            i=i+1
            index=lineNumber-1
            key=((list)(trainDict.keys()))[index]
            bug1=str(key[0])
            bug2=str(key[1])
            ####取出缺陷对的数据
            f_write.write('----------------------------------------------------------------------------\n')
            f_write.write('index in DupIsPredictedAsDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            f_write.write('----------------------------------------------------------------------------\n')
            pass
        f_write.write("输出：真实为非重复缺陷报告对，预测也正确。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(NonDupIsPredictedAsNonDup)))
        i=0
        for lineNumber in NonDupIsPredictedAsNonDup:
            i=i+1
            index=lineNumber-1
            key=((list)(trainDict.keys()))[index]
            bug1=str(key[0])
            bug2=str(key[1])
            ####取出缺陷对的数据
            f_write.write('----------------------------------------------------------------------------\n')
            f_write.write('index in NonDupIsPredictedAsNonDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            f_write.write('----------------------------------------------------------------------------\n')
            pass
    elif propertyInProject_of_data_for_testing_model=='test':
        testDict=read_from_pkl(testPKL_project_of_data_for_testing_model)
        f_write.write("输出：真实为重复缺陷报告对，预测也正确。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(DupIsPredictedAsDup)))
        i=0
        for lineNumber in DupIsPredictedAsDup:
            i=i+1
            index=lineNumber-1
            key=((list)(testDict.keys()))[index]
            bug1=str(key[0])
            bug2=str(key[1])
            ####取出缺陷对的数据
            f_write.write('----------------------------------------------------------------------------\n')
            f_write.write('index in DupIsPredictedAsNonDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            f_write.write('----------------------------------------------------------------------------\n')
            pass
        f_write.write("输出：真实为非重复缺陷报告对，预测也正确。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(NonDupIsPredictedAsNonDup)))
        i=0
        for lineNumber in NonDupIsPredictedAsNonDup:
            i=i+1
            index=lineNumber-1
            key=((list)(testDict.keys()))[index]
            bug1=str(key[0])
            bug2=str(key[1])
            ####取出缺陷对的数据
            f_write.write('----------------------------------------------------------------------------\n')
            f_write.write('index in NonDupIsPredictedAsNonDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            f_write.write('----------------------------------------------------------------------------\n')
            pass
    else:
        print ("wrong propertyInProject_of_data_for_testing_model!")


def outputWrongPredictedReportPairs(gs_of_data_for_testing_model,predicted_of_data_for_testing_model,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path):
    f_gs=open(gs_of_data_for_testing_model)
    gs=[line.strip('\n').strip(' ') for line in f_gs.readlines()] #如果不做处理，容易出错。会出现异常标签，比如'1 '即带上空格或者回车的。
    f_gs.close()
    f_predicted=open(predicted_of_data_for_testing_model)
    predict=[line.strip('\n').strip(' ') for line in f_predicted.readlines()]
    f_predicted.close()
    f_write=open(outputFile_path, 'w',encoding='UTF-8')
    DupIsPredictedAsNonDup=[]
    NonDupIsPredictedAsDup=[]
    index=0
    for gs_item in gs:
        predict_item=predict[index]
        if gs_item != predict_item:#预测和实际不一致
            if gs_item=='1' and predict_item=='-1':
                lineNumber=index+1 #行号从下标1开始
                DupIsPredictedAsNonDup.append(lineNumber)
            elif gs_item=='-1' and predict_item=='1':
                lineNumber=index+1 #行号从下标1开始
                NonDupIsPredictedAsDup.append(lineNumber)
            else:
                print ("wrong!")
        index=index+1
    if (project_of_data_for_testing_model=='eclipse'):
        db=client.eclipse
    elif (project_of_data_for_testing_model=='netBeans'):
        db=client.netBeans
    elif (project_of_data_for_testing_model=='openOffice'):
        db=client.openOffice
    else:
        print ("wrong project_of_data_for_testing_model!")
    f_write.write("统计：真实为重复缺陷报告对，却被预测为非负缺陷报告对{}个\n".format(len(DupIsPredictedAsNonDup)))
    f_write.write("统计：真实为非重复缺陷报告对，却被预测为重复缺陷报告对{}个\n".format(len(NonDupIsPredictedAsDup)))
    f_write.write('共计{}个这样的\n'.format(len(DupIsPredictedAsNonDup)))
    
    if propertyInProject_of_data_for_testing_model=='complete':
        trainDict=read_from_pkl(trainPKL_project_of_data_for_testing_model)
        testDict=read_from_pkl(testPKL_project_of_data_for_testing_model)
        f_write.write("输出：真实为重复缺陷报告对，却被预测为非负缺陷报告对。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(DupIsPredictedAsNonDup)))
        i=0
        for lineNumber in DupIsPredictedAsNonDup:
            i=i+1
            if (lineNumber<=trainset_num):
                index=lineNumber-1
                key=((list)(trainDict.keys()))[index]
                bug1=str(key[0])
                bug2=str(key[1])
            elif(lineNumber>trainset_num):
                index=lineNumber-trainset_num-1
                key=((list)(testDict.keys()))[index]
                bug1=str(key[0])
                bug2=str(key[1])
            else:
                print ("wrong lineNumber!")
                break
            ####取出缺陷对的数据

            f_write.write('index in DupIsPredictedAsNonDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            pass
        f_write.write("输出：真实为非重复缺陷报告对，却被预测为重复缺陷报告对。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(NonDupIsPredictedAsDup)))
        i=0
        for lineNumber in NonDupIsPredictedAsDup:
            i=i+1
            if (lineNumber<=trainset_num):
                index=lineNumber-1
                key=((list)(trainDict.keys()))[index]
                bug1=str(key[0])
                bug2=str(key[1])
            elif(lineNumber>trainset_num):
                index=lineNumber-trainset_num-1
                key=((list)(testDict.keys()))[index]
                bug1=str(key[0])
                bug2=str(key[1])
            else:
                print ("wrong lineNumber!")
                break
            ####取出缺陷对的数据
            f_write.write('----------------------------------------------------------------------------\n')
            f_write.write('index in NonDupIsPredictedAsDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            f_write.write('----------------------------------------------------------------------------\n')
            pass
    elif (propertyInProject_of_data_for_testing_model=='train'):
        trainDict=read_from_pkl(trainPKL_project_of_data_for_testing_model)
        f_write.write("输出：真实为重复缺陷报告对，却被预测为非负缺陷报告对。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(DupIsPredictedAsNonDup)))
        i=0
        for lineNumber in DupIsPredictedAsNonDup:
            i=i+1
            index=lineNumber-1
            key=((list)(trainDict.keys()))[index]
            bug1=str(key[0])
            bug2=str(key[1])
            ####取出缺陷对的数据
            f_write.write('----------------------------------------------------------------------------\n')
            f_write.write('index in DupIsPredictedAsNonDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            f_write.write('----------------------------------------------------------------------------\n')
            pass
        f_write.write("输出：真实为非重复缺陷报告对，却被预测为重复缺陷报告对。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(NonDupIsPredictedAsDup)))
        i=0
        for lineNumber in NonDupIsPredictedAsDup:
            i=i+1
            index=lineNumber-1
            key=((list)(trainDict.keys()))[index]
            bug1=str(key[0])
            bug2=str(key[1])
            ####取出缺陷对的数据
            f_write.write('----------------------------------------------------------------------------\n')
            f_write.write('index in NonDupIsPredictedAsDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            f_write.write('----------------------------------------------------------------------------\n')
            pass
    elif propertyInProject_of_data_for_testing_model=='test':
        testDict=read_from_pkl(testPKL_project_of_data_for_testing_model)
        f_write.write("输出：真实为重复缺陷报告对，却被预测为非负缺陷报告对。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(DupIsPredictedAsNonDup)))
        i=0
        for lineNumber in DupIsPredictedAsNonDup:
            i=i+1
            index=lineNumber-1
            key=((list)(testDict.keys()))[index]
            bug1=str(key[0])
            bug2=str(key[1])
            ####取出缺陷对的数据
            f_write.write('----------------------------------------------------------------------------\n')
            f_write.write('index in DupIsPredictedAsNonDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            f_write.write('----------------------------------------------------------------------------\n')
            pass
        f_write.write("输出：真实为非重复缺陷报告对，却被预测为重复缺陷报告对。\n")
        f_write.write("<------------------------------------------------>\n")
        f_write.write('共计{}个这样的\n'.format(len(NonDupIsPredictedAsDup)))
        i=0
        for lineNumber in NonDupIsPredictedAsDup:
            i=i+1
            index=lineNumber-1
            key=((list)(testDict.keys()))[index]
            bug1=str(key[0])
            bug2=str(key[1])
            ####取出缺陷对的数据
            f_write.write('----------------------------------------------------------------------------\n')
            f_write.write('index in NonDupIsPredictedAsDup is:{}\n'.format(i))
            f_write.write('bug1_id:{},bug2_id:{}\n'.format(bug1,bug2))
            f_write.flush()
            writeBugInformation(bug1=bug1,bug2=bug2,db=db,f_write=f_write)
            f_write.write('----------------------------------------------------------------------------\n')
            pass
    else:
        print ("wrong propertyInProject_of_data_for_testing_model!")

def computeIndicators(gs_file_path,predict_file_path):
    f1=open(gs_file_path)
    gs=[line.strip('\n').strip(' ') for line in f1.readlines()] #如果不做处理，容易出错。会出现异常标签，比如'1 '即带上空格或者回车的。
    print (len(gs))
    f1.close()
    f2=open(predict_file_path)
    predict=[line.strip('\n').strip(' ') for line in f2.readlines()]
    print (len(predict))
    print (classification_report(gs,predict,labels=['1','-1'],target_names=['Duplicate','NonDuplicate'],digits=4))


def computeTakeLabOnly_rightPredictedInformation(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    print ('eclipse训练集进行训练然后预测eclipse训练集')
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.rightPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='train'
#    computeIndicators(gs_file_path_1_1,predict_file_path_1_1)
    project_of_data_for_testing_model='eclipse'
    outputrightPredictedReportPairs(gs_file_path_1_1,predict_file_path_1_1,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)


def computeTakeLabOnly_wrongPredictedInformation(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ####TakeLab_only
    print ('TakeLab_only,5000 train,1:4')

    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    #1_5 eclipse训练集进行训练然后预测openOffice全集
    
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    print ('eclipse训练集进行训练然后预测eclipse训练集')
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='train'
#    computeIndicators(gs_file_path_1_1,predict_file_path_1_1)
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_1_1,predict_file_path_1_1,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse测试集')
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='test'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_1_2,predict_file_path_1_2,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_complete'
    gs_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('eclipse训练集进行训练然后预测eclipse全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_1_3,predict_file_path_1_3,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_netBeans_complete'
    gs_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='netBeans'
    print ('eclipse训练集进行训练然后预测netBeans全集')
    outputWrongPredictedReportPairs(gs_file_path_1_4,predict_file_path_1_4,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #1_5 eclipse训练集进行训练然后预测openOffice全
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_openOffice_complete'
    gs_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('eclipse训练集进行训练然后预测openOffice全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_1_5,predict_file_path_1_5,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #2_1 netBeans训练集进行训练然后预测netBeans训练集
    train_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='train'
    project_of_data_for_testing_model='netBeans'
    print ('netBeans训练集进行训练然后预测netBeans训练集')
    computeIndicators(gs_file_path_2_1,predict_file_path_2_1)
    outputWrongPredictedReportPairs(gs_file_path_2_1,predict_file_path_2_1,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    
    #2_2 netBeans训练集进行训练然后预测netBeans测试集
    train_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='test'
    project_of_data_for_testing_model='netBeans'
    print ('netBeans训练集进行训练然后预测netBeans测试集')
    outputWrongPredictedReportPairs(gs_file_path_2_2,predict_file_path_2_2,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #2_3 netBeans训练集进行训练然后预测netBeans全集
    train_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_netBeans_complete'
    gs_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('netBeans训练集进行训练然后预测netBeans全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='netBeans'
    outputWrongPredictedReportPairs(gs_file_path_2_3,predict_file_path_2_3,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #2_4 netBeans训练集进行训练然后预测eclipse全集
    train_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_complete'
    gs_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('enetBeans训练集进行训练然后预测eclipse全集')
    
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_2_4,predict_file_path_2_4,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #2_5 netBeans训练集进行训练然后预测openOffice全集
    train_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_openOffice_complete'
    gs_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('netBeans训练集进行训练然后预测openOffice全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_2_5,predict_file_path_2_5,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #3_1 openOffice训练集进行训练然后预测openOffice训练集
    train_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测openOffice训练集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='train'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_3_1,predict_file_path_3_1,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #3_2 openOffice训练集进行训练然后预测openOffice测试集
    train_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测openOffice测试集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='test'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_3_2,predict_file_path_3_2,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #3_3 openOffice训练集进行训练然后预测openOffice全集
    train_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_openOffice_complete'
    gs_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测openOffice全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_3_3,predict_file_path_3_3,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #3_4 openOffice训练集进行训练然后预测eclipse全集
    train_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_complete'
    gs_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测eclipse全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_3_4,predict_file_path_3_4,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #3_5 openOffice训练集进行训练然后预测netBeans全集
    train_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_netBeans_complete'
    gs_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测netBeans全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='netBeans'
    outputWrongPredictedReportPairs(gs_file_path_3_5,predict_file_path_3_5,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)



def computeTakeLabCategoricalCombined_wrongPredictedInformation(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ####TakeLab_Categorical_combined
    print ('TakeLab_Categorical_combined,5000 train,1:4')

    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    #1_5 eclipse训练集进行训练然后预测openOffice全集
    
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    print ('eclipse训练集进行训练然后预测eclipse训练集')
    train_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='train'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_1_1,predict_file_path_1_1,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    train_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse测试集')
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='test'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_1_2,predict_file_path_1_2,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    train_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_eclipse_complete'
    gs_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('eclipse训练集进行训练然后预测eclipse全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_1_3,predict_file_path_1_3,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    train_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_netBeans_complete'
    gs_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='netBeans'
    print ('eclipse训练集进行训练然后预测netBeans全集')
    outputWrongPredictedReportPairs(gs_file_path_1_4,predict_file_path_1_4,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #1_5 eclipse训练集进行训练然后预测openOffice全
    train_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_openOffice_complete'
    gs_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('eclipse训练集进行训练然后预测openOffice全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_1_5,predict_file_path_1_5,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #2_1 netBeans训练集进行训练然后预测netBeans训练集
    train_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='train'
    project_of_data_for_testing_model='netBeans'
    print ('netBeans训练集进行训练然后预测netBeans训练集')
    computeIndicators(gs_file_path_2_1,predict_file_path_2_1)
    outputWrongPredictedReportPairs(gs_file_path_2_1,predict_file_path_2_1,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    
    #2_2 netBeans训练集进行训练然后预测netBeans测试集
    train_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='test'
    project_of_data_for_testing_model='netBeans'
    print ('netBeans训练集进行训练然后预测netBeans测试集')
    outputWrongPredictedReportPairs(gs_file_path_2_2,predict_file_path_2_2,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #2_3 netBeans训练集进行训练然后预测netBeans全集
    train_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_netBeans_complete'
    gs_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('netBeans训练集进行训练然后预测netBeans全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='netBeans'
    outputWrongPredictedReportPairs(gs_file_path_2_3,predict_file_path_2_3,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #2_4 netBeans训练集进行训练然后预测eclipse全集
    train_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_eclipse_complete'
    gs_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('enetBeans训练集进行训练然后预测eclipse全集')
    
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_2_4,predict_file_path_2_4,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #2_5 netBeans训练集进行训练然后预测openOffice全集
    train_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_openOffice_complete'
    gs_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('netBeans训练集进行训练然后预测openOffice全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_2_5,predict_file_path_2_5,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #3_1 openOffice训练集进行训练然后预测openOffice训练集
    train_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测openOffice训练集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='train'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_3_1,predict_file_path_3_1,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #3_2 openOffice训练集进行训练然后预测openOffice测试集
    train_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测openOffice测试集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='test'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_3_2,predict_file_path_3_2,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #3_3 openOffice训练集进行训练然后预测openOffice全集
    train_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_openOffice_complete'
    gs_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测openOffice全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_3_3,predict_file_path_3_3,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #3_4 openOffice训练集进行训练然后预测eclipse全集
    train_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_eclipse_complete'
    gs_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测eclipse全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_3_4,predict_file_path_3_4,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #3_5 openOffice训练集进行训练然后预测netBeans全集
    train_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_netBeans_complete'
    gs_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测netBeans全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='netBeans'
    outputWrongPredictedReportPairs(gs_file_path_3_5,predict_file_path_3_5,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)


def computeCategoricalOnly_wrongPredictedInformation(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ####TakeLab_Categorical_combined
    print ('CategoricalOnly,5000 train,1:4')

    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    #1_5 eclipse训练集进行训练然后预测openOffice全集
    
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    print ('eclipse训练集进行训练然后预测eclipse训练集')
    train_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='train'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_1_1,predict_file_path_1_1,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    train_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse测试集')
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='test'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_1_2,predict_file_path_1_2,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    train_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_eclipse_complete'
    gs_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('eclipse训练集进行训练然后预测eclipse全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_1_3,predict_file_path_1_3,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    train_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_netBeans_complete'
    gs_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='netBeans'
    print ('eclipse训练集进行训练然后预测netBeans全集')
    outputWrongPredictedReportPairs(gs_file_path_1_4,predict_file_path_1_4,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #1_5 eclipse训练集进行训练然后预测openOffice全
    train_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_openOffice_complete'
    gs_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('eclipse训练集进行训练然后预测openOffice全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_1_5,predict_file_path_1_5,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #2_1 netBeans训练集进行训练然后预测netBeans训练集
    train_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='train'
    project_of_data_for_testing_model='netBeans'
    print ('netBeans训练集进行训练然后预测netBeans训练集')
    computeIndicators(gs_file_path_2_1,predict_file_path_2_1)
    outputWrongPredictedReportPairs(gs_file_path_2_1,predict_file_path_2_1,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    
    #2_2 netBeans训练集进行训练然后预测netBeans测试集
    train_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='test'
    project_of_data_for_testing_model='netBeans'
    print ('netBeans训练集进行训练然后预测netBeans测试集')
    outputWrongPredictedReportPairs(gs_file_path_2_2,predict_file_path_2_2,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #2_3 netBeans训练集进行训练然后预测netBeans全集
    train_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_netBeans_complete'
    gs_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('netBeans训练集进行训练然后预测netBeans全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='netBeans'
    outputWrongPredictedReportPairs(gs_file_path_2_3,predict_file_path_2_3,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #2_4 netBeans训练集进行训练然后预测eclipse全集
    train_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_eclipse_complete'
    gs_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('enetBeans训练集进行训练然后预测eclipse全集')
    
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_2_4,predict_file_path_2_4,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #2_5 netBeans训练集进行训练然后预测openOffice全集
    train_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_openOffice_complete'
    gs_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('netBeans训练集进行训练然后预测openOffice全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_2_5,predict_file_path_2_5,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #3_1 openOffice训练集进行训练然后预测openOffice训练集
    train_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测openOffice训练集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='train'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_3_1,predict_file_path_3_1,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #3_2 openOffice训练集进行训练然后预测openOffice测试集
    train_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测openOffice测试集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='test'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_3_2,predict_file_path_3_2,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    
    #3_3 openOffice训练集进行训练然后预测openOffice全集
    train_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_openOffice_complete'
    gs_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测openOffice全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='openOffice'
    outputWrongPredictedReportPairs(gs_file_path_3_3,predict_file_path_3_3,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    #3_4 openOffice训练集进行训练然后预测eclipse全集
    train_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_eclipse_complete'
    gs_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测eclipse全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='eclipse'
    outputWrongPredictedReportPairs(gs_file_path_3_4,predict_file_path_3_4,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)
    
    #3_5 openOffice训练集进行训练然后预测netBeans全集
    train_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_netBeans_complete'
    gs_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    outputFile_path='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'+'.wrongPredictedInformation'
    print ('openOffice训练集进行训练然后预测netBeans全集')
    trainPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    testPKL_project_of_data_for_testing_model='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    propertyInProject_of_data_for_testing_model='complete'
    project_of_data_for_testing_model='netBeans'
    outputWrongPredictedReportPairs(gs_file_path_3_5,predict_file_path_3_5,trainPKL_project_of_data_for_testing_model,testPKL_project_of_data_for_testing_model,propertyInProject_of_data_for_testing_model,trainset_num,project_of_data_for_testing_model,outputFile_path)

if __name__ == "__main__":
    trainset_num_list=[5000,10000,15000,20000]
    trainset_num_list=[5000]
    ratio_TrueFlag=1
    ratio_FalseFlag=4
    for trainset_num in trainset_num_list:
        #####输出CategoricalOnly特征下预测错误的信息
        computeTakeLabOnly_rightPredictedInformation(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        computeTakeLabOnly_wrongPredictedInformation(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        computeTakeLabCategoricalCombined_wrongPredictedInformation(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        computeCategoricalOnly_wrongPredictedInformation(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#
        
        
        
        
