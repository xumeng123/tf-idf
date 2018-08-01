#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import math
import sys
import jieba
import re
#文本解析预处理
# 分词以后，去掉字母，数字，标点符号以及括号，返回一个词集合[word1,word2,....]
def segment(sentence, cut_all=False):
    sentence = sentence.replace('\n', '').replace('\u3000', '').replace('\u00A0', '')
    sentence = ' '.join(jieba.cut(sentence, cut_all=cut_all))
    return re.sub('[a-zA-Z0-9.。:：,，)）(（！!??”“\"]', '', sentence).split()

class MyDocuments(object):
    def __init__(self, dirname):
        self.dirname = dirname
        if not os.path.isdir(dirname):
            print(dirname, ' not exists, system exit!')
            sys.exit()

    def __iter__(self):
        for dirfile in os.walk(self.dirname):  #dirfile: [dirpath, dirnames, filenames]
            for fname in dirfile[2]:
                text = open(os.path.join(dirfile[0], fname),
                            'r', encoding='utf-8', errors='ignore').read()
                yield segment(text)   #文本解析


def main():
    inputdir = ''   #训练文档的位置
    outputfile = '' #输出的IDF文件
    documents = MyDocuments(inputdir) #返回的是被分词后的文档的集合

    ignored = {'', ' ', '', '。', '：', '，', '）', '（', '！', '?', '”', '“'}
    id_freq = {}
    i = 0
    #统计不同的单词在不同文档中出现的次数 idf=N/Nw 文档总数除以存在某个单词的文档的数目
    for doc in documents:
        doc = set(x for x in doc if x not in ignored) #set集合保证每个文档中的单词在计数时只被记录一次
        for x in doc:
            id_freq[x] = id_freq.get(x, 0) + 1
        if i % 1000 == 0:
            print('Documents processed: ', i)
        i += 1
    #将产生的idf文件存储起来
    with open(outputfile, 'w', encoding='utf-8') as f:
        for key, value in id_freq.items():
            f.write(key + ' ' + str(math.log(i / value, 2)) + '\n')


if __name__ == "__main__":
   main()
