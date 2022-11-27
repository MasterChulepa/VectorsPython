import numpy as np
from itertools import groupby

import DataReader


def splitToVectors(lst, n):
    for i in range(0, len(lst)):
        yield lst[i:i + n]


class VectorBuilder:
    def __init__(self):
        self.fileName = '../resources/4470-AK.txt'
        self.data = DataReader.DataReader().readFile(self.fileName)

    def findBP(self):
        n = 1
        flag = True
        while flag:
            n += 1
            dataArray = np.array(self.data)
            arrays = list(splitToVectors(dataArray, n))
            vectors = self.buildVectors(n, arrays, dataArray)
            flag = self.groupVectros(vectors)
        return n

    def buildVectors(self, n, arrays, dataArray):
        vectors = []
        for i in range(0, len(arrays) - n):
            vectors.append(({'coords': ' '.join(arrays[i]), 'pointTo': dataArray[n + i]}))
        return vectors

    def groupVectros(self, vectors):
        for key, group_items in groupby(vectors, lambda vector: vector['coords']):
            numberOfItems = 0
            for item in group_items:
                numberOfItems += 1
            if numberOfItems > 1:
                print('Key: %s' % key)
                print("№ of Items: ", numberOfItems)
                print("Oops!")
                return True
        return False
