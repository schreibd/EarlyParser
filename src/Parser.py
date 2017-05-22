
import sys
from Item import*
from Regel import*
from Itemset import*


class Parser():
    
    #START_SYMBOL = "StartStart"
    
    def __init__(self, grammar, sentence):
        self.grammar = grammar
        self.sentence = sentence[:0] + " " + sentence[0:]
        
        self.letterCount = len(self.sentence) - self.sentence.count(' ') 
        print(str(self.letterCount))
        
        #Liste der Itemsets (active und prediction werden hier zusammengefasst (Konzept nach Fachliteratur))
        self.itemSetLists = []
        #Liste der Itemsets (completed)
        self.completedSetLists = []
        
        #Initialisiere Startregel um ParseLoop zu beginnen     
        self.initializeParser()
    
    
    def __repr__(self):
        
        cSetLists = 0
        for itemSet in self.itemSetLists:
            print("itemSet: " + str(cSetLists))
            itemSet.__repr__()
            cSetLists += 1
        
        cCompletedsetLists = 0
        for itemSet in self.completedSetLists:
            print("completedSet: " + str(cCompletedsetLists))
            itemSet.__repr__()   
            cCompletedsetLists += 1
    
    #Erstelle Startregel und f�ge sie dem ersten Itemset hinzu
    def initializeParser(self):
        tempSet = Itemset()
        for group in self.grammar.regeln.values():
            for rule in group:
                if rule.leftSide == "S":
                    tempItem = Item(rule)
                    tempSet.addItem(tempItem)
                    self.itemSetLists.append(tempSet)   
    
    #Main-Loop der durch den Eingabesatz iteriert
    def parseLoop(self):
        counter = 0
        while counter < self.letterCount:
            
            currentItemSet = self.itemSetLists[counter]
            
            length = len(currentItemSet.itemSet)
            oldLength = 0
            
            #Rufe Predictor so oft auf, bis sich Groesse des aktuell betrachteten 
            #Itemsets nicht mehr veraendert
            while oldLength < int(length):  
                self.predict(currentItemSet, counter)
                oldLength = length
                length = len(currentItemSet.itemSet)
                
            #Rufe Scanner auf 
            self.scan(counter)
            
            
            if counter < len(self.completedSetLists):
                completedLength = len(self.completedSetLists[counter].itemSet)
            else:
                completedLength = 0
        
            oCompletedLength = 0
            
            #Rufe Completor so oft auf, bis sich die Groesse des aktuell betrachteten 
            #Itemsets (completedSetLists[counter]) nicht mehr veraendert. 
            while oCompletedLength < int(completedLength):
                self.complete(currentItemSet, counter)
                oCompletedLength = completedLength
                completedLength = len(self.completedSetLists[counter].itemSet)
                
            counter += 1   
        self.validate() 
    
    #Predictor zum vorhersagen von Regeln
    def predict(self, currentItemSet, position):
        for group in self.grammar.regeln.values():  
            for rule in group:
                tempItem = None
                for item in currentItemSet.itemSet:
                    #Falls Item bereits enthalten
                    if rule == item.regel:
                        tempItem = None
                        break
                    
                    #Greife hier nicht komplette Regel auf rechter Seite ab sondern nur das Zeichen nach dem Punkt
                    if rule.leftSide == item.regel.rightSide[item.dot]:
                        tempItem = Item(rule, 0, position)
                        
                if tempItem != None and self.itemSetLists[position] != None:
                    self.itemSetLists[position].addItem(tempItem)   
                    
                elif tempItem != None:
                    tempSet = Itemset().addItem(tempItem)
                    self.itemSetLists.append(tempSet)
                    

    def scan(self, position):
        
        #Aktuell zu betrachtendes Terminal im String
        symbol = self.sentence[position+1]
        
        #Laeuft über aktuelles Itemset und sucht nach Terminal
        #Bei Erkennen eines Terminals wird es im aktuellen completedSet gespeichert
        for item in self.itemSetLists[position].itemSet:
            if item.regel.rightSide == symbol:
                
                tempItem = Item(item.regel, item.dot + 1, position)
                
                if position < len(self.completedSetLists) and self.completedSetLists:
                    self.completedSetLists[position].addItem(tempItem)
                
                else:
                    tempSet = Itemset()
                    tempSet.addItem(tempItem)
                    self.completedSetLists.append(tempSet)
    
    
    #Füllt completedSetlist an der Stelle p 
    #Oder setList an der Stelle p+1 falls noch weitere Symbole erkannt werden müssen
    def complete(self, currentItemSet, position):
        for item in self.completedSetLists[position].itemSet:
            tempItem = None
            if item.start < position:
                currentItemSet = self.itemSetLists[item.start]
            for item2 in currentItemSet.itemSet: 
                if item.regel.leftSide == item2.regel.rightSide[item2.dot] and item2.dot+1 == len(item2.regel.rightSide):
                    tempItem = Item(item2.regel, item2.dot + 1, item2.start)
                    #tempItem = Item(item2.regel, item2.dot + 1, position)
                    if self.completedSetLists[position].hasItem(tempItem) == False:
                        self.completedSetLists[position].addItem(tempItem)
                elif item2.dot+1 < len(item2.regel.rightSide) and item.regel.leftSide == item2.regel.rightSide[item2.dot]:
                    tempItem = Item(item2.regel, item2.dot + 1, item2.start)
                    if len(self.itemSetLists) <= position+1:
                        tempSet = Itemset()
                        tempSet.addItem(tempItem)
                        self.itemSetLists.append(tempSet)
                    elif self.itemSetLists[position+1].hasItem(tempItem) == False:
                        self.itemSetLists[position+1].addItem(tempItem)
    
    def validate(self):
        for item in self.completedSetLists[self.letterCount-1].itemSet:
            if item.regel.leftSide == "S":
                i = self.letterCount - 1
                j = 0
                b = Itemset()
                b.addItem(item)
                self.ungerParse(i, j, b)
            #else:
                #self.parseFound(False)
    
    def parseFound(self, result, tree):
        if result:
            print("Gültiger Parse gefunden")
            for item in tree: 
                item.__repr__()
                sys.exit(0)
        else:
            print("Kein gültiger Parse gefunden")
            sys.exit(1)
                    
    def ungerParse(self, i, j, tree):
        while i > 0:
            dot = tree.itemSet[j].dot 
            if tree.itemSet[j].regel.rightSide[dot-1].isupper():
                wj = tree.itemSet[j].regel.rightSide[dot-1]
                #print(tree.itemSet[j].__repr__())
                kj = tree.itemSet[j].start 
                pj = dot                
                for item in self.completedSetLists[i].itemSet:
                    wItem = item.regel.leftSide
                    kItem = item.start
                    pItem = item.dot
                    if wj == wItem:
                        if (pj-1 == 0 and kItem==kj) or (pj-1 > 0 and kItem-kj >= pj-1):
                            if tree.hasItem(item) == False:
                                tempItem = Item(item.regel, item.dot, item.start)
                                #print(tempItem.__repr__())
                                tree.addItem(tempItem)
                                #tree.__repr__()
                                self.ungerParse(i, j+1, tree)
                                tree.itemSet.remove(tree.itemSet[len(tree.itemSet)-1])
                return
            symbol = tree.itemSet[j].regel.rightSide[tree.itemSet[j].dot-1]
            #print(symbol)
            if symbol.islower() or symbol == "+" or symbol == "-":
                if tree.itemSet[j].regel.rightSide[tree.itemSet[j].dot-1] == self.sentence[i+1]:
                    tree.itemSet[j].dot -= 1
                    i -=1
            if tree.itemSet[j].dot == 0:
                j -= 1
                tree.itemSet[j].dot -= 1
            if tree.itemSet[j] == self.itemSetLists[0].itemSet[0]:
                self.parseFound(True, tree)
            
                        
                    