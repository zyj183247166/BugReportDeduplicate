# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:06:28 2019

@author: Administrator
"""
    
def combineDoc2VecFeaturesAndTag_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
   
    
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    outputPath=filePath
    Doc2VecFeatures_train_path=outputPath
#        
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    outputPath=filePath
    Doc2VecFeatures_test_path=outputPath
    
    tag_train_path='./processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'   ##gs表示standard groud也就是标签
    tag_test_path='./processedData_2014MSR_xiaojie/gs_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    
    combined_train_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    
    scores_train= [int(x) for x in open(tag_train_path)]
    f1 = open(combined_train_path, 'w',encoding='UTF-8')
    f2 = open(Doc2VecFeatures_train_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_train[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()
        
    scores_test= [int(x) for x in open(tag_test_path)]
    f1 = open(combined_test_path, 'w',encoding='UTF-8')
    f2 = open(Doc2VecFeatures_test_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_test[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()
    

def combineDoc2VecFeaturesAndTag_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    outputPath=filePath
    Doc2VecFeatures_train_path=outputPath
#        
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    outputPath=filePath
    Doc2VecFeatures_test_path=outputPath
    
    tag_train_path='./processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'   ##gs表示standard groud也就是标签
    tag_test_path='./processedData_2014MSR_xiaojie/gs_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    
    combined_train_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    
    scores_train= [int(x) for x in open(tag_train_path)]
    f1 = open(combined_train_path, 'w',encoding='UTF-8')
    f2 = open(Doc2VecFeatures_train_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_train[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()
        
    scores_test= [int(x) for x in open(tag_test_path)]
    f1 = open(combined_test_path, 'w',encoding='UTF-8')
    f2 = open(Doc2VecFeatures_test_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_test[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()

def combineDoc2VecFeaturesAndTag_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag):

    
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    outputPath=filePath
    Doc2VecFeatures_train_path=outputPath
#        
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    outputPath=filePath
    Doc2VecFeatures_test_path=outputPath
    
    tag_train_path='./processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'   ##gs表示standard groud也就是标签
    tag_test_path='./processedData_2014MSR_xiaojie/gs_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    
    combined_train_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    
    scores_train= [int(x) for x in open(tag_train_path)]
    f1 = open(combined_train_path, 'w',encoding='UTF-8')
    f2 = open(Doc2VecFeatures_train_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_train[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()
        
    scores_test= [int(x) for x in open(tag_test_path)]
    f1 = open(combined_test_path, 'w',encoding='UTF-8')
    f2 = open(Doc2VecFeatures_test_path,'r',encoding='UTF-8')
    for num,value in enumerate(f2):
        tag=scores_test[num]
        write_content=str(tag)+value
        f1.write(write_content)
        f1.flush()
        
        
def combineDoc2VecFeaturesAndTagAndCategorical_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ###之前的Categorical特征都经过归一化的。
    
    CategoricalFeaturesAndTag_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' #我们用归一后的数据
    CategoricalFeaturesAndTag_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    
    
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    outputPath=filePath
    Doc2VecFeatures_train_path=outputPath
#        
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    outputPath=filePath
    Doc2VecFeatures_test_path=outputPath

    combined_train_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    f3 = open(combined_train_path,'w',encoding='UTF-8')
    with open(CategoricalFeaturesAndTag_train_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_train_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
    f3 = open(combined_test_path,'w',encoding='UTF-8')
    with open(CategoricalFeaturesAndTag_test_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_test_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()


def combineDoc2VecFeaturesAndTagAndCategorical_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ###之前的Categorical特征都经过归一化的。
    
    CategoricalFeaturesAndTag_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' #我们用归一后的数据
    CategoricalFeaturesAndTag_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    
    
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    outputPath=filePath
    Doc2VecFeatures_train_path=outputPath
#        
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    outputPath=filePath
    Doc2VecFeatures_test_path=outputPath

    combined_train_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    f3 = open(combined_train_path,'w',encoding='UTF-8')
    with open(CategoricalFeaturesAndTag_train_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_train_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
    f3 = open(combined_test_path,'w',encoding='UTF-8')
    with open(CategoricalFeaturesAndTag_test_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_test_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()

def combineDoc2VecFeaturesAndTagAndCategorical_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ###之前的Categorical特征都经过归一化的。
    
    CategoricalFeaturesAndTag_train_path='./processedData_2014MSR_xiaojie/categorical_only/co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt' #我们用归一后的数据
    CategoricalFeaturesAndTag_test_path='./processedData_2014MSR_xiaojie/categorical_only/co_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    
    
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    outputPath=filePath
    Doc2VecFeatures_train_path=outputPath
#        
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    outputPath=filePath
    Doc2VecFeatures_test_path=outputPath

    combined_train_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    f3 = open(combined_train_path,'w',encoding='UTF-8')
    with open(CategoricalFeaturesAndTag_train_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_train_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
    f3 = open(combined_test_path,'w',encoding='UTF-8')
    with open(CategoricalFeaturesAndTag_test_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_test_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()


def combineTCAndTagAnddoc2vec_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ###之前的Categorical特征都经过归一化的。
    
    takelab_categorical_combined_AndTag_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt'  #我们用归一后的数据
    takelab_categorical_combined_AndTag_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    
    
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    outputPath=filePath
    Doc2VecFeatures_train_path=outputPath
#        
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    outputPath=filePath
    Doc2VecFeatures_test_path=outputPath

    combined_train_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    f3 = open(combined_train_path,'w',encoding='UTF-8')
    with open(takelab_categorical_combined_AndTag_train_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_train_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
    f3 = open(combined_test_path,'w',encoding='UTF-8')
    with open(takelab_categorical_combined_AndTag_test_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_test_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()




def combineTCAndTagAnddoc2vec_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ###之前的Categorical特征都经过归一化的。
    
    takelab_categorical_combined_AndTag_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt'  #我们用归一后的数据
    takelab_categorical_combined_AndTag_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    
    
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    outputPath=filePath
    Doc2VecFeatures_train_path=outputPath
#        
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    outputPath=filePath
    Doc2VecFeatures_test_path=outputPath

    combined_train_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    f3 = open(combined_train_path,'w',encoding='UTF-8')
    with open(takelab_categorical_combined_AndTag_train_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_train_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
    f3 = open(combined_test_path,'w',encoding='UTF-8')
    with open(takelab_categorical_combined_AndTag_test_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_test_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
                
                
def combineTCAndTagAnddoc2vec_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    ###之前的Categorical特征都经过归一化的。
    
    takelab_categorical_combined_AndTag_train_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.scaled.txt'  #我们用归一后的数据
    takelab_categorical_combined_AndTag_test_path='./processedData_2014MSR_xiaojie/takelab_categorical_combined/tc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.scaled.txt' 
    
    
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    outputPath=filePath
    Doc2VecFeatures_train_path=outputPath
#        
    filePath='./processedData_2014MSR_xiaojie/doc2vecSimilarity_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    outputPath=filePath
    Doc2VecFeatures_test_path=outputPath

    combined_train_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    combined_test_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    
    f3 = open(combined_train_path,'w',encoding='UTF-8')
    with open(takelab_categorical_combined_AndTag_train_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_train_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()
    f3 = open(combined_test_path,'w',encoding='UTF-8')
    with open(takelab_categorical_combined_AndTag_test_path, 'r',encoding='UTF-8') as f1:
        with open(Doc2VecFeatures_test_path,'r',encoding='UTF-8') as f2:
            for x,y in zip(f1.readlines(),f2.readlines()):
                x=x.strip(' ')
                x=x.strip('\n')
                y=y.strip(' ')
                y=y.strip('\n')
#                print (y)
                write_content=x+y
                f3.write(write_content)
                f3.write('\n')
                f3.flush()

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

def get_eclipse_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    do_train_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    do_test_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    do_complete_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_eclipse_complete.txt'  
    combineTwoTxts(do_train_path,do_test_path,do_complete_path)

    dc_train_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    dc_test_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    dc_complete_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_eclipse_complete.txt'  
    combineTwoTxts(dc_train_path,dc_test_path,dc_complete_path)
    
    dtc_train_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    dtc_test_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    dtc_complete_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_eclipse_complete.txt'  
    combineTwoTxts(dtc_train_path,dtc_test_path,dtc_complete_path)

def get_netBeans_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    do_train_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    do_test_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    do_complete_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_netBeans_complete.txt'  
    combineTwoTxts(do_train_path,do_test_path,do_complete_path)

    dc_train_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    dc_test_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    dc_complete_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_netBeans_complete.txt'  
    combineTwoTxts(dc_train_path,dc_test_path,dc_complete_path)
    
    dtc_train_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    dtc_test_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    dtc_complete_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_netBeans_complete.txt'  
    combineTwoTxts(dtc_train_path,dtc_test_path,dtc_complete_path)
    
    

def get_openOffice_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    do_train_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    do_test_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    do_complete_path='./processedData_2014MSR_xiaojie/doc2vec_only/do_openOffice_complete.txt'  
    combineTwoTxts(do_train_path,do_test_path,do_complete_path)

    dc_train_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    dc_test_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    dc_complete_path='./processedData_2014MSR_xiaojie/doc2vec_categorical_combined/dc_openOffice_complete.txt'  
    combineTwoTxts(dc_train_path,dc_test_path,dc_complete_path)
    
    dtc_train_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt' 
    dtc_test_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt' 
    dtc_complete_path='./processedData_2014MSR_xiaojie/doc2vec_takelab_categorical_combined/dtc_openOffice_complete.txt'  
    combineTwoTxts(dtc_train_path,dtc_test_path,dtc_complete_path)
    

if __name__ == "__main__":
    trainset_num_list=[5000,10000,15000,20000]
#    test()
    trainset_num_list=[5000]
    ratio_TrueFlag=1
    ratio_FalseFlag=4
    for trainset_num in trainset_num_list:
        ###先生成doc2vec特征的数据集，输出到doc2vec_only
        combineDoc2VecFeaturesAndTag_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        combineDoc2VecFeaturesAndTag_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        combineDoc2VecFeaturesAndTag_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
            
        
        ###再生成doc2vec特征融合Categorical特征的数据集，输出到doc2vec_categorical_combined
        combineDoc2VecFeaturesAndTagAndCategorical_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        combineDoc2VecFeaturesAndTagAndCategorical_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        combineDoc2VecFeaturesAndTagAndCategorical_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        ###再生成doc2vec特征融合TakeLab特征和Categorical的数据集，输出到doc2vec_takelab_categorical_combined目录
        combineTCAndTagAnddoc2vec_Eclipse(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        combineTCAndTagAnddoc2vec_netBeans(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        combineTCAndTagAnddoc2vec_openOffice(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
        #生成三种特征三大项目的全集文件
        get_eclipse_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        get_netBeans_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        get_openOffice_complete(trainset_num,ratio_TrueFlag,ratio_FalseFlag)