'''
Created on 10.05.2017

@author: Daniel
'''
#from lib2to3.pgen2.tokenize import group

class Grammatik(object):
    
    def __init__(self):
        #Regeln ist ein Dictionary geordnet nach Nichtterminalen
        #Key = Linke Seite einer Regel
        #Object = Liste mit rechten Regelseiten
        
        self.regeln = {}
    
    
    def addRegel(self, regel):
        if regel.leftSide in self.regeln:
            self.regeln[regel.leftSide].append(regel)
        else: 
            self.regeln[regel.leftSide] = [regel]
        
    
    def __repr__(self):
        for group in self.regeln.values():
            for regel in group:
                result = regel.__repr__()
                print(result)