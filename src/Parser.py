

from Item import*
from Regel import*
from Itemset import*

class Parser():
    
    START_SYMBOL = "StartStart"
    
    def __init__(self, grammar, sentence):
        self.grammar = grammar
        self.sentence = sentence[:0] + " " + sentence[0:]
        
        #self.wordCount = len(re.findall(r'\w', self.sentence))
        self.letterCount = len(self.sentence) - self.sentence.count(' ')
        self.itemSetLists = []
        
        self.completedSetLists = []     
    def __repr__(self):
        for item in self.itemSetLists:
            item.__repr__()
        for item in self.completedSetLists:
            item.__repr__()   
    
    def initializeParser(self):
        tempSet = Itemset()
        for group in self.grammar.regeln.values():
            for rule in group:
                if rule.leftSide == "S":
                    tempItem = Item(rule, 0, 0)
                    tempSet.addItem(tempItem)
                    self.itemSetLists.append(tempSet)   
    
    def parseLoop(self):
        counter = 0
        while counter < self.letterCount:
            currentItemSet = self.itemSetLists[counter]
            length = len(currentItemSet.itemSet)
            oldLength = 0
            while oldLength < int(length):  
                self.predict(currentItemSet, counter)
                ##print("Old length: " + str(oldLength) + " Length: " + str(length))
                oldLength = length
                length = len(currentItemSet.itemSet)
            #self.scan(currentItemSet, counter)
            self.scan(currentItemSet, counter)
            counter += 1    
    
    def predict(self, currentItemSet, position):
        counter = 0
        for group in self.grammar.regeln.values():
            for rule in group:
                tempItem = None
                for item in currentItemSet.itemSet:
                    if item.regel.rightSide == rule.rightSide and item.regel.leftSide == rule.leftSide:
                        tempItem = None
                        break
                    if rule.leftSide == item.regel.rightSide:
                        tempItem = Item(rule, 0, position)
                if tempItem != None:
                    self.itemSetLists[position].addItem(tempItem)   
    
    def scan(self, currentItemSet, position):
        symbol = self.sentence[position+1]
        for item in self.itemSetLists[position].itemSet:
            if item.regel.rightSide == symbol:
                tempItem = Item(item.regel, item.dot + 1, position)
                if self.completedSetLists  and self.completedSetLists[position] != None:  
                    self.completedSetLists.append(tempItem)
                else:
                    tempSet = Itemset()
                    tempSet.addItem(tempItem)
                    self.completedSetLists.append(tempSet)
    
    
    
    #def scan(self, currentItemSet, position):    
        #for group in self.grammar.regeln.values():
            #for rule in group:
                #if str(self.itemSetLists[position].itemSet[0].regel.rightSide) == rule.leftSide:                   
                    #newItem = Item(rule, 0, position)
                    #self.itemSetLists[position+1].addItem(newItem)    
                    
        #while counter < len(currentItemSet.itemSet):
            #for group in self.grammar.regeln.values():
                #for rule in group:
                    #if rule.leftSide == currentItemSet.itemSet[counter].regel.rightSide:
                        #tempItem = Item(rule, 0, position)
                        #self.itemSetLists[position].addItem(tempItem)
            #counter += 1
            
            
            
    

    #def complete(self):