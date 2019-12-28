#python example to infer document vectors from trained doc2vec model
import gensim.models as gm
import codecs
import numpy as np
def simlarityCalu(vector1, vector2):
    vector1Mod = np.sqrt(vector1.dot(vector1))
    vector2Mod = np.sqrt(vector2.dot(vector2))
    if vector2Mod != 0 and vector1Mod != 0:
        simlarity = (vector1.dot(vector2)) / (vector1Mod * vector2Mod)
    else:
        simlarity = 0
    return simlarity
#parameters
model = "./processedData_2014MSR_xiaojie/doc2vec_model/doc2vec_test.model.bin"
test_docs = "./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/test.txt" # test.txt为需要向量化的文本
output_file = "./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/test_vector.txt" #得到测试文本的每一行的向量表示

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

test_vector = np.loadtxt("./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/test_vector.txt")
print(m.docvecs.most_similar([test_vector], topn=5)) # 
test_vector_2 = np.save('./processedData_2014MSR_xiaojie/text_for_trainingDoc2Vec/test_vector', test_vector)
vector1=m.docvecs[0] #根据行号取出向量。
print (simlarityCalu(vector1,test_vector))
vector2=m.docvecs[9]
print (simlarityCalu(vector2,test_vector))