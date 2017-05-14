'''
Created on 08.05.2017

@author: Daniel
'''

class Regel():

    #Regeln bestehen aus linker Seite einer Regel
    def __init__(self, leftSide, rightSide):
        self.leftSide = leftSide
        self.rightSide = rightSide
    #Liefert die L�nge einer Regel zur�ck. 
    #Da wir eine kontextfreie Grammatik verwenden, findet sich auf der
    #linken Seite der Regel immer nur ein Nichtterminal. 
    #Aus diesem Grund lassen wir uns nur die L�nge der rechten Seite 
    #zur�ckgeben
    def __len__(self):
        return len(self.rightSide) 
    #Ausgabe der Regel im Format LinkeSeite -> RechteSeite      
    def __repr__(self):
        return "Regel {0} -> {1}".format(self.leftSide, ''.join(self.rightSide))
    
