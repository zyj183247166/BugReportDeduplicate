import gensim.models as g
import codecs
import numpy
import numpy as np
import nltk
model_path = 'D:/alreadyTrainedModel/enwiki_dbow/doc2vec.bin'
start_alpha = 0.01
infer_epoch = 1000
docvec_size = 192


def simlarityCalu(vector1, vector2):
    vector1Mod = np.sqrt(vector1.dot(vector1))
    vector2Mod = np.sqrt(vector2.dot(vector2))
    if vector2Mod != 0 and vector1Mod != 0:
        simlarity = (vector1.dot(vector2)) / (vector1Mod * vector2Mod)
    else:
        simlarity = 0
    return simlarity


def doc2vec(file_name, model):
    import jieba
    doc = [w for x in codecs.open(file_name, 'r', 'utf-8').readlines() for w in jieba.cut(x.strip())]
#    print (doc)
    doc_vec_all = model.infer_vector(doc, alpha=start_alpha, steps=infer_epoch)
    
#    sims = model.docvecs.most_similar([doc_vec_all], topn=10)
    sims = model.most_similar("party", topn=10)
    for count, sim in sims:
#        sentence = str(x_train[count])
        # sentence = x_train[count]
        # print('sentence:'+sentence)
        # print('sim:'+str(sim))
        print (count,sim)
#        print(sentence, sim, len(sentence))
        pass
    return doc_vec_all

def test():
    #python example to infer document vectors from trained doc2vec model
    import gensim.models as gm
    import codecs
    import numpy as np
    
#parameters
    model = "toy_data/model/wiki_en_doc2vec.model.bin"
    test_docs = "toy_data/test.txt" # test.txt为需要向量化的文本
    output_file = "toy_data/test_vector.txt" #得到测试文本的每一行的向量表示
    
    # 超参
    start_alpha = 0.01
    infer_epoch = 1000
    
    #加载模型
    m = gm.Doc2Vec.load(model)
    test_docs = [x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines()]
    
    #infer test vectors
    output = open(output_file, "w")
    for d in test_docs:
        output.write(" ".join([str(x) for x in m.infer_vector(d, alpha=start_alpha, steps=infer_epoch)]) + "\n")
    output.flush()
    output.close()
    #print(len(test_docs)) #测试文本的行数
    
    print(m.most_similar("party", topn=5)) # 找到与party单词最相近的前5个
    
    #保存为numpy形式
    test_vector = np.loadtxt('toy_data/test_vector.txt')
    test_vector = np.save('toy_data/test_vector', test_vector)


def processTextPairsForSimilarity(filePath,outputPath,model):
    test_docs = [x.strip() for x in codecs.open(filePath, "r", "utf-8").readlines()]
    f = open(outputPath, 'w',encoding='UTF-8')
    index=0
    for item in test_docs:
        print (index+1)
        index=index+1
        items=item.split('\t')
        document1=items[0]
        document2=items[1]
        document1_doc=nltk.word_tokenize(document1)
        document2_doc=nltk.word_tokenize(document2)
        document1_doc_vec=model.infer_vector(document1_doc, alpha=start_alpha, steps=infer_epoch)
        document2_doc_vec=model.infer_vector(document2_doc, alpha=start_alpha, steps=infer_epoch)
#        print (document1_doc)
#        print (document2_doc)
        sim=simlarityCalu(document1_doc_vec, document2_doc_vec)
#        print (sim)
        f.write(' 28:%f' % (sim))
        f.write('\n')
        f.flush()
        
import time
import random
from threading import Thread
#multiprocess总是有错误
#def run(name,trainset_num,ratio_TrueFlag,ratio_FalseFlag,trainOrTest,model_path):
#    print('{},{} runing\n'.format(name,trainOrTest))
#    model = g.Doc2Vec.load(model_path)
#    if trainOrTest=='train':
#        filePath='./processedData_2014MSR_xiaojie/textForTakeLab_to_'+name+'_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
#        outputPath=filePath+'.doc2vecSimilarity'
#    elif trainOrTest=='test':
#        filePath='./processedData_2014MSR_xiaojie/textForTakeLab_to_'+name+'_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
#        outputPath=filePath+'.doc2vecSimilarity'
#    else:
#        print ('wrong\n')
#    try:
#        processTextPairsForSimilarity(filePath,outputPath,model)
#    except MemoryError:
#        print ('MemoryError {},{} runing\n'.format(name,trainOrTest))
#        
#    print('%s running end\n' %name)


def printCMD(name,trainset_num,ratio_TrueFlag,ratio_FalseFlag,trainOrTest,model_path):
    if trainOrTest=='train':
        filePath='./processedData_2014MSR_xiaojie/textForTakeLab_to_'+name+'_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
        outputPath=filePath+'.doc2vecSimilarity'
    elif trainOrTest=='test':
        filePath='./processedData_2014MSR_xiaojie/textForTakeLab_to_'+name+'_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
        outputPath=filePath+'.doc2vecSimilarity'
    else:
        print ('wrong\n')
    print ('./8_doc2vec_sim.py '+filePath+' '+outputPath)

