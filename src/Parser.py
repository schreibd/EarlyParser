import re
from Itemset import*
from EarleyItem import*
from Regel import*

class Parser:
    
    START_SYMBOL = "StartStart"
    def __init__(self, grammar, sentence):
        self.grammar = grammar
        self.sentence = sentence
        
        self.wordCount = len(re.findall(r'\w', self.sentence))
        self.letterCount = len(self.sentence) - self.sentence.count(' ')
        self.itemSetList = [self.letterCount+1]
        #self.completedSetList = []
        
    def __repr__(self):
        for item in self.itemSetList:
            print(item.__repr__())
    
    def initializeParser(self):
        currentItemset = Itemset()
        print("OLLLA" + str(currentItemset.__repr__()))
        currentItem = EarleyItem(Regel(Parser.START_SYMBOL, "S"), 0, 0)
        
        currentItemset.addItem(currentItem)
        self.itemSetList[0] = currentItemset
        

        
    def parseLoop(self):
        counter = 0
        while counter < self.letterCount:
            currentItemSet = self.itemSetList[counter]
            #self.scan(currentItemSet, counter)
            #print(currentItemSet.__repr__())
            counter += 1
    
    #def scan(self, currentItemSet, position):
        
        #for group in self.grammar.regeln.values():
            #for rule in group:
                #print("In Scanner: " + self.itemSetList[position][0].__repr__())
                #print("Hallo")
                ##if str(self.itemSetList[position][0].regel.leftSide) == rule.leftSide:
                    #print("Hallo2")
                    #newItem = EarleyItem(rule, 0, position)
                    #self.itemSetList[position].addItem(newItem)
        
        
    #def predict(self):
        
    #def complete(self):