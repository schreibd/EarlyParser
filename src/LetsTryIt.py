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
        self.count = len(self.name) - self.name.count(' ')
        print(self.count)
    
    
        '''
        Constructor
        '''
        