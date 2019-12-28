# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:39:15 2019

@author: Administrator
"""

from sklearn.metrics import classification_report

def computeIndicators(gs_file_path,predict_file_path):
    f1=open(gs_file_path)
    gs=[line.strip('\n').strip(' ') for line in f1.readlines()] #如果不做处理，容易出错。会出现异常标签，比如'1 '即带上空格或者回车的。
    print (len(gs))
    f1.close()
    f2=open(predict_file_path)
    predict=[line.strip('\n').strip(' ') for line in f2.readlines()]
    print (len(predict))
    print (classification_report(gs,predict,labels=['1','-1'],target_names=['Duplicate','NonDuplicate'],digits=4))





def computeTakeLabOnly(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ####TakeLab_only
    print ('TakeLab_only,5000 train,1:4')

    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    #1_5 eclipse训练集进行训练然后预测openOffice全集
    
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse训练集')
    computeIndicators(gs_file_path_1_1,predict_file_path_1_1)
    
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse测试集')
    computeIndicators(gs_file_path_1_2,predict_file_path_1_2)
    
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_complete'
    gs_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_1_3,predict_file_path_1_3)
    
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_netBeans_complete'
    gs_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_1_4,predict_file_path_1_4)
    
    
    
    #1_5 eclipse训练集进行训练然后预测openOffice全
    train_filename='to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_openOffice_complete'
    gs_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_1_5,predict_file_path_1_5)
    
    
    
    #2_1 netBeans训练集进行训练然后预测netBeans训练集
    train_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测netBeans训练集')
    computeIndicators(gs_file_path_2_1,predict_file_path_2_1)
    
    
    
    #2_2 netBeans训练集进行训练然后预测netBeans测试集
    train_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测netBeans测试集')
    computeIndicators(gs_file_path_2_2,predict_file_path_2_2)
    
    #2_3 netBeans训练集进行训练然后预测netBeans全集
    train_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_netBeans_complete'
    gs_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_2_3,predict_file_path_2_3)
    
    
    #2_4 netBeans训练集进行训练然后预测eclipse全集
    train_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_complete'
    gs_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('enetBeans训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_2_4,predict_file_path_2_4)
    
    #2_5 netBeans训练集进行训练然后预测openOffice全集
    train_filename='to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_openOffice_complete'
    gs_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_2_5,predict_file_path_2_5)
    
    
    #3_1 openOffice训练集进行训练然后预测openOffice训练集
    train_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测openOffice训练集')
    computeIndicators(gs_file_path_3_1,predict_file_path_3_1)
    
    
    #3_2 openOffice训练集进行训练然后预测openOffice测试集
    train_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测openOffice测试集')
    computeIndicators(gs_file_path_3_2,predict_file_path_3_2)
    
    
    #3_3 openOffice训练集进行训练然后预测openOffice全集
    train_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_openOffice_complete'
    gs_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_3_3,predict_file_path_3_3)
    
    #3_4 openOffice训练集进行训练然后预测eclipse全集
    train_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_eclipse_complete'
    gs_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_3_4,predict_file_path_3_4)
    
    #3_5 openOffice训练集进行训练然后预测netBeans全集
    train_filename='to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='to_netBeans_complete'
    gs_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_3_5,predict_file_path_3_5)



def computeCategoricalOnly(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    
    ####Categorical_only
    print ('Categorical_only,5000 train,1:4')
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    #1_5 eclipse训练集进行训练然后预测openOffice全集
    
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    train_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse训练集')
    computeIndicators(gs_file_path_1_1,predict_file_path_1_1)
    
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    train_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse测试集')
    computeIndicators(gs_file_path_1_2,predict_file_path_1_2)
    
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    train_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_eclipse_complete'
    gs_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_1_3,predict_file_path_1_3)
    
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    train_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_netBeans_complete'
    gs_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_1_4,predict_file_path_1_4)
    
    
    
    #1_5 eclipse训练集进行训练然后预测openOffice全
    train_filename='co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_openOffice_complete'
    gs_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_1_5,predict_file_path_1_5)
    
    
    
    #2_1 netBeans训练集进行训练然后预测netBeans训练集
    train_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测netBeans训练集')
    computeIndicators(gs_file_path_2_1,predict_file_path_2_1)
    
    
    
    #2_2 netBeans训练集进行训练然后预测netBeans测试集
    train_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测netBeans测试集')
    computeIndicators(gs_file_path_2_2,predict_file_path_2_2)
    
    #2_3 netBeans训练集进行训练然后预测netBeans全集
    train_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_netBeans_complete'
    gs_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_2_3,predict_file_path_2_3)
    
    
    #2_4 netBeans训练集进行训练然后预测eclipse全集
    train_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_eclipse_complete'
    gs_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('enetBeans训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_2_4,predict_file_path_2_4)
    
    #2_5 netBeans训练集进行训练然后预测openOffice全集
    train_filename='co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_openOffice_complete'
    gs_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_2_5,predict_file_path_2_5)
    
    
    #3_1 openOffice训练集进行训练然后预测openOffice训练集
    train_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测openOffice训练集')
    computeIndicators(gs_file_path_3_1,predict_file_path_3_1)
    
    
    #3_2 openOffice训练集进行训练然后预测openOffice测试集
    train_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测openOffice测试集')
    computeIndicators(gs_file_path_3_2,predict_file_path_3_2)
    
    
    #3_3 openOffice训练集进行训练然后预测openOffice全集
    train_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_openOffice_complete'
    gs_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_3_3,predict_file_path_3_3)
    
    #3_4 openOffice训练集进行训练然后预测eclipse全集
    train_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_eclipse_complete'
    gs_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_3_4,predict_file_path_3_4)
    
    #3_5 openOffice训练集进行训练然后预测netBeans全集
    train_filename='co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='co_netBeans_complete'
    gs_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/categorical_only/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_3_5,predict_file_path_3_5)





def computeTakeLabCategoricalCombined(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ####TakeLab_Categorical_combined
    print ('TakeLab_Categorical_combined,5000 train,1:4')
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    #1_5 eclipse训练集进行训练然后预测openOffice全集
    
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    train_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse训练集')
    computeIndicators(gs_file_path_1_1,predict_file_path_1_1)
    
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    train_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse测试集')
    computeIndicators(gs_file_path_1_2,predict_file_path_1_2)
    
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    train_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_eclipse_complete'
    gs_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_1_3,predict_file_path_1_3)
    
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    train_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_netBeans_complete'
    gs_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_1_4,predict_file_path_1_4)
    
    
    
    #1_5 eclipse训练集进行训练然后预测openOffice全
    train_filename='tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_openOffice_complete'
    gs_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('eclipse训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_1_5,predict_file_path_1_5)
    
    
    
    #2_1 netBeans训练集进行训练然后预测netBeans训练集
    train_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测netBeans训练集')
    computeIndicators(gs_file_path_2_1,predict_file_path_2_1)
    
    
    
    #2_2 netBeans训练集进行训练然后预测netBeans测试集
    train_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测netBeans测试集')
    computeIndicators(gs_file_path_2_2,predict_file_path_2_2)
    
    #2_3 netBeans训练集进行训练然后预测netBeans全集
    train_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_netBeans_complete'
    gs_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_2_3,predict_file_path_2_3)
    
    
    #2_4 netBeans训练集进行训练然后预测eclipse全集
    train_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_eclipse_complete'
    gs_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('enetBeans训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_2_4,predict_file_path_2_4)
    
    #2_5 netBeans训练集进行训练然后预测openOffice全集
    train_filename='tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_openOffice_complete'
    gs_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('netBeans训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_2_5,predict_file_path_2_5)
    
    
    #3_1 openOffice训练集进行训练然后预测openOffice训练集
    train_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测openOffice训练集')
    computeIndicators(gs_file_path_3_1,predict_file_path_3_1)
    
    
    #3_2 openOffice训练集进行训练然后预测openOffice测试集
    train_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测openOffice测试集')
    computeIndicators(gs_file_path_3_2,predict_file_path_3_2)
    
    
    #3_3 openOffice训练集进行训练然后预测openOffice全集
    train_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_openOffice_complete'
    gs_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_3_3,predict_file_path_3_3)
    
    #3_4 openOffice训练集进行训练然后预测eclipse全集
    train_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_eclipse_complete'
    gs_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_3_4,predict_file_path_3_4)
    
    #3_5 openOffice训练集进行训练然后预测netBeans全集
    train_filename='tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='tc_netBeans_complete'
    gs_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.scaled.txt'
    print ('openOffice训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_3_5,predict_file_path_3_5)
def computeDoc2VecTakeLabCategoricalCombined(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
	    ####TakeLab_Categorical_combined
    print ('Doc2VecTakeLabCategoricalCombined,5000 train,1:4')
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    #1_5 eclipse训练集进行训练然后预测openOffice全集
    
    #1_1 eclipse训练集进行训练然后预测eclipse训练集
    train_filename='dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_1_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('eclipse训练集进行训练然后预测eclipse训练集')
    computeIndicators(gs_file_path_1_1,predict_file_path_1_1)
    
    #1_2 eclipse训练集进行训练然后预测eclipse测试集
    train_filename='dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_1_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('eclipse训练集进行训练然后预测eclipse测试集')
    computeIndicators(gs_file_path_1_2,predict_file_path_1_2)
    
    #1_3 eclipse训练集进行训练然后预测eclipse全集
    train_filename='dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_eclipse_complete'
    gs_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_1_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('eclipse训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_1_3,predict_file_path_1_3)
    
    #1_4 eclipse训练集进行训练然后预测netBeans全集
    train_filename='dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_netBeans_complete'
    gs_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_1_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('eclipse训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_1_4,predict_file_path_1_4)
    
    
    
    #1_5 eclipse训练集进行训练然后预测openOffice全
    train_filename='dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_openOffice_complete'
    gs_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_1_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('eclipse训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_1_5,predict_file_path_1_5)
    
    
    
    #2_1 netBeans训练集进行训练然后预测netBeans训练集
    train_filename='dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_2_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('netBeans训练集进行训练然后预测netBeans训练集')
    computeIndicators(gs_file_path_2_1,predict_file_path_2_1)
    
    
    
    #2_2 netBeans训练集进行训练然后预测netBeans测试集
    train_filename='dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_2_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('netBeans训练集进行训练然后预测netBeans测试集')
    computeIndicators(gs_file_path_2_2,predict_file_path_2_2)
    
    #2_3 netBeans训练集进行训练然后预测netBeans全集
    train_filename='dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_netBeans_complete'
    gs_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_2_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('netBeans训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_2_3,predict_file_path_2_3)
    
    
    #2_4 netBeans训练集进行训练然后预测eclipse全集
    train_filename='dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_eclipse_complete'
    gs_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_2_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('enetBeans训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_2_4,predict_file_path_2_4)
    
    #2_5 netBeans训练集进行训练然后预测openOffice全集
    train_filename='dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_openOffice_complete'
    gs_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_2_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('netBeans训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_2_5,predict_file_path_2_5)
    
    
    #3_1 openOffice训练集进行训练然后预测openOffice训练集
    train_filename='dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    gs_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    predict_file_path_3_1='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('openOffice训练集进行训练然后预测openOffice训练集')
    computeIndicators(gs_file_path_3_1,predict_file_path_3_1)
    
    
    #3_2 openOffice训练集进行训练然后预测openOffice测试集
    train_filename='dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test'
    gs_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    predict_file_path_3_2='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('openOffice训练集进行训练然后预测openOffice测试集')
    computeIndicators(gs_file_path_3_2,predict_file_path_3_2)
    
    
    #3_3 openOffice训练集进行训练然后预测openOffice全集
    train_filename='dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_openOffice_complete'
    gs_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_openOffice_complete.txt'
    predict_file_path_3_3='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('openOffice训练集进行训练然后预测openOffice全集')
    computeIndicators(gs_file_path_3_3,predict_file_path_3_3)
    
    #3_4 openOffice训练集进行训练然后预测eclipse全集
    train_filename='dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_eclipse_complete'
    gs_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_eclipse_complete.txt'
    predict_file_path_3_4='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('openOffice训练集进行训练然后预测eclipse全集')
    computeIndicators(gs_file_path_3_4,predict_file_path_3_4)
    
    #3_5 openOffice训练集进行训练然后预测netBeans全集
    train_filename='dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random'
    test_filename='dtc_netBeans_complete'
    gs_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/gs_netBeans_complete.txt'
    predict_file_path_3_5='G:/code_of_zengjie/DeepLearningCodeOfXiaoJie/BugReportDeduplicate/processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/'+test_filename+'_PredictedBy_'+train_filename+'.txt'
    print ('openOffice训练集进行训练然后预测netBeans全集')
    computeIndicators(gs_file_path_3_5,predict_file_path_3_5)


if __name__ == "__main__":
    trainset_num_list=[5000,10000,15000,20000]
    trainset_num_list=[5000]
    ratio_TrueFlag=1
    ratio_FalseFlag=4
    for trainset_num in trainset_num_list:
#        computeTakeLabOnly(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        computeCategoricalOnly(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        computeTakeLabCategoricalCombined(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        computeDoc2VecTakeLabCategoricalCombined(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        
        
        
        
