# 导入numpy工具包。
import numpy as np
# 初始化一个2*2的线性相关矩阵。
M = np.array([[1, 2], [2, 4]])
# 计算2*2线性相关矩阵的秩。
np.linalg.matrix_rank(M, tol=None)



# 导入pandas用于数据读取和处理。
import pandas as pd

# 从互联网读入手写体图片识别任务的训练数据，存储在变量digits_train中。
#digits_train = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra', header=None)
digits_train = pd.read_csv('./optdigits.tra', header=None)

# 从互联网读入手写体图片识别任务的测试数据，存储在变量digits_test中。
digits_test = pd.read_csv('./optdigits.tes', header=None)
#digits_test = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes', header=None)
#####xiaojie#####
#read_csv返回的是DataFrame对象,具体可以搜索一些关于DataFrame的操作方法
#####xiaojie#####
print digits_train.iloc[0] #输出第0行数据
# 分割训练数据的特征向量和标记。
X_digits = digits_train[np.arange(64)] ###其实可以直接用digits_train[[0,1]]即直接用列表，来抽取指定列的数据。
y_digits = digits_train[64]

# 从sklearn.decomposition导入PCA。 
from sklearn.decomposition import PCA

# 初始化一个可以将高维度特征向量（64维）压缩至2个维度的PCA。 
estimator = PCA(n_components=2)
X_pca = estimator.fit_transform(X_digits) ###这里的X_pca不再是DataFrame对象，而是Array矩阵对象。

# 显示10类手写体数字图片经PCA压缩后的2维空间分布。 
from matplotlib import pyplot as plt

def plot_pca_scatter():
    colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
    for i in xrange(len(colors)):
        px = X_pca[:, 0][y_digits.as_matrix() == i] # y_digits.as_matrix() == i返回的是一个同等长度的数组。并且==i位置处的值为true，反之为false，仍然可以作为索引
        py = X_pca[:, 1][y_digits.as_matrix()== i]
        plt.scatter(px, py, c=colors[i]) #t通过颜色的分析，对应手写数字的九个数字。
    
    plt.legend(np.arange(0,10).astype(str))
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.show()
    
plot_pca_scatter()



# 对训练数据、测试数据进行特征向量（图片像素）与分类目标的分隔。
X_train = digits_train[np.arange(64)]
y_train = digits_train[64]
X_test = digits_test[np.arange(64)]
y_test = digits_test[64]

# 导入基于线性核的支持向量机分类器。
from sklearn.svm import LinearSVC

# 使用默认配置初始化LinearSVC，对原始64维像素特征的训练数据进行建模，并在测试数据上做出预测，存储在y_predict中。
svc = LinearSVC()
svc.fit(X_train, y_train)
y_predict = svc.predict(X_test)

# 使用PCA将原64维的图像数据压缩到20个维度。
estimator = PCA(n_components=20)

# 利用训练特征决定（fit）20个正交维度的方向，并转化（transform）原训练特征。
pca_X_train = estimator.fit_transform(X_train)
# 测试特征也按照上述的20个正交维度方向进行转化（transform）。
pca_X_test = estimator.transform(X_test)   ###注意：这里也要用上面fit_transform的方差还有期望等等。而不能单独再用fit_transform.

# 使用默认配置初始化LinearSVC，对压缩过后的20维特征的训练数据进行建模，并在测试数据上做出预测，存储在pca_y_predict中。
pca_svc = LinearSVC()
pca_svc.fit(pca_X_train, y_train)
pca_y_predict = pca_svc.predict(pca_X_test)



# 从sklearn.metrics导入classification_report用于更加细致的分类性能分析。
from sklearn.metrics import classification_report

# 对使用原始图像高维像素特征训练的支持向量机分类器的性能作出评估。
print svc.score(X_test, y_test)
print classification_report(y_test, y_predict, target_names=np.arange(10).astype(str))

# 对使用PCA压缩重建的低维图像特征训练的支持向量机分类器的性能作出评估。
print pca_svc.score(pca_X_test, y_test)
print classification_report(y_test, pca_y_predict, target_names=np.arange(10).astype(str))

###很明显，用了主成分分析以后，降低了分析的精确度。
###由于有多个类别，可以参见原书中的解释。
