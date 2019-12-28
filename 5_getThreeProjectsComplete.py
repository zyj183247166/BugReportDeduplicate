# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:06:57 2019

@author: Administrator
"""

#合并训练集数据的特征和测试集数据的特征到complete集合中去
def get_eclipse_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    to_train_path='./processedData_2014MSR_xiaojie/takelab_only/to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    to_test_path='./processedData_2014MSR_xiaojie/takelab_only/to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    to_complete_path='./processedData_2014MSR_xiaojie/takelab_only/to_eclipse_complete.txt'  
    combineTwoTxts(to_train_path,to_test_path,to_complete_path)

    co_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    co_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    co_complete_path='./processedData_2014MSR_xiaojie/categorical_only/co_eclipse_complete.txt'  
    combineTwoTxts(co_train_path,co_test_path,co_complete_path)
    
    tc_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    tc_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    tc_complete_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_complete.txt'  
    combineTwoTxts(tc_train_path,tc_test_path,tc_complete_path)
    ##合并gs文件
    gs_train_path='./processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    gs_test_path='./processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    gs_complete_path='./processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'  
    combineTwoTxts(gs_train_path,gs_test_path,gs_complete_path)
    
    

def get_openOffice_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    to_train_path='./processedData_2014MSR_xiaojie/takelab_only/to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    to_test_path='./processedData_2014MSR_xiaojie/takelab_only/to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    to_complete_path='./processedData_2014MSR_xiaojie/takelab_only/to_openOffice_complete.txt'  
    combineTwoTxts(to_train_path,to_test_path,to_complete_path)

    co_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    co_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    co_complete_path='./processedData_2014MSR_xiaojie/categorical_only/co_openOffice_complete.txt'  
    combineTwoTxts(co_train_path,co_test_path,co_complete_path)      
    
    tc_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    tc_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    tc_complete_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_complete.txt'  
    combineTwoTxts(tc_train_path,tc_test_path,tc_complete_path)
    
    
    ##合并gs文件
    gs_train_path='./processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    gs_test_path='./processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    gs_complete_path='./processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'  
    combineTwoTxts(gs_train_path,gs_test_path,gs_complete_path)

def get_netBeans_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    to_train_path='./processedData_2014MSR_xiaojie/takelab_only/to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    to_test_path='./processedData_2014MSR_xiaojie/takelab_only/to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    to_complete_path='./processedData_2014MSR_xiaojie/takelab_only/to_netBeans_complete.txt'  
    combineTwoTxts(to_train_path,to_test_path,to_complete_path)

    co_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    co_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    co_complete_path='./processedData_2014MSR_xiaojie/categorical_only/co_netBeans_complete.txt'  
    combineTwoTxts(co_train_path,co_test_path,co_complete_path)
    
    tc_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    tc_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    tc_complete_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_complete.txt'  
    combineTwoTxts(tc_train_path,tc_test_path,tc_complete_path)
    
    ##合并gs文件
    gs_train_path='./processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    gs_test_path='./processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    gs_complete_path='./processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'  
    combineTwoTxts(gs_train_path,gs_test_path,gs_complete_path)
    
    

    
    
def combineTwoTxts(txt_path_1,txt_path_2,target_path):
    f1 = open(txt_path_1, 'r',encoding='UTF-8')
    f2 = open(txt_path_2,'r',encoding='UTF-8')
    f3 = open(target_path,'w',encoding='UTF-8')
    for num, value in enumerate(f1):
#        print (value)
        if(value=='\n'): #空行，就不写入。其实不需要这个判断，因为即使有空行，用for和enumerate以后，也不会读出来。并且每行解析出的value之后都是自带\n的。
            continue
        f3.write(value)
        f3.flush()
    for num, value in enumerate(f2):
#        print (value)
        if(value=='\n'): #空行，就不写入。
            continue
        f3.write(value)
        f3.flush()

if __name__ == "__main__":
    trainset_num_list=[5000,10000,15000,20000]
#    combineTwoTxts('./testTakeLab1.txt','testTakeLab2.txt','./test.txt')
    trainset_num_list=[5000]
    ratio_TrueFlag=1
    ratio_FalseFlag=4
    for trainset_num in trainset_num_list:
        get_netBeans_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        get_eclipse_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        get_openOffice_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag)