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
    
    def hasItem(self, other):
        for item in self.itemSet:
            if(item.regel == other.regel):
                return True
            else:
                return False
            