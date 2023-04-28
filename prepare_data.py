# 以下代码是没有意义的测试
# 可以删掉



# 导入需要打标的数据及评论
import re
import pickle
import random
import pandas as pd
import numpy as np
import jieba

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

from sklearn.svm import SVC
from sklearn import preprocessing, decomposition, model_selection, metrics, pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import TfidfVectorizer as TFIV
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix

# 数据审核及矫正
def DataOverview(data):
    print('Data Overview:')
    print(data.head(4))
    print('-' * 30)
    print('Data Information')
    print(data.info())
    print('-' * 40)
    print('Data DESC:')
    print(data.describe())
    print('-' * 60)


# 缺失值审核
def MissingView(data):
    na_cols = data.isnull().any(axis=0)  # 查看每一列是否具有缺失值
    print('NA Cols:')
    print(na_cols)  # 查看具有缺失值的列
    print('-' * 30)
    na_lines = data.isnull().any(axis=1)  # 查看每一行是否具有缺失值
    print('NA Recors:')
    print('Total number of NA lines is: {0}'.format(na_lines.sum()))  # 查看具有缺失值的行总记录数
    print(data[na_lines])  # 只查看具有缺失值的行信息
    print('-' * 60)


def SetLabel(score):
    # 构建情感标签， 京东评分为1 - 5分，
    # 对于我们做的情感分析作用不大，可以重新划分标签，作为训练模型的语料。
    # 即划分方式为： 划分为4 - 5分好评，1 - 3分差评。
    if score >= 4:
        return 1
    else:
        return 0

def sample_balabce(X, y):

    model_smote = SMOTE()
    x_smote_resamples, y_smote_resamples = model_smote.fit_resample(X, y)
    return x_smote_resamples, y_smote_resamples



def main():
    with open('./data/京东评论数据.csv', 'r', encoding='utf-8') as f:
        data = pd.read_csv(f)

    # DataOverview(data)

    MissingView(data)

    # 计算数据集中’score’列中每个值的出现次数
    data['score'].value_counts()
    # 然后用这些计数绘制一个条形图
    sns.countplot(data=data, x='score')

    # 数据转化
    data['creation_time'] = pd.to_datetime(data['creation_time'])
    data['reference_time'] = pd.to_datetime(data['reference_time'])

    data['year'] = data.creation_time.dt.year
    data['month'] = data.creation_time.dt.month
    data['weekday'] = data.creation_time.dt.weekday
    data['hour'] = data.creation_time.dt.hour
    plt.show()
    # 观测每周评论数数据变化情况
    fig1, ax1 = plt.subplots(figsize=(14, 4))
    df = data.groupby(['hour', 'weekday']).count()['nickname'].unstack()
    df.plot(ax=ax1, style='-.')
    plt.show()

    # 评论的长短可以看出评论者的认真程度
    data['content_len'] = data['content'].str.len()
    fig2, ax2 = plt.subplots()
    sns.boxplot(x='score', y='content_len', data=data, ax=ax2)
    ax2.set_ylim(0, 600)
    plt.show()

    # stopwords = stopwordslist(r'D:\分析实战\京东评论文本挖掘\data\哈工大停用词表.txt')
    # comment = getcomment(r"D:\分析实战\京东评论文本挖掘\data\京东评论数据.csv")
    #
    # print('停用词点', stopwords[:3])
    # print('语料信息：', comment[:3])

    ########################################### 文本预处理
    # 提取需处理的数据及标签
    data1 = data[['content', 'score']]
    data1.info()

    # 获取停用词
    with open('./data/哈工大停用词表.txt', 'r', encoding='gbk') as file:
        word_list = [x.strip() for x in file.readlines()]

    data1['score'] = data1['score'].map(lambda x: SetLabel(x))
    # 分词函数 把文本通过空格形式分词
    data1['seg_words'] = data1['content'].apply(lambda x: ' '.join(jieba.cut(x)))


    # 特征选取
    # 数据集拆分为语料、标签
    terms = data1['seg_words'].tolist()
    y = data1['score'].tolist()


    # 初始化TFIV对象，去停用词，加2元语言模型
    tfv = TFIV(min_df=3, max_features=None, strip_accents='unicode', analyzer='word', token_pattern=r'\w{1,}',
               ngram_range=(1, 2), use_idf=1, smooth_idf=1, sublinear_tf=1, stop_words=word_list)

    tfv.fit(terms)
    X_all = tfv.transform(terms)

    # 分类模型前的特征选择：将文本进行特征表示后，还进行特征选择，选出较优的特征。这一步操作可以有效特省模型性能，改善模型。本次模型选用卡方检验选取100个特征
    # 特征选择

    select_feature_model = SelectKBest(chi2, k=100)  ##卡方检验来选择100个最佳特征
    X_all = select_feature_model.fit_transform(X_all, y)  # 减少特征的数量，达到降维的效果，从而使模型的方法能力更强，降低过拟合的风险

    ###################################  模型建立与选择
    # 使用机器学习去做情感分析。特征值是评论文本经过TF-IDF处理的向量，标签值评论分类为1（好评）、0（差评）。主要选取模型有：朴素贝叶斯、逻辑回归、SVM。对比下模型拟合效果
    # 切分测试集、训练集

    x_train, x_test, y_train, y_test = train_test_split(X_all, y, random_state=0, test_size=0.25)

    # 朴素贝叶斯
    model_NB = MNB()
    model_NB.fit(x_train, y_train)  # 特征数据直接灌进来
    MNB(alpha=1.0, class_prior=None, fit_prior=True)  # ”alpha“是平滑参数，不需要掌握哈。


    # 评估预测性能，减少过拟合
    print("贝叶斯分类器20折交叉验证得分: ",
          np.mean(cross_val_score(model_NB, x_train, y_train, cv=20, scoring='roc_auc')))

    model_LR = LogisticRegression(C=.01)  # C是正则化系数。
    model_LR.fit(x_train, y_train)
    print("20折交叉验证得分: ", np.mean(cross_val_score(model_LR, x_train, y_train, cv=20, scoring='roc_auc')))


    model_SVM = LinearSVC(C=.01)  # C是正则化系数。
    model_SVM.fit(x_train, y_train)
    print("20折交叉验证得分: ", np.mean(cross_val_score(model_SVM, x_train, y_train, cv=20, scoring='roc_auc')))

    model_LR = LogisticRegression(C=.01)  # C是正则化系数。
    model_LR.fit(x_train, y_train)
    print("20折交叉验证得分: ", np.mean(cross_val_score(model_LR, x_train, y_train, cv=20)))

    # 查看此时的混淆矩阵
    y_predict = model_SVM.predict(x_test)
    cm = confusion_matrix(y_test, y_predict)
    print(cm)

    rex, rey = sample_balabce(X_all, y)
    rex_train, rex_test, rey_train, rey_test = train_test_split(rex, rey,
                                                                random_state=0, test_size=0.25)

    # 使用过采样样本(简单复制)进行模型训练，并查看准确率
    model_SVM = LinearSVC(C=.01)  # C是正则化系数。
    model_SVM.fit(rex_train, rey_train)
    print("20折交叉验证得分: ", np.mean(cross_val_score(model_SVM, rex_train, rey_train, cv=20, scoring='roc_auc')))

    # 查看此时的混淆矩阵
    rey_predict = model_SVM.predict(rex_test)
    cm = confusion_matrix(rey_test, rey_predict)
    print(cm)


if __name__ == "__main__":
    main()
