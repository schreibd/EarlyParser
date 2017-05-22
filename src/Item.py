class Item():

    def __init__(self, regel, dot=0, start=0, previous=None, completing=None):
        self.regel = regel
        self.dot = dot
        self.start = start
        self.previous = previous
        self.completing = completing

    def __repr__(self):
        rechteSeite = list(self.regel.rightSide)
        rechteSeite.insert(self.dot, "●")
        rechteSeite.insert(rechteSeite.__len__(), "@"+str(self.start))
        return "Regel {0} -> {1}".format(self.regel.leftSide, ' '.join(rechteSeite))
