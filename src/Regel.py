class Regel():

    #Regeln bestehen aus linker und rechter Seite
    def __init__(self, leftSide, rightSide):
        self.leftSide = leftSide
        self.rightSide = rightSide
        
    #Liefert die L�nge einer Regel zur�ck. 
    #Da wir eine kontextfreie Grammatik verwenden, besteht die
    #linke Seite einer Regel immer nur aus einem Nichtterminal der Laenge 1. 
    #Aus diesem Grund lassen wir uns nur die Laenge der rechten Seite 
    #zurueckgeben
    def __len__(self):
        return len(self.rightSide) 
    
    #Ausgabe der Regel im Format LinkeSeite -> RechteSeite      
    def __repr__(self):
        return "{0} -> {1}".format(self.leftSide, ''.join(self.rightSide))
    
    #Vergleichsoperator für eigene Datenstruktur überschrieben
    def __eq__(self, other):
        if self.leftSide == other.leftSide:
            if self.rightSide == other.rightSide:
                return True
        return False
    
