'''
Created on 18.05.2017

@author: Daniel
'''
from Parser import *
from Grammatik import *
 
grammatik = Grammatik()
regel1 = Regel("S", "E")
regel2 = Regel("E", "EQF")
grammatik.addRegel(regel1)
regel3 = Regel("E", "F")
regel4 = Regel("F", "a")
regel5 = Regel("Q", "+")
regel6 = Regel("Q", "-")
grammatik.addRegel(regel2)
grammatik.addRegel(regel3)
grammatik.addRegel(regel4)
grammatik.addRegel(regel5)
grammatik.addRegel(regel6)
parser = Parser(grammatik, "a-a+a-a+a-a-a-a-a-a-a-a+a+a+a+a+a+a+a+a+a+a")
parser.initializeParser()
parser.parseLoop()
parser.__repr__()
#parser.itemSetLists[4].__repr__()
#parser.completedSetLists[4].__repr__()

