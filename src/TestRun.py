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
regel5 = Regel("E", "EPF")
regel6 = Regel("O", "b")
regel7 = Regel("E", "O")
grammatik.addRegel(regel2)
grammatik.addRegel(regel3)
grammatik.addRegel(regel4)
grammatik.addRegel(regel5)
grammatik.addRegel(regel6)
grammatik.addRegel(regel7)
parser = Parser(grammatik, "ab")
parser.initializeParser()
parser.parseLoop()
parser.itemSetLists[0].__repr__()
