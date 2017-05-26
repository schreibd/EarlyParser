class Itemset():


    def __init__(self):
        #Liste, welche EarleyItems enthaelt
        self.itemList = []
        
    def addItem(self, item):
        self.itemList.append(item)
        
    def __repr__(self):
        for item in self.itemList:
            print(item.__repr__())
    
    #Checkt ob Item bereits in Set enthalten ist
    def hasItem(self, other):
        for item in self.itemList:
            if item.regel == other.regel:
                return True
        return False
            