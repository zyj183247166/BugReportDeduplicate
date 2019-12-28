#python example to train doc2vec model (with or without pre-trained word embeddings)

import gensim.models as gm
import logging
import time
import codecs
import gensim.models as g
import codecs
import numpy
import numpy as np
import nltk
import pickle
def simlarityCalu(vector1, vector2):
    vector1Mod = np.sqrt(vector1.dot(vector1))
    vector2Mod = np.sqrt(vector2.dot(vector2))
    if vector2Mod != 0 and vector1Mod != 0:
        simlarity = (vector1.dot(vector2)) / (vector1Mod * vector2Mod)
    else:
        simlarity = 0
    return simlarity
def save_to_pkl(python_content, pickle_name):
    with open(pickle_name, 'wb') as pickle_f:
        pickle.dump(python_content, pickle_f)
def read_from_pkl(pickle_name):
    with open(pickle_name, 'rb') as pickle_f:
        python_content = pickle.load(pickle_f)
    return python_content

def process_eclipse_ForDoc2VecSimilarity(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    #读入doc2vec模型
    saved_path = "./processedData_2014MSR_xiaojie/doc2vec_model/eclipse_text_for_trainingDoc2Vec.model.bin"
#    saved_path = "./processedData_2014MSR_xiaojie/doc2vec_model/doc2vec_test.model.bin"
    model = gm.Doc2Vec.load(saved_path)
    
    #读入训练和测试数据的pairs
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_Eclipse_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    trainPairs=read_from_pkl(all_dataset_name1_forTrain)
    testPairs=read_from_pkl(all_dataset_name1_forTest)
    trainPairs_num=len(trainPairs)
    testPairs_num=len(testPairs)
    print ("eclipse训练数据一共{}组".format(trainPairs_num))
    print ("eclipse测试数据一共{}组".format(testPairs_num))
    
    #读入bug_id到lineNumber的映射文件。LineNumber对应Doc2Vec训练文件的行号
    bug_id_Map_lineNumber_pkl='./processedData_2014MSR_xiaojie/bug_id_Map_lineNumber_pkl/eclipse_bug_id_Map_lineNumber.pkl'
    bug_id_Map_lineNumber_dict=read_from_pkl(bug_id_Map_lineNumber_pkl)
    
    ##输出文件
    train_code2vecFeatures_text='./processedData_2014MSR_xiaojie/doc2vecSimilarity_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    test_code2vecFeatures_text='./processedData_2014MSR_xiaojie/doc2vecSimilarity_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    f_train=open(train_code2vecFeatures_text, 'w',encoding='UTF-8')
    f_test=open(test_code2vecFeatures_text, 'w',encoding='UTF-8')
    index=0
    for key in trainPairs.keys():
        if index%1000==0:
            print ('处理第{}对训练数据'.format(index))
        bug1=key[0]
        bug2=key[1]
        lineNumber1=bug_id_Map_lineNumber_dict[bug1] #从0开始编号
        lineNumber2=bug_id_Map_lineNumber_dict[bug2]
        vector1=model.docvecs[lineNumber1] #根据行号取出向量。
        vector2=model.docvecs[lineNumber2]
#        print (simlarityCalu(vector1,vector2))
        simlarity=simlarityCalu(vector1,vector2)
        f_train.write(' 28:%f' % (simlarity))
        f_train.write('\n')
        f_train.flush()
        index=index+1
    index=0
    for key in testPairs.keys():
        if index%1000==0:
            print ('处理第{}对训练数据'.format(index))
        bug1=key[0]
        bug2=key[1]
        lineNumber1=bug_id_Map_lineNumber_dict[bug1] #从0开始编号
        lineNumber2=bug_id_Map_lineNumber_dict[bug2]
        vector1=model.docvecs[lineNumber1] #根据行号取出向量。
        vector2=model.docvecs[lineNumber2]
        simlarity=simlarityCalu(vector1,vector2)
        f_test.write(' 28:%f' % (simlarity))
        f_test.write('\n')
        f_test.flush()
        index=index+1

def process_openOffice_ForDoc2VecSimilarity(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    #读入doc2vec模型
    saved_path = "./processedData_2014MSR_xiaojie/doc2vec_model/openOffice_text_for_trainingDoc2Vec.model.bin"
#    saved_path = "./processedData_2014MSR_xiaojie/doc2vec_model/doc2vec_test.model.bin"
    model = gm.Doc2Vec.load(saved_path)
    
    #读入训练和测试数据的pairs
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_openOffice_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    trainPairs=read_from_pkl(all_dataset_name1_forTrain)
    testPairs=read_from_pkl(all_dataset_name1_forTest)
    trainPairs_num=len(trainPairs)
    testPairs_num=len(testPairs)
    print ("openOffice训练数据一共{}组".format(trainPairs_num))
    print ("openOffice测试数据一共{}组".format(testPairs_num))
    
    #读入bug_id到lineNumber的映射文件。LineNumber对应Doc2Vec训练文件的行号
    bug_id_Map_lineNumber_pkl='./processedData_2014MSR_xiaojie/bug_id_Map_lineNumber_pkl/openOffice_bug_id_Map_lineNumber.pkl'
    bug_id_Map_lineNumber_dict=read_from_pkl(bug_id_Map_lineNumber_pkl)
    
    ##输出文件
    train_code2vecFeatures_text='./processedData_2014MSR_xiaojie/doc2vecSimilarity_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    test_code2vecFeatures_text='./processedData_2014MSR_xiaojie/doc2vecSimilarity_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    f_train=open(train_code2vecFeatures_text, 'w',encoding='UTF-8')
    f_test=open(test_code2vecFeatures_text, 'w',encoding='UTF-8')
    index=0
    for key in trainPairs.keys():
        if index%1000==0:
            print ('处理第{}对训练数据'.format(index))
        bug1=key[0]
        bug2=key[1]
        lineNumber1=bug_id_Map_lineNumber_dict[bug1] #从0开始编号
        lineNumber2=bug_id_Map_lineNumber_dict[bug2]
        vector1=model.docvecs[lineNumber1] #根据行号取出向量。
        vector2=model.docvecs[lineNumber2]
#        print (simlarityCalu(vector1,vector2))
        simlarity=simlarityCalu(vector1,vector2)
        f_train.write(' 28:%f' % (simlarity))
        f_train.write('\n')
        f_train.flush()
        index=index+1
    index=0
    for key in testPairs.keys():
        if index%1000==0:
            print ('处理第{}对训练数据'.format(index))
        bug1=key[0]
        bug2=key[1]
        lineNumber1=bug_id_Map_lineNumber_dict[bug1] #从0开始编号
        lineNumber2=bug_id_Map_lineNumber_dict[bug2]
        vector1=model.docvecs[lineNumber1] #根据行号取出向量。
        vector2=model.docvecs[lineNumber2]
        simlarity=simlarityCalu(vector1,vector2)
        f_test.write(' 28:%f' % (simlarity))
        f_test.write('\n')
        f_test.flush()
        index=index+1

def process_netBeans_ForDoc2VecSimilarity(trainset_num,ratio_TrueFlag,ratio_FalseFlag):
    #读入doc2vec模型
    saved_path = "./processedData_2014MSR_xiaojie/doc2vec_model/netBeans_text_for_trainingDoc2Vec.model.bin"
#    saved_path = "./processedData_2014MSR_xiaojie/doc2vec_model/doc2vec_test.model.bin"
    model = gm.Doc2Vec.load(saved_path)
    
    #读入训练和测试数据的pairs
    all_dataset_name1_forTrain='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'.pkl'
    all_dataset_name1_forTest='./processedData_2014MSR_xiaojie/all_pairs_id_train_netBeans_XIAOJIE_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_'+'test'+'.pkl'
    trainPairs=read_from_pkl(all_dataset_name1_forTrain)
    testPairs=read_from_pkl(all_dataset_name1_forTest)
    trainPairs_num=len(trainPairs)
    testPairs_num=len(testPairs)
    print ("netBeans训练数据一共{}组".format(trainPairs_num))
    print ("netBeans测试数据一共{}组".format(testPairs_num))
    
    #读入bug_id到lineNumber的映射文件。LineNumber对应Doc2Vec训练文件的行号
    bug_id_Map_lineNumber_pkl='./processedData_2014MSR_xiaojie/bug_id_Map_lineNumber_pkl/netBeans_bug_id_Map_lineNumber.pkl'
    bug_id_Map_lineNumber_dict=read_from_pkl(bug_id_Map_lineNumber_pkl)
    
    ##输出文件
    train_code2vecFeatures_text='./processedData_2014MSR_xiaojie/doc2vecSimilarity_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
    test_code2vecFeatures_text='./processedData_2014MSR_xiaojie/doc2vecSimilarity_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
    f_train=open(train_code2vecFeatures_text, 'w',encoding='UTF-8')
    f_test=open(test_code2vecFeatures_text, 'w',encoding='UTF-8')
    index=0
    for key in trainPairs.keys():
        if index%1000==0:
            print ('处理第{}对训练数据'.format(index))
        bug1=key[0]
        bug2=key[1]
        lineNumber1=bug_id_Map_lineNumber_dict[bug1] #从0开始编号
        lineNumber2=bug_id_Map_lineNumber_dict[bug2]
        vector1=model.docvecs[lineNumber1] #根据行号取出向量。
        vector2=model.docvecs[lineNumber2]
#        print (simlarityCalu(vector1,vector2))
        simlarity=simlarityCalu(vector1,vector2)
        f_train.write(' 28:%f' % (simlarity))
        f_train.write('\n')
        f_train.flush()
        index=index+1
    index=0
    for key in testPairs.keys():
        if index%1000==0:
            print ('处理第{}对训练数据'.format(index))
        bug1=key[0]
        bug2=key[1]
        lineNumber1=bug_id_Map_lineNumber_dict[bug1] #从0开始编号
        lineNumber2=bug_id_Map_lineNumber_dict[bug2]
        vector1=model.docvecs[lineNumber1] #根据行号取出向量。
        vector2=model.docvecs[lineNumber2]
        simlarity=simlarityCalu(vector1,vector2)
        f_test.write(' 28:%f' % (simlarity))
        f_test.write('\n')
        f_test.flush()
        index=index+1
if __name__ == '__main__':
#    
    trainset_num_list=[5000]
    ratio_TrueFlag=1
    ratio_FalseFlag=4
    for trainset_num in trainset_num_list:
        process_eclipse_ForDoc2VecSimilarity(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        process_openOffice_ForDoc2VecSimilarity(trainset_num,ratio_TrueFlag,ratio_FalseFlag)
#        process_netBeans_ForDoc2VecSimilarity(trainset_num,ratio_TrueFlag,ratio_FalseFlag)



