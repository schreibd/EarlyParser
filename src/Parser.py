
import sys
from Item import*
from Regel import*
from Itemset import*


class Parser():
    
    
    def __init__(self, grammar, sentence):
        self.grammar = grammar
        self.sentence = sentence[:0] + " " + sentence[0:]
        
        self.letterCount = len(self.sentence) - self.sentence.count(' ') 
        
        #Liste der Itemsets (active und prediction werden hier zusammengefasst (Konzept nach Fachliteratur))
        self.actPredSets = []
        #Liste der Itemsets (completed)
        self.completedSetLists = []
        
        #Initialisiere Startregel um ParseLoop zu beginnen     
        self.initializeParser()
    
    
    def __repr__(self):
        cSetLists = 0
        for itemSet in self.actPredSets:
            print("Active/Predicted Set: " + str(cSetLists))
            itemSet.__repr__()
            cSetLists += 1
        
        cCompletedsetLists = 0
        for itemSet in self.completedSetLists:
            print("Completed Set: " + str(cCompletedsetLists))
            itemSet.__repr__()   
            cCompletedsetLists += 1
    
    #Erstelle Startregel und f�ge sie dem ersten Itemset hinzu
    def initializeParser(self):
        tempSet = Itemset()
        for group in self.grammar.regeln.values():
            for rule in group:
                if rule.leftSide == "S" and len(self.actPredSets) == 0:
                    tempItem = Item(rule)
                    tempSet.addItem(tempItem)
                    self.actPredSets.append(tempSet)   
                elif rule.leftSide == "S":
                    tempItem = Item(rule)
                    self.actPredSets[0].addItem(tempItem)
    
    #Main-Loop der durch den Eingabesatz iteriert
    def parseLoop(self):
        counter = 0
        while counter < self.letterCount:
            if counter < len(self.actPredSets):
                currentItemSet = self.actPredSets[counter]
            else:
                self.parseFound(False, None)
            
            
            length = len(currentItemSet.itemList)
            oldLength = 0
            
            #Rufe Predictor so oft auf, bis sich Groesse des aktuell betrachteten 
            #Itemsets nicht mehr veraendert
            while oldLength < int(length):  
                self.predict(currentItemSet, counter)
                oldLength = length
                length = len(currentItemSet.itemList)
                
            #Rufe Scanner auf 
            self.scan(counter)
            
            
            if counter < len(self.completedSetLists):
                completedLength = len(self.completedSetLists[counter].itemList)
            else:
                completedLength = 0
            oCompletedLength = 0
            
            #Rufe Completor so oft auf, bis sich die Groesse des aktuell betrachteten 
            #Itemsets (completedSetLists[counter]) nicht mehr veraendert. 
            while oCompletedLength < int(completedLength):
                self.complete(currentItemSet, counter)
                oCompletedLength = completedLength
                completedLength = len(self.completedSetLists[counter].itemList)
                
            counter += 1 
        for item in self.completedSetLists[len(self.completedSetLists)-1].itemList:
            if item.regel.leftSide == "S" and item.start == 0:
                self.parseFound(True, None)
        self.parseFound(False, None)  
        
    
    #Predictor zum vorhersagen von Regeln
    #    dieser sucht nach Items, in welchen der Punkt vor einem NonTerminal zu finden ist
    def predict(self, currentItemSet, position):
        for group in self.grammar.regeln.values():  
            for rule in group:
                tempItem = None
                for item in currentItemSet.itemList:
                    #Falls Item bereits enthalten
                    if rule == item.regel:
                        tempItem = None
                        break
                    
                    #Greif hier nicht komplette Regel auf rechter Seite ab sondern nur das Zeichen nach dem Punkt
                    if rule.leftSide == item.regel.rightSide[item.dot]:
                        tempItem = Item(rule, 0, position)
                        
                if tempItem != None and self.actPredSets[position] != None:
                    self.actPredSets[position].addItem(tempItem)   
                    
                elif tempItem != None:
                    tempSet = Itemset().addItem(tempItem)
                    self.actPredSets.append(tempSet)
                    

    def scan(self, position):
        
        #Aktuell zu betrachtendes Terminal im String
        symbol = self.sentence[position+1]
        
        if self.grammar.hasSymbol(symbol):
        #Laeuft über aktuelles Itemset und sucht nach Terminal
        #Bei Erkennen eines Terminals wird es im aktuellen completedSet gespeichert
            for item in self.actPredSets[position].itemList:
                if item.regel.rightSide == symbol:
                
                    tempItem = Item(item.regel, item.dot + 1, position)
                
                    if position < len(self.completedSetLists) and self.completedSetLists:
                        self.completedSetLists[position].addItem(tempItem)
                
                    else:
                        tempSet = Itemset()
                        tempSet.addItem(tempItem)
                        self.completedSetLists.append(tempSet)
        else:
            self.parseFound(False, None)
        
    
    
    #Füllt completedSetlist an der Stelle p 
    #Oder actPredSets an der Stelle p+1 falls noch weitere Symbole erkannt werden müssen
    def complete(self, currentItemSet, position):
        for completedItem in self.completedSetLists[position].itemList:
            tempItem = None
            if completedItem.start < position:
                currentItemSet = self.actPredSets[completedItem.start]
            for item in currentItemSet.itemList: 
                if completedItem.regel.leftSide == item.regel.rightSide[item.dot] and item.dot+1 == len(item.regel.rightSide):
                    tempItem = Item(item.regel, item.dot + 1, item.start)
                    if self.completedSetLists[position].hasItem(tempItem) == False:
                        self.completedSetLists[position].addItem(tempItem)
                elif item.dot+1 < len(item.regel.rightSide) and completedItem.regel.leftSide == item.regel.rightSide[item.dot]:
                    tempItem = Item(item.regel, item.dot + 1, item.start)
                    if len(self.actPredSets) <= position+1:
                        tempSet = Itemset()
                        tempSet.addItem(tempItem)
                        self.actPredSets.append(tempSet)
                    elif self.actPredSets[position+1].hasItem(tempItem) == False:
                        self.actPredSets[position+1].addItem(tempItem)
    
    
    def parseFound(self, result, tree):
        self.__repr__()
        if result:
            print("Gültiger Parse gefunden")
            sys.exit(0)
        else:
            print("Kein gültiger Parse gefunden")
            sys.exit(1)
    