

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
        self.itemSetList = []
        
        self.completedSetList = []
        
    def __repr__(self):
        for item in self.itemSetList:
            item.__repr__()
    
    def initializeParser(self):
        tempSet = Itemset()
        for group in self.grammar.regeln.values():
            for rule in group:
                if rule.leftSide == "S":
                    tempItem = Item(rule, 0, 0)
                    tempSet.addItem(tempItem)
                    self.itemSetList.append(tempSet)
    def parseLoop(self):
        counter = 0
        while counter < self.letterCount:
            currentItemSet = self.itemSetList[counter]
            length = len(currentItemSet.itemSet)
            oldLength = 0
            while oldLength < int(length):  
                self.predict(currentItemSet, counter)
                ##print("Old length: " + str(oldLength) + " Length: " + str(length))
                self.__repr__()
                oldLength = length
                length = len(currentItemSet.itemSet)
            #self.scan(currentItemSet, counter)
            counter += 1 
    
    def predict(self, currentItemSet, position):
        counter = 0
        while counter < len(currentItemSet.itemSet):
            for group in self.grammar.regeln.values():
                for rule in group:
                    if rule.leftSide == currentItemSet.itemSet[counter].regel.rightSide:
                        if rule.leftSide != currentItemSet.itemSet[counter].regel.
                        tempItem = Item(rule, 0, position)
                        self.itemSetList[position].addItem(tempItem)
            counter += 1
    #def scan(self, currentItemSet, position):    
        #for group in self.grammar.regeln.values():
            #for rule in group:
                #if str(self.itemSetList[position].itemSet[0].regel.rightSide) == rule.leftSide:                   
                    #newItem = Item(rule, 0, position)
                    #self.itemSetList[position+1].addItem(newItem)

    #def complete(self):