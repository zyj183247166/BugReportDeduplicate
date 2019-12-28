# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:34:09 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:06:28 2019

@author: Administrator
"""
def combineOtherFeaturesAndTakeLabFeaturesAndTag_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    otherFeatures_test_path='./processedData_2014MSR_xiaojie/otherFeatures_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    TakeLabFeaturesAndTag_train_path='./processedData_2014MSR_xiaojie/takelab_only/to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    TakeLabFeaturesAndTag_test_path='./processedData_2014MSR_xiaojie/takelab_only/to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    combined_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    f3 = open(combined_train_path,'w',encoding='UTF-8')
    with open(TakeLabFeaturesAndTag_train_path, 'r',encoding='UTF-8') as f1:
        with open(otherFeatures_train_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+' '+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
    f3 = open(combined_test_path,'w',encoding='UTF-8')
    with open(TakeLabFeaturesAndTag_test_path, 'r',encoding='UTF-8') as f1:
        with open(otherFeatures_test_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+' '+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()

    
def combineOtherFeaturesAndTakeLabFeaturesAndTag_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    otherFeatures_test_path='./processedData_2014MSR_xiaojie/otherFeatures_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    TakeLabFeaturesAndTag_train_path='./processedData_2014MSR_xiaojie/takelab_only/to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    TakeLabFeaturesAndTag_test_path='./processedData_2014MSR_xiaojie/takelab_only/to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    combined_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    f3 = open(combined_train_path,'w',encoding='UTF-8')
    with open(TakeLabFeaturesAndTag_train_path, 'r',encoding='UTF-8') as f1:
        with open(otherFeatures_train_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+' '+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
    f3 = open(combined_test_path,'w',encoding='UTF-8')
    with open(TakeLabFeaturesAndTag_test_path, 'r',encoding='UTF-8') as f1:
        with open(otherFeatures_test_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+' '+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
                
def combineOtherFeaturesAndTakeLabFeaturesAndTag_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    otherFeatures_test_path='./processedData_2014MSR_xiaojie/otherFeatures_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    TakeLabFeaturesAndTag_train_path='./processedData_2014MSR_xiaojie/takelab_only/to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    TakeLabFeaturesAndTag_test_path='./processedData_2014MSR_xiaojie/takelab_only/to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    combined_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    f3 = open(combined_train_path,'w',encoding='UTF-8')
    with open(TakeLabFeaturesAndTag_train_path, 'r',encoding='UTF-8') as f1:
        with open(otherFeatures_train_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+' '+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
    f3 = open(combined_test_path,'w',encoding='UTF-8')
    with open(TakeLabFeaturesAndTag_test_path, 'r',encoding='UTF-8') as f1:
        with open(otherFeatures_test_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+' '+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()

def test():
    otherFeatures_train_path='./processedData_2014MSR_xiaojie/otherFeatures_test.txt' 
    TakeLabFeaturesAndTag_train_path='./processedData_2014MSR_xiaojie/takelab_only/to_test.txt'   ##gs表示standard groud也就是标签
    combined_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_test.txt' 
    
    f3 = open(combined_train_path,'w',encoding='UTF-8')
    with open(TakeLabFeaturesAndTag_train_path, 'r',encoding='UTF-8') as f1:
        with open(otherFeatures_train_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+' '+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()


if __name__ == "__main__":
    trainset_num_list=[5000,10000,15000,20000]
#    test()
    trainset_num_list=[5000]
    ratio_TrueFlag=1
    ratio_FalseFlag=4
    for trainset_num in trainset_num_list:
        combineOtherFeaturesAndTakeLabFeaturesAndTag_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        combineOtherFeaturesAndTakeLabFeaturesAndTag_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        combineOtherFeaturesAndTakeLabFeaturesAndTag_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag)