#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

class Recommendation(object):
    def __init__(self):
        self.hash_pair = dict()
        self.hash_tuple = dict()
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

                for j in range(i+1,len(data)):
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
        count100 = 0
        f = open("f_2", 'w')
        for key in self.hash_pair:
            f.write(str(key) + " " + str(self.hash_pair[key]) + "\n")

            if self.hash_pair[key] < 100:
                continue
            else:
                count100 += 1
                self.hash_conf[key] = float(self.hash_pair[key])/float(self.hash_item[key[0]])
        f.flush()
        f.close()

        print count100
        list = sorted(self.hash_conf.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

        count = 0
        for element in list:
            if count == 10:
                break
            print element
            count += 1


    def read_tuple(self, file, ):
        f = open(file, 'r')
        count  = 0
        for line in f:
            count += 1
            data = line.rstrip().split(' ')
            data.sort()
            for i in range(0,len(data)):
                if data[i] in self.hash_item:
                    self.hash_item[data[i]] = self.hash_item[data[i]] + 1
                else:
                    self.hash_item[data[i]] = 1

                for j in range(i+1,len(data)):
                    if data[i] == data[j]:
                        continue
                    current = (data[i], data[j])
                    if current in self.hash_pair:
                        self.hash_pair[current] = self.hash_pair[current] + 1
                    else:
                        self.hash_pair[current] = 1
                    for k in range(j+1,len(data)):
                        current = (data[i], data[j], data[k])
                        if current in self.hash_tuple:
                            self.hash_tuple[current] = self.hash_tuple[current] + 1
                        else:
                            self.hash_tuple[current] = 1


        # get support at least 100

        for key in self.hash_tuple:
            if self.hash_tuple[key] < 100:
                continue
            # 12-3 13-1 23-1
            self.hash_conf[(key[0],key[1],key[2])] = float(self.hash_tuple[key]) / float(
                self.hash_pair[(key[0],key[1])])
            self.hash_conf[(key[0], key[2], key[1])] = float(self.hash_tuple[key]) / float(
                self.hash_pair[(key[0], key[2])])
            self.hash_conf[(key[1], key[2], key[0])] = float(self.hash_tuple[key]) / float(
                self.hash_pair[(key[1], key[2])])


        list = sorted(self.hash_conf.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

        count = 0
        for element in list:
            if count == 100:
                break
            print element
            count += 1

if __name__ == "__main__":

    r = Recommendation()
    r.read_pair("/Users/wenzhongli/Desktop/homework1/data/browsing.txt")
    # r.read_tuple("/Users/wenzhongli/Desktop/homework1/data/browsing.txt")