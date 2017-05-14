'''
Created on 12.05.2017

@author: Daniel
'''

class LetsTryIt(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        
        self.name = name
        
    def __repr__(self, position):
        print(self.name[position + 1])
        
    def changeName(self, name):
        self.name = name
        
    def compare(self):
        if self.name == None:
            print("Ja kann man")
        