#python example to train doc2vec model (with or without pre-trained word embeddings)

import gensim.models as gm
import logging
import time
import codecs
def trainModel(train_corpus,save_model_name,saved_path,test_docs,test_lineNumber,log_text):
    #doc2vec 参数
    vector_size = 256 # 词向量长度，默认为100
    window_size = 15 # 窗口大小，表示当前词与预测词在一个句子中的最大距离是多少
    min_count = 1 #可以对字典做截断. 词频少于min_count次数的单词会被丢弃掉, 默认值为5
    sampling_threshold = 1e-5 # 高频词汇的随机降采样的配置阈值，默认为1e-3，范围是(0,1e-5)
    negative_size = 5 #如果>0,则会采用negativesampling，用于设置多少个noise words（一般是5-20）
    #train_epoch = 100 # 迭代次数
#    train_epoch = 100 # 迭代次数
    train_epoch = 100 # 迭代次数
    dm = 0 #0 = dbow; 1 = dmpv
    worker_count = 1 # 用于控制训练的并行数
    
    #pretrained word embeddings
    #pretrained_emb = "toy_data/pretrained_word_embeddings.txt" #None if use without pretrained embeddings
    pretrained_emb=None
    
    #获取日志信息
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    
    #训练 doc2vec 模型
    start = time.time()
    f_write=open(log_text, 'w',encoding='UTF-8')
    ####单纯训练train_epoch轮
#    docs = gm.doc2vec.TaggedLineDocument(train_corpus) #加载语料
#    model = gm.Doc2Vec(docs, size=vector_size, window=window_size, min_count=min_count, sample=sampling_threshold, workers=worker_count,\
#                       hs=0, dm=dm, negative=negative_size, dbow_words=1, dm_concat=1, pretrained_emb=pretrained_emb, iter=train_epoch)
#    model.save(saved_path)
    #保存模型
    
    
    ####训练轮数取决于测试样本（来源于训练数据），然后排名第一的相似度是否达到了0.99，并且是指定编号。
    similarity=0.0
    init=True
    index=0
#

    while(similarity<0.99 and index <10):# 因为有一些无论训练多少轮，也无法达到99%。所以，index应该设一个上限。
        index=index+1
        print ('第{}次训练:\n'.format(index))
        if init==True:###第一次训练
            docs = gm.doc2vec.TaggedLineDocument(train_corpus) #加载语料
            model = gm.Doc2Vec(docs, size=vector_size, window=window_size, min_count=min_count, sample=sampling_threshold, workers=worker_count,\
                           hs=0, dm=dm, negative=negative_size, dbow_words=1, dm_concat=1, pretrained_emb=pretrained_emb, iter=train_epoch)
            model.save(saved_path)
            init=False
        else:###增量训练
            model = gm.Doc2Vec.load(saved_path)
            docs = gm.doc2vec.TaggedLineDocument(train_corpus) #加载语料\
            
    #        tte = model.corpus_count+len(docs)               #total_examples参数更新
    #        model.train(docs,total_examples=tte,epochs=train_epoch)      #完成增量训练
            
            model.train(docs,total_examples=model.corpus_count,epochs=train_epoch)      #完成增量训练
            model.save(saved_path)
        ###加载模型，完成样本的推测
        m = gm.Doc2Vec.load(saved_path)
        test_docs = "./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/eclipse_test.txt" # test.txt为需要向量化的文本
        test_docs = [x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines()]\
        # 超参
        start_alpha = 0.01
        infer_epoch = 1000
        for d in test_docs:
            vector=m.infer_vector(d, alpha=start_alpha, steps=infer_epoch)
            sims=m.docvecs.most_similar([vector], topn=5)
            (lineNumber,sim)=sims[0]
            similarity=sim
            print ('similarity:{}\n'.format(similarity))
            print ('lineNumber:{}\n'.format(lineNumber))
            f_write.write('similarity:{}\n'.format(similarity))
            f_write.write('lineNumber:{}\n'.format(lineNumber))
            f_write.write('index:{}\n'.format(index))
            f_write.flush()
            if (lineNumber!=test_lineNumber):
                print ('error!\n')
            break
        
    end = time.time()
    realEpoch=index*train_epoch
    
    print("训练时间:%.2f秒\n"%(end-start))
    print("总训练轮数:{}，训练{}次\n".format(realEpoch,index))
    f_write.write("训练时间:%.2f秒\n"%(end-start))
    f_write.write("总训练轮数:{}，训练{}次\n".format(realEpoch,index))
    f_write.flush()
    
    #488.79秒
if __name__ == '__main__':
    #输入语料库
    #train_corpus = "./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/testText_doc2vec_xiaojie.txt"
    ##模型输出
    #save_model_name = 'doc2vec_test.model'
    #saved_path = "./processedData_2014MSR_xiaojie/doc2vec_model/doc2vec_test.model.bin"
    
    
    ###训练eclipse
    #输入语料库
    train_corpus = "./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/eclipse_text_for_trainingDoc2Vec.txt"
    #模型输出
    save_model_name = 'eclipse_text_for_trainingDoc2Vec.model'
    saved_path = "./processedData_2014MSR_xiaojie/doc2vec_model/eclipse_text_for_trainingDoc2Vec.model.bin"
    
    log_text="./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/eclipse_log.txt" # test.txt为需要向量化的文本
    test_docs="./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/eclipse_test.txt"
    test_lineNumber=9
    trainModel(train_corpus,save_model_name,saved_path,test_docs,test_lineNumber,log_text)
    

    ###训练netBeans
#    train_corpus = "./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/netBeans_text_for_trainingDoc2Vec.txt"
#    #模型输出
#    save_model_name = 'netBeans_text_for_trainingDoc2Vec.model'
#    saved_path = "./processedData_2014MSR_xiaojie/doc2vec_model/netBeans_text_for_trainingDoc2Vec.model.bin"
#    
#    log_text="./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/log_netBeans.txt" # test.txt为需要向量化的文本
#    test_docs="./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/netBeans_test.txt"
#    test_lineNumber= 
#    trainModel(train_corpus,save_model_name,saved_path,test_docs,test_lineNumber,log_text)

    
    
    ###训练openOffice
#    train_corpus = "./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/openOffice_text_for_trainingDoc2Vec.txt"
#    #模型输出
#    save_model_name = 'openOffice_text_for_trainingDoc2Vec.model'
#    saved_path = "./processedData_2014MSR_xiaojie/doc2vec_model/openOffice_text_for_trainingDoc2Vec.model.bin"
#    
#    log_text="./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/log_openOffice.txt" # test.txt为需要向量化的文本
#    test_docs="./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/openOffice_test.txt"
#    test_lineNumber=44 #编号从0开始。
#    trainModel(train_corpus,save_model_name,saved_path,test_docs,test_lineNumber,log_text)



