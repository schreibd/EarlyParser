

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
        #Liste der Itemsets (active und prediction zusammengefasst)
        self.itemSetLists = []
        #Liste der Itemsets (completed)
        self.completedSetLists = []     
    def __repr__(self):
        for itemSet in self.itemSetLists:
            itemSet.__repr__()
        for itemSet in self.completedSetLists:
            itemSet.__repr__()   
    
    #Erstelle Startregel und füge sie dem ersten Itemset hinzu
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
                #print("Old length: " + str(oldLength) + " Length: " + str(length))
                oldLength = length
                length = len(currentItemSet.itemSet)
            #print("Old length: " + str(oldLength) + " Length: " + str(length))
            self.scan(currentItemSet, counter)
            completedLength = len(self.completedSetLists[counter].itemSet)
            #print(str(completedLength))
            
            oCompletedLength = 0
            while oCompletedLength < int(completedLength):
                self.complete(currentItemSet, counter)
                print("Old length: " + str(oCompletedLength) + " Length: " + str(completedLength))
                oCompletedLength = completedLength
                completedLength = len(self.completedSetLists[counter].itemSet)
            counter += 1    
    
    def predict(self, currentItemSet, position):
        for group in self.grammar.regeln.values():  
            for rule in group:
                tempItem = None
                for item in currentItemSet.itemSet:
                    if rule == item.regel:
                    #if item.regel.rightSide == rule.rightSide and item.regel.leftSide == rule.leftSide:
                        tempItem = None
                        break
                    if rule.leftSide == item.regel.rightSide:
                        tempItem = Item(rule, 0, position)
                if tempItem != None and self.itemSetLists[position] != None:
                    
                    self.itemSetLists[position].addItem(tempItem)   
                elif tempItem != None:
                    tempSet = Itemset().addItem(tempItem)
                    self.itemSetLists.append(tempSet)
                    
    
    def scan(self, currentItemSet, position):
        symbol = self.sentence[position+1]
        for item in self.itemSetLists[position].itemSet:
            if item.regel.rightSide == symbol:
                tempItem = Item(item.regel, item.dot + 1, position)
                if self.completedSetLists  and self.completedSetLists[position] != None: 
                    self.completedSetLists[position].addItem(tempItem)
                else:
                    tempSet = Itemset()
                    tempSet.addItem(tempItem)
                    self.completedSetLists.append(tempSet)
    
    
    
    def complete(self, currentItemSet, position):
        for item in self.completedSetLists[position].itemSet:
            tempItem = None
            for item2 in currentItemSet.itemSet: 
                print(item2.dot+1 < len(item2.regel.rightSide))
                if item.regel.leftSide == item2.regel.rightSide and item2.dot+1 == len(item2.regel.rightSide):
                    tempItem = Item(item2.regel, item2.dot + 1, position)
                    if self.completedSetLists[position].hasItem(tempItem) == False:
                        self.completedSetLists[position].addItem(tempItem)
                elif item2.dot+1 < len(item2.regel.rightSide) and item.regel.leftSide == item2.regel.rightSide[item2.dot + 1]:
                    tempItem = Item(item2.regel, item.dot + 1, position)
                    tempSet = Itemset()
                    tempSet.addItem(tempItem)
                    self.itemSetLists.append(tempSet)
                
        
        #for item in self.completedSetLists[position].itemSet:
            #tempItem = None
            #for item2 in currentItemSet.itemSet: 
                #if item.regel.leftSide == item2.regel.rightSide and item2.dot+1 == len(item2.regel.rightSide):
                    #print("Hallo")
                    #tempItem = Item(item2.regel, item.dot + 1, position)
                #if tempItem and item.regel == tempItem.regel:
                    #tempItem = None
                    #break
                #if tempItem != None:
                    #self.completedSetLists[position].addItem(tempItem)
                    
    #def complete(self, currentItemSet, position):
        #for item in self.completedSetLists[position].itemSet:
            #for item2 in currentItemSet.itemSet:                
                #if item.regel.leftSide == item2.regel.rightSide and item2.dot+1 == len(item2.regel.rightSide):
                    #self.completedSetLists[position].itemSet.append(Item(item2.regel, item.dot + 1, position))
    
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