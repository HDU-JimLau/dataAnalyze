from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import jieba
import numpy as np

def DictTest():
    """
    字典数据抽取
    :return:
    """
    # 实例化
    # 注意sparse参数，默认为true
    dict = DictVectorizer(sparse=False)
    # 调用fit_transform
    data = dict.fit_transform(
        [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 80}, {'city': '深圳', 'temperature': 90},
         {'city': '杭州', 'temperature': 40}])

    print(dict.get_feature_names())
    print(data)

    return None;


def CountTest():
    """
    对文本进行特征值化
    :return:
    """
    # 实例化
    cv = CountVectorizer()
    data = cv.fit_transform(["life life  is short ,i like python", 'life is long, i like java'])

    print(cv.get_feature_names())
    print(data.toarray())

    return None


def jiebaCut():
    """
    对文章分词，返回分词后的字符串
    :return:
    """

    s1 = "参演电视剧《与青春有关的日子》，参演开始在影视圈崭露头角 [1]  "
    s2 = "在电影《海洋天堂》中扮演自闭症患者王大福；同年参演抗战题材的电视剧《雪豹》"

    s1, s2 = jieba.cut(s1), jieba.cut(s2)
    return " ".join(s1), " ".join(s2)


def Chinese():
    """
    对中文进行特征提取
    :return:
    """
    # 实例化
    s1, s2 = jiebaCut()
    cv = CountVectorizer()
    data = cv.fit_transform([s1, s2])

    print(cv.get_feature_names())
    print(data.toarray())


def TfidfTest():
    """
    中文特征化提取
    :return:
    """

    s1, s2 = jiebaCut()

    print(s1, s2)
    # 实例化
    tf = TfidfVectorizer()

    data = tf.fit_transform([s1, s2])

    print(tf.get_feature_names())

    print(data)

    return None


def mm():
    """
    归一化处理
    :return:
    """
    mm = MinMaxScaler(feature_range=(10,20))

    data = mm.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])

    print(data)
    return None

def stand():
    """
    标准化缩放
    :return:
    """
    std=StandardScaler()

    data=std.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])

    print(data)
    return None

def im():
    """
    缺失值填充
    :return:
    """
    # Nan nan
    # im=Imputer(missing_values='NaN',strategy='mean',axis=0)
    #
    # data = im.fit_transform([[1,2], [np.nan,3], [7,6]])
    #
    # print(data)
    # return None

def var():
    """
    特征过滤，删除低方差的特征
    :return:
    """
    vari=VarianceThreshold(threshold=0.0)

    data=vari.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]])

    print(data)
    return None

def pcatest():
    """
    主要成分分析进行特征降维
    :return:
    """
    pca=PCA(n_components=0.9)

    data=pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])

    print(data)



    return None


if __name__ == "__main__":
    pcatest()
