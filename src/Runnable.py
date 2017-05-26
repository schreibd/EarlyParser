
from Grammatik import *
from Parser import * 

grammatik = Grammatik()
regel1 = Regel("S", "E")
regel2 = Regel("E", "EQF")
regel3 = Regel("E", "F")
regel4 = Regel("F", "a")
regel5 = Regel("F", "b")
regel6 = Regel("Q", "+")
regel7 = Regel("Q", "-")
regel8 = Regel("E", "EPF")
regel9 = Regel("P", "*")
regel10 = Regel("P", "/")

grammatik.addRegel(regel1)
grammatik.addRegel(regel2)
grammatik.addRegel(regel3)
grammatik.addRegel(regel4)
grammatik.addRegel(regel5)
grammatik.addRegel(regel6)
grammatik.addRegel(regel7)
grammatik.addRegel(regel8)
grammatik.addRegel(regel9)
grammatik.addRegel(regel10)

parser = Parser(grammatik, "a-b+a/a-b")
parser.parseLoop()

