# tf-idf
使用TF-IDF算法提取关键词[Extracting the key words with TF-IDF algorithm]
基于TD-IDF算法的关键词提取
运行环境：
python3.5(python2也可以，基本没啥改动)
结巴分词工具
pip3 install jieba


## IDF(逆文档频率)生成

用法：

```bash
$ python gen_idf.py -i <inputdir> -o <outputfile>
```

- `-i <inputdir>`   ： 语料库目录，程序会扫描目录下的所有文件
- `-o <outputfile>` ： 保存idf到指定文件

## TF-IDF关键词提取

用法：
1.先运行GetIDF.py得到IDF（已训练好），无需再运行
2.输入参数，直接运行TF-IDF.py即可

> 注：该repo中提供的idf.txt由清华NLP组的新闻数据集训练获得。
