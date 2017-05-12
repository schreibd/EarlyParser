'''
Created on 11.05.2017

@author: Daniel
'''

class Itemset():



    def __init__(self):
        self.itemSet = []
        
    def addItem(self, item):
        self.itemSet.append(item)
        
    def __repr__(self):
        for item in self.itemSet:
            print(item.__repr__())
        
        