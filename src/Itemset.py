class Itemset():

    def __init__(self):
        #Liste, welche EarleyItems enthaelt
        self.itemSet = []
        
    def addItem(self, item):
        self.itemSet.append(item)
        
    def __repr__(self):
        for item in self.itemSet:
            print(item.__repr__())
    
    #Checkt ob Item bereits in Set enthalten ist
    def hasItem(self, other):
        for item in self.itemSet:
            if(item.regel == other.regel):
                return True
        return False
            