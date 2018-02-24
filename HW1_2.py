#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

class Recommendation(object):
    def __init__(self):
        self.hash_pair = dict()
        self.hash_item = dict()
        self.hash_conf = dict()

    def read_pair(self, file, ):
        f = open(file, 'r')
        count  = 0
        for line in f:
            count += 1
            data = line.rstrip().split(' ')
            for i in range(0,len(data)):
                if data[i] in self.hash_item:
                    self.hash_item[data[i]] = self.hash_item[data[i]] + 1
                else:
                    self.hash_item[data[i]] = 1

                for j in range(i,len(data)):
                    if data[i] == data[j]:
                        continue
                    current1 = (data[i], data[j])
                    current2 = (data[j], data[i])
                    if current1 in self.hash_pair:
                        self.hash_pair[current1] = self.hash_pair[current1] + 1
                    else:
                        self.hash_pair[current1] = 1
                    if current2 in self.hash_pair:
                        self.hash_pair[current2] = self.hash_pair[current2] + 1
                    else:
                        self.hash_pair[current2] = 1

        # get support at least 100

        for key in self.hash_pair:
            if self.hash_pair[key] < 100:
                continue
            else:
                self.hash_conf[key] = float(self.hash_pair[key])/float(self.hash_item[key[0]])

        list = sorted(self.hash_conf.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

        count = 0
        for element in list:
            if count == 10:
                break
            print element
            count += 1



if __name__ == "__main__":
    a = "abc"
    b = "abb4"
    print a < b
    r = Recommendation()
    r.read_pair("/Users/wenzhongli/Desktop/homework1/data/browsing.txt")