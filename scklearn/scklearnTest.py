from sklearn.datasets import load_iris,fetch_20newsgroups,load_boston,load_diabetes
from sklearn.model_selection import train_test_split

def iris():
    # 加载数据
    l=load_iris()

    # print("获取特征值")
    #
    # print(l.data)
    #
    # print("获取目标值")
    #
    # print(l.target)
    #
    # print("获取描述")
    #
    # print(l.DESCR)
    #
    # print("获取特征名")
    #
    # print(l.feature_names)
    #
    # print("获取标签名")
    #
    # print(l.target_names)

    # print(l.data.shape)

    # print(l.target.shape)

    # 分割训练集和测试集，可以查看源码
    X_train, X_test, y_train, y_test=train_test_split(l.data,l.target,test_size=0.25,random_state=42)

    print(X_train)

    print(y_train)

    print(X_test)

    print(y_test)

def fetch_20newsgroupsTest():
    """
    scklearn分类数据
    :return:
    """
    # 加载数据
    l=fetch_20newsgroups(subset="all")

    # 获取特征值
    # print(l.data)

    # 获取标签
    print(l.target)

def boston():
    """
    回归数据
    :return:
    """
    # 加载数据
    l=load_boston()

    print(l.data)

    print(l.target)


if __name__=="__main__":
    iris()
    # boston()