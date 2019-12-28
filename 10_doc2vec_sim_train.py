# @author：DerrickOzil
# date: 2017-09-04
# -*- coding: utf-8 -*-
import sys 
import gensim
import os
from gensim.models.doc2vec import Doc2Vec


TaggededDocument = gensim.models.doc2vec.TaggedDocument

#获取语料集合
def get_datasest(filename,cate,x_train=[]):
    with open(filename, 'rb') as f:
        print ("Reading "+filename+" .......")
        docs = f.readlines()
    x_train = []
    for doc in docs:
        id,text = doc.split("\t")               #切分文档id与内容
        word_list = text.split(' ')
        length = len(word_list)
        word_list[length-1] = word_list[length-1].strip()
        document = TaggededDocument(word_list, tags=[str(cate)+':'+str(id)])
        x_train.append(document)
    return x_train

#增量式训练模型
def incrementaTraining(model_path,incr_corpuses):

    for corpus,cate in incr_corpuses.items():
        #load corpus
        x_train = []
        x_train = get_datasest(corpus,cate,x_train)

        if os.path.exists(model_path) and os.path.isfile(model_path):   #如果已经有现成model，则load   
            # load model                                                                                                                                                                                                                                                                         
            model = Doc2Vec.load(model_path)    
            print (corpus + " is ready for training!!!")
        else:                                        #如果没有model，初始化一个
            # init model
            print (corpus + " is initating training-model!!!")
            model = Doc2Vec(x_train, min_count=1, window=3, size=500, sample=1e-3, negative=5, workers=4)

        tte = model.corpus_count+len(x_train)               #total_examples参数更新
        model.train(x_train,total_examples=tte,epochs=70)      #完成增量训练
        print (model.corpus_count)
        
        
        
        
        model.save(model_path)        #保存模型
    return

if __name__ == '__main__':
    model_path = "model/model_dm"
    incr_corpuses = {"word_segs_1":1,"word_segs_2":2,"word_segs_3":3}
    incrementaTraining(model_path,incr_corpuses)
    print ("====over===")


