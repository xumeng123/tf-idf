##基于TD-IDF算法的关键词提取
运行环境：
python3.5(python2也可以，基本没啥改动)
结巴分词工具
pip3 install jieba

## TF-IDF关键词提取

用法：
1.先运行GetIDF.py得到IDF(逆文档频率)（已训练好），无需再运行
2.输入参数，直接运行TF-IDF.py即可

> 注：该repo中提供的idf.txt由清华NLP组的新闻数据集训练获得。
