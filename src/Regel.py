class Regel():

    #Regeln bestehen aus linker und rechter Seite
    def __init__(self, leftSide, rightSide):
        self.leftSide = leftSide
        self.rightSide = rightSide
        
    #Liefert die L�nge einer Regel zur�ck. 
    #Da wir eine kontextfreie Grammatik verwenden, findet sich auf der
    #linken Seite der Regel immer nur ein Nichtterminal. 
    #Aus diesem Grund lassen wir uns nur die Laenge der rechten Seite 
    #zurueckgeben
    def __len__(self):
        return len(self.rightSide) 
    #Ausgabe der Regel im Format LinkeSeite -> RechteSeite      
    def __repr__(self):
        return "Regel {0} -> {1}".format(self.leftSide, ''.join(self.rightSide))
    
    def __eq__(self, other):
        if self.leftSide == other.leftSide:
            if self.rightSide == other.rightSide:
                return True
        return False
    