import sys
if __name__ == '__main__':
    
####################程序中执行模式
    model = g.Doc2Vec.load(model_path)
    p1 = './data/P1.txt'
    p2 = './data/P2.txt'
    P1_doc2vec = doc2vec(p1, model)
    P2_doc2vec = doc2vec(p2, model)
    print(simlarityCalu(P1_doc2vec, P2_doc2vec))
    
#    trainset_num_list=[5000]
#    ratio_TrueFlag=1
#    ratio_FalseFlag=4
#    for trainset_num in trainset_num_list:
        ###eclipse
        
#        filePath='./processedData_2014MSR_xiaojie/textForTakeLab_to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
#        outputPath=filePath+'.doc2vecSimilarity'
#        processTextPairsForSimilarity(filePath,outputPath,model)
#        
#        filePath='./processedData_2014MSR_xiaojie/textForTakeLab_to_eclipse_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
#        outputPath=filePath+'.doc2vecSimilarity'
#        processTextPairsForSimilarity(filePath,outputPath,model)
#        
#        
#        ###netBeans
#        filePath='./processedData_2014MSR_xiaojie/textForTakeLab_to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
#        outputPath=filePath+'.doc2vecSimilarity'
#        processTextPairsForSimilarity(filePath,outputPath,model)
#        
#        filePath='./processedData_2014MSR_xiaojie/textForTakeLab_to_netBeans_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
#        outputPath=filePath+'.doc2vecSimilarity'
#        ###先处理训练数据
#        processTextPairsForSimilarity(filePath,outputPath,model)
#
#        ###openOffice
#        filePath='./processedData_2014MSR_xiaojie/textForTakeLab_to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random.txt'
#        outputPath=filePath+'.doc2vecSimilarity'
#        processTextPairsForSimilarity(filePath,outputPath,model)
#        
#        filePath='./processedData_2014MSR_xiaojie/textForTakeLab_to_openOffice_'+str(trainset_num)+'_'+str(ratio_TrueFlag)+'_'+str(ratio_FalseFlag)+'_train_random_test.txt'
#        outputPath=filePath+'.doc2vecSimilarity'
#        ###先处理训练数据
#        processTextPairsForSimilarity(filePath,outputPath,model)
        
        
        ###并发 ###这种并发实际上，更慢。我们弃之不用。
#        thread_array = {}
#        start_time = time.time()
#        
#        t = Thread(target=run,args=('eclipse',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'train',model_path))
#        t.start()
#        thread_array[0] = t
#        
#        t = Thread(target=run,args=('eclipse',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'test',model_path))
#        t.start()
#        thread_array[1] = t
#        
#        t = Thread(target=run,args=('netBeans',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'train',model_path))
#        t.start()
#        thread_array[2] = t
#        
#        t = Thread(target=run,args=('netBeans',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'test',model_path))
#        t.start()
#        thread_array[3] = t
#        
#        t = Thread(target=run,args=('openOffice',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'train',model_path))
#        t.start()
#        thread_array[4] = t
#        
#        t = Thread(target=run,args=('openOffice',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'test',model_path))
#        t.start()
#        thread_array[5] = t
#        
#        for i in range(6):
#            print (i)
#            thread_array[i].join()
#        end_time = time.time()
#        print("Total time: {}\n".format(end_time - start_time))
        
        ###输出在命令行
#        printCMD('eclipse',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'train',model_path)
#        printCMD('eclipse',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'test',model_path)
#        printCMD('netBeans',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'train',model_path)
#        printCMD('netBeans',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'test',model_path)
#        printCMD('openOffice',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'train',model_path)
#        printCMD('openOffice',trainset_num,ratio_TrueFlag,ratio_FalseFlag,'test',model_path)

####################命令行中执行方式
        ###打印出命令行，我们在命令行中同时启动多个程序。
#    if len(sys.argv) != 3 :
#        print ("Usage: ")
#        print ('%s input.txt output.txt' % sys.argv[0])
#        exit(1)
##    
#    model = g.Doc2Vec.load(model_path)
#    filePath=sys.argv[1]
#    outputPath=sys.argv[2]
#    processTextPairsForSimilarity(filePath,outputPath,model)

#    #    if len(sys.argv) >= 3:
#    #        scores = [float(x) for x in open(sys.argv[2])]
#    #    if len(sys.argv) >= 4:
#    #        scores = [float(x) for x in open(sys.argv[3])]
#        if len(sys.argv) >= 4: #如果标签是整数的话，就应该用int
#            scores = [int(x) for x in open(sys.argv[3])]
#        f_target=open(sys.argv[2], 'w')
#    #    xxx=load_data(sys.argv[1])#小杰测试

