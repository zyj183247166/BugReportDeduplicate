# coding=utf-8

import gensim
import os
from gensim.models.doc2vec import Doc2Vec,LabeledSentence
from pprint import pprint


# 要实现的功能：利用给定的语料训练模型，再利用模型计算任意文本的相似度


# 第一步，训练模型前，先将语料整理成规定的形式，这里用到TaggedDocument模型

TaggededDocument = gensim.models.doc2vec.TaggedDocument # 输入输出内容都为 词袋 + tag列表， 作用是记录每一篇博客的大致内容，并给该博客编号
list_name = os.listdir("/home/wayne/2017SMP/fenci2/testingcorpus")  # 用于训练模型的语料先进行预处理
def get_trainset():
    x_train = [] # 用来存放语料
    index = 0    # 每一篇博客需要一个对应的编号
    doc_dict = {}  # 由编号映射博客ID的字典
    for name in list_name:
        user_file = '/home/wayne/2017SMP/fenci2/testingcorpus/'+name
        # 语料预处理
        data = open(user_file).read()
        data = data.replace('\n', '').replace('  ', ' ')
        data = data.lower()
        words = data.split(" ")
        x_train.append(TaggededDocument(words, tags=[index]))
        doc_dict[index] = name.strip(".txt")
        print ('append ok!')
        index += 1
    return x_train, doc_dict # doc_dict的key和value 分别为编号和对应博客ID


# 第二步，初始化训练模型的参数，再保存训练结果以释放内存

def train(x_train, size=500, epoch_num=1):
    model_dm = gensim.models.Doc2Vec(x_train, min_count=1, window=3, size=size, sample=1e-3, negative=5, workers=4)  # 模型的初始化，设置参数
    #  提供x_train可初始化, min_cout 忽略总频率低于这个的所有单词, window 预测的词与上下文词之间最大的距离, 用于预测  size 特征向量的维数 negative 接受杂质的个数 worker 工作模块数
    model_dm.train(x_train, total_examples=model_dm.corpus_count, epochs=70) # corpus_count是文件个数  epochs 训练次数
    model_dm.save('/home/wayne/2017SMP/fenci2/testingcorpus/doc2vecmodel')  # 保存模型训练结果，释放内存空间，后续可用load加载
    return model_dm


#第三步，利用训练好的模型计算一个博客内容的相似度，这里用test_text做一个测试

def test():
    model_dm = Doc2Vec.load("/home/wayne/2017SMP/fenci2/doc2vecmodel")  # 加载训练的模型   model_dm输出类似Doc2Vec(dm/m,d500,n5,w3,s0.001,t4)
    test_text = ["web", "json"]   # 测试用的博客（假设已经过预处理）# 将test_text转换成相关矩阵

    sims = model_dm.docvecs.most_similar([inferred_vector_dm], topn=10)   # topn 降序显示相似度最大的10个taggeddocument
    return sims


# 第四步，将字典内容写入文档方便查阅，下次打开程序可以用另外的函数加载，不用重新
def save_doc_index(doc_dict):
    index_file = "/home/wayne/2017SMP/fenci2/index_file.txt"
    lines = ""
    for index in doc_dict:
        lines += str(index) + ' ' + doc_dict[index] + '\n'
    f = open(index_file, 'w')
    f.write(lines)
    f.close()


def load_doc_index():
    doc_dict = {}
    index_file = "/home/wayne/2017SMP/fenci2/index_file.txt"
    f = open(index_file)
    lines = f.readlines()       
    # 把文件内容读出来存到lines 再关掉，不占内存
    f.close()
    for line in lines:
        line = line.strip()
        tokens = line.split(" ")
        doc_dict[int(tokens[0])] = tokens[1]
    return doc_dict


if __name__ == '__main__':              
# if __name__ == '__main__' 函数只有直接当作脚本执行时才有效，Import到其他模块时无效
    x_train, doc_dict = get_trainset() # 获取预处理的语料
    save_doc_index(doc_dict) # 保存index_file
    doc_dict = load_doc_index()# 加载index_filex
    model_dm = train(x_train)  # 训练模型，若已经训练过可以省略这步
    sims = test()
    for index, sim in sims:
        print (doc_dict[index])
        print (sim)
        doc = x_train[int(index)]
        doc = doc[0] # doc包括词袋和编号,这里只要词袋
        for word in doc:
            print (word,)

