'''
Created on 12.05.2017

@author: Daniel
'''

class LetsTryIt(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        
        #self.name = name
        #self.count = len(self.name) - self.name.count(' ')
        #print(self.count)
        self.name = name
        self.sentence = self.name[:0] + " " + self.name[0:]

    
        '''
        Constructor
        '''
    def __repr__(self,):
        print(len(self.sentence))