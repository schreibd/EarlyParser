from Parser import *
from Grammatik import *
 
grammatik1 = Grammatik()
regel1 = Regel("S", "E")
regel2 = Regel("E", "EQF")
grammatik1.addRegel(regel1)
regel3 = Regel("E", "F")
regel4 = Regel("F", "a")
regel5 = Regel("Q", "+")
regel6 = Regel("Q", "-")
grammatik1.addRegel(regel2)
grammatik1.addRegel(regel3)
grammatik1.addRegel(regel4)
grammatik1.addRegel(regel5)
grammatik1.addRegel(regel6)
#Spuckt Fehler aus
#parser = Parser(grammatik, "a+a---")
parser = Parser(grammatik1, "a-a+a")
parser.parseLoop()
#parser.__repr__()
#parser.validate()
#parser.itemSetLists[4].__repr__()
#parser.completedSetLists[4].__repr__()

