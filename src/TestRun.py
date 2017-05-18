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
grammatik.addRegel(regel2)
grammatik.addRegel(regel3)
grammatik.addRegel(regel4)
parser = Parser(grammatik, "aa")
parser.initializeParser()
parser.parseLoop()
#parser.itemSetLists[0].__repr__()
#parser.completedSetLists[1].__repr__()
