class Grammatik(object):
    
    def __init__(self):
        
        #Regeln ist ein Dictionary geordnet nach Nichtterminalen
        #Key = Linke Seite einer Regel
        #Object = Liste mit rechten Regelseiten
        
        self.regeln = {}
    
    
    def addRegel(self, regel):
        #Wenn Linke Seite einer Regel bereits als Key im Dictionary vorhanden ist, 
        #fuege  dem Key die Rechte Seite der Regel als Objekt hinzu
        if regel.leftSide in self.regeln:
            self.regeln[regel.leftSide].append(regel)
        else: 
            self.regeln[regel.leftSide] = [regel]
        
    
    def __repr__(self):
        for group in self.regeln.values():
            for regel in group:
                result = regel.__repr__()
                print(result)