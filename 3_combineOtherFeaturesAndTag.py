# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:06:28 2019

@author: Administrator
"""
def combineOtherFeaturesAndTag_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    otherFeatures_test_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    tag_train_path='./processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'   ##gs表示standard groud也就是标签
    tag_test_path='./processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'  
    combined_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    scores_train= [int(x) for x in open(tag_train_path)]
    f1 = open(combined_train_path, 'w',encoding='UTF-8')
    f2 = open(otherFeatures_train_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_train[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()
        
    scores_test= [int(x) for x in open(tag_test_path)]
    f1 = open(combined_test_path, 'w',encoding='UTF-8')
    f2 = open(otherFeatures_test_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_test[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()

    
def combineOtherFeaturesAndTag_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    otherFeatures_test_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    tag_train_path='./processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'   ##gs表示standard groud也就是标签
    tag_test_path='./processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'  
    combined_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    scores_train= [int(x) for x in open(tag_train_path)]
    f1 = open(combined_train_path, 'w',encoding='UTF-8')
    f2 = open(otherFeatures_train_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_train[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()
        
    scores_test= [int(x) for x in open(tag_test_path)]
    f1 = open(combined_test_path, 'w',encoding='UTF-8')
    f2 = open(otherFeatures_test_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_test[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()
    
def combineOtherFeaturesAndTag_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    otherFeatures_test_path='./processedData_2014MSR_xiaojie/otherFeatures_NoStartFrom1_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    tag_train_path='./processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'   ##gs表示standard groud也就是标签
    tag_test_path='./processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'  
    combined_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    scores_train= [int(x) for x in open(tag_train_path)]
    f1 = open(combined_train_path, 'w',encoding='UTF-8')
    f2 = open(otherFeatures_train_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_train[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()
        
    scores_test= [int(x) for x in open(tag_test_path)]
    f1 = open(combined_test_path, 'w',encoding='UTF-8')
    f2 = open(otherFeatures_test_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_test[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()

def test():
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_test.txt' 
    tag_train_path='./processedData_2014MSR_xiaojie/gs_test.txt'   ##gs表示standard groud也就是标签
    combined_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_test.txt' 
    
    scores_train= [int(x) for x in open(tag_train_path)]
    f1 = open(combined_train_path, 'w',encoding='UTF-8')
    f2 = open(otherFeatures_train_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_train[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()


if __name__ == "__main__":
    trainset_num_list=[5000,10000,15000,20000]
#    test()
    trainset_num_list=[5000]
    ratio_TrueFlag=1
    ratio_FalseFlag=4
    for trainset_num in trainset_num_list:
        combineOtherFeaturesAndTag_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        combineOtherFeaturesAndTag_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        combineOtherFeaturesAndTag_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag)