# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:06:57 2019

@author: Administrator
"""

def chaifen_eclipse_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    to_train_path='./processedData_2014MSR_xiaojie/takelab_only/to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' 
    to_test_path='./processedData_2014MSR_xiaojie/takelab_only/to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    to_complete_path='./processedData_2014MSR_xiaojie/takelab_only/to_eclipse_complete.scaled.txt'  

    co_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' 
    co_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    co_complete_path='./processedData_2014MSR_xiaojie/categorical_only/co_eclipse_complete.scaled.txt'  
    
    tc_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' 
    tc_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    tc_complete_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_complete.scaled.txt'  
    
    chaifen(to_train_path,to_test_path,to_complete_path,trainset_num)
    chaifen(co_train_path,co_test_path,co_complete_path,trainset_num)
    chaifen(tc_train_path,tc_test_path,tc_complete_path,trainset_num)


def chaifen_openOffice_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    to_train_path='./processedData_2014MSR_xiaojie/takelab_only/to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' 
    to_test_path='./processedData_2014MSR_xiaojie/takelab_only/to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    to_complete_path='./processedData_2014MSR_xiaojie/takelab_only/to_openOffice_complete.scaled.txt'  
    
    
    
    

    co_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' 
    co_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    co_complete_path='./processedData_2014MSR_xiaojie/categorical_only/co_openOffice_complete.scaled.txt'  
    
    tc_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' 
    tc_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    tc_complete_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_complete.scaled.txt'  
    
    
    chaifen(to_train_path,to_test_path,to_complete_path,trainset_num)
    chaifen(co_train_path,co_test_path,co_complete_path,trainset_num)
    chaifen(tc_train_path,tc_test_path,tc_complete_path,trainset_num)

def chaifen_netBeans_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    to_train_path='./processedData_2014MSR_xiaojie/takelab_only/to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' 
    to_test_path='./processedData_2014MSR_xiaojie/takelab_only/to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    to_complete_path='./processedData_2014MSR_xiaojie/takelab_only/to_netBeans_complete.scaled.txt'  

    co_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' 
    co_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    co_complete_path='./processedData_2014MSR_xiaojie/categorical_only/co_netBeans_complete.scaled.txt'  
    
    tc_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' 
    tc_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    tc_complete_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_complete.scaled.txt'  
    
    chaifen(to_train_path,to_test_path,to_complete_path,trainset_num)
    chaifen(co_train_path,co_test_path,co_complete_path,trainset_num)
    chaifen(tc_train_path,tc_test_path,tc_complete_path,trainset_num)


def chaifen(txt_path_1,txt_path_2,target_path,trainset_num):
    f1 = open(txt_path_1, 'w',encoding='UTF-8')
    f2 = open(txt_path_2,'w',encoding='UTF-8')
    f3 = open(target_path,'r',encoding='UTF-8')
    index=0
    for num, value in enumerate(f3):
        if index<trainset_num:
            f1.write(value)
            f1.flush()
        else:
            f2.write(value)
            f2.flush()
#        print (value)
        if(value=='\n'): #空行，就不写入。其实不需要这个判断，因为即使有空行，用for和enumerate以后，也不会读出来。并且每行解析出的value之后都是自带\n的。
            continue
        index=index+1
        

if __name__ == "__main__":
    trainset_num_list=[5000,10000,15000,20000]
    trainset_num_list=[5000]
    ratio_TrueFlag=1
    ratio_FalseFlag=4
    for trainset_num in trainset_num_list:
        chaifen_netBeans_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        chaifen_eclipse_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        chaifen_openOffice_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
