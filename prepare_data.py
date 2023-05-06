# 导入需要打标的数据及评论

import pandas as pd
import re
import jieba.posseg as psg
import numpy as np
import jieba
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB as MNB
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import TfidfVectorizer as TFIV
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix


# 正则表达式导入
def makePattern():
    with open('./prepareFile/pattern.txt', 'r') as f:
        # 读取一行，同时把回车符合换成'|'
        pattern_string = f.read().replace('\n', '|')
        pattern = re.compile(pattern_string)
    return pattern


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
    with open('./data/JD/iphone13/1.csv', 'r', encoding='gbk') as f:
        data = pd.read_csv(f)

    # 评论去重
    print("数据的规模(行, 列):", data.shape)  #
    dataf = data
    # 删除数据记录中所有列值相同的记录
    print("重复的行数:", data[['content']].duplicated().sum())
    data = data[['content']].drop_duplicates()  # (n, 1)

    content = data['content']  # (n,)

    # 编译匹配模式
    pattern = makePattern()
    # re.sub用于替换字符串中的匹配项
    content = content.apply(lambda x: pattern.sub('', x))

    # 自定义简单的分词函数
    worker = lambda s: [[x.word, x.flag] for x in psg.cut(s)]  # 单词与词性
    seg_word = content.apply(worker)

    # 将词语转化为数据框形式，一列是词，一列是词语所在的句子id，最后一列是词语在该句子中的位置
    # 每一评论中词的个数
    n_word = seg_word.apply(lambda x: len(x))
    # 构造词语所在的句子id
    n_content = [[x + 1] * y for x, y in zip(list(seg_word.index), list(n_word))]
    # 将嵌套的列表展开，作为词所在评论的id
    index_content = sum(n_content, [])

    seg_word = sum(seg_word, [])
    # 词
    word = [x[0] for x in seg_word]
    # 词性
    nature = [x[1] for x in seg_word]
    # content_type评论类型
    score = [[x] * y for x, y in zip(list(dataf['score']), list(n_word))]
    score = sum(score, [])

    # 构造数据框
    result = pd.DataFrame({'index_content': index_content,
                           'word': word,
                           'nature': nature,
                           'score': score})

    print(result)

    # 删除标点符号
    result = result[result['nature'] != 'x']

    print(result)

    # 删除停用词
    # 加载停用词
    stop_path = open('./data/哈工大停用词表.txt', 'r', encoding='gbk')
    stop = [x.replace('\n', '') for x in stop_path.readlines()]
    # 得到非停用词序列
    word = list(set(word) - set(stop))
    # 判断表格中的单词列是否在非停用词列中
    result = result[result['word'].isin(word)]
    print(result)

    # 构造各词在评论中的位置列
    n_word = list(result.groupby(by=['index_content'])['index_content'].count())
    index_word = [list(np.arange(0, x)) for x in n_word]
    index_word = sum(index_word, [])
    result['index_word'] = index_word
    result.reset_index(drop=True, inplace=True)
    print(result)

    # 提取含名词的评论的句子id
    ind = result[[x == 'n' for x in result['nature']]]['index_content'].unique()
    # 提取评论
    result = result[result['index_content'].isin(ind)]
    # 重置索引
    result.reset_index(drop=True, inplace=True)
    print(result)

    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    # 按word分组统计数目
    frequencies = result.groupby(by=['word'])['word'].count()
    # 按数目降序排序
    frequencies = frequencies.sort_values(ascending=False)
    # 从文件中将图像读取为数组
    backgroud_Image = plt.imread('./data/cloud.png')
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",  # 这里的字体要与自己电脑中的对应
                          max_words=100,  # 选择前100词
                          background_color='white',  # 背景颜色为白色
                          mask=backgroud_Image).fit_words(frequencies)
    # 将数据展示到二维图像上
    plt.imshow(wordcloud)
    # 关掉x,y轴
    plt.axis('off')
    plt.show()

    # 将结果写出
    result.to_csv("./outputFile/word.csv", index=False, encoding='gbk')


if __name__ == "__main__":
    main()
