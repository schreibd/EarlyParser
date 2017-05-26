class Item():

    #Ein Earley Item besteht aus:
    #        - Produktionsregel
    #        - einem int Wert, der die Stelle des Punktes auf der rechten Regelseite darstellt
    #                    ist der Punkt am Ende der rechten Regelseite wurde die rechte Seite erkannt und kann reduziert werden
    #                    ist der Punkt vor einem Nonterminal kann dieses geshiftet werden
    #                    ist der Punkt zu Beginn handelt es sich um ein Predicted Item da es vom Predictor vorausgesagt wurde 
    #        - einem int Wert der die Zeichenposition beim Start der Erkennung angibt


    def __init__(self, regel, dot=0, start=0):
        self.regel = regel
        self.dot = dot
        self.start = start


    def __repr__(self):
        rechteSeite = list(self.regel.rightSide)
        rechteSeite.insert(self.dot, "●")
        rechteSeite.insert(rechteSeite.__len__(), "@"+str(self.start))
        return "{0} -> {1}".format(self.regel.leftSide, ' '.join(rechteSeite))
