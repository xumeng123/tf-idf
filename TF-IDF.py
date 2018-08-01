#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys, getopt
import jieba
import re
#文本解析预处理
# 分词以后，去掉字母，数字，标点符号以及括号，返回一个词集合[word1,word2,....]
def segment(sentence, cut_all=False):
    sentence = sentence.replace('\n', '').replace('\u3000', '').replace('\u00A0', '')
    sentence = ' '.join(jieba.cut(sentence, cut_all=cut_all))
    return re.sub('[a-zA-Z0-9.。:：,，)）(（！!??”“\"]', '', sentence).split()


class IDFLoader(object):
    def __init__(self, idf_path):
        self.idf_path = idf_path
        self.idf_freq = {}     # idf
        self.mean_idf = 0.0    # 均值idf,采用均值的目的是以防输入句子中出现IDF中没有的单词，此时使用均值IDF代替
        self.load_idf()

    def load_idf(self):       # 加载idf数据
        cnt = 0
        with open(self.idf_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    word, freq = line.strip().split(' ')
                    cnt += 1
                except Exception as e:
                    pass
                self.idf_freq[word] = float(freq)

        print('词汇总数: ',cnt)
        self.mean_idf = sum(self.idf_freq.values()) / cnt


class TFIDF(object):
    def __init__(self, idf_path):
        self.idf_loader = IDFLoader(idf_path)
        self.idf_freq = self.idf_loader.idf_freq
        self.mean_idf = self.idf_loader.mean_idf

    def Extract_KWords(self, sentence, topK=20):    # 提取关键词
        # 过滤
        seg_list = segment(sentence)

        freq = {}
        for w in seg_list:
            freq[w] = freq.get(w, 0.0) + 1.0
        total = sum(freq.values())

        for k in freq:   # 计算 TF-IDF
            freq[k] *= self.idf_freq.get(k, self.mean_idf) / total

        tags = sorted(freq, key=freq.__getitem__, reverse=True)  # 排序

        if topK:
            return tags[:topK]
        else:
            return tags

def main():
    #idf文件路径
    IDF_File = 'idf.txt'
    #文档路径
    docPath = 'test2.txt'
    #提取关键字的个数
    topK = 20
    tf_idf = TFIDF(IDF_File)
    sentence = open(docPath, 'r', encoding='utf-8', errors='ignore').read()
    key_words = tf_idf.Extract_KWords(sentence, topK)

    for k_w in key_words:
        print(k_w)

if __name__ == "__main__":
    main()
