# Hashtable ADT Lab
# Last edited: 2/5/2022

import numpy as np

class MyHashtable():
    
    def __init__(self,size):
        self.size = size
        self.table = np.array([None]*self.size)
    
    def __str__(self):
        return str(self.table)
        
    def hash(self,element):
        
        # Hash function h(x) = x%10
        index = ord(element[0])%self.size
        
        if self.table[index] == None:
            return index
        else:
            
            # Implementing linear probing
            while self.table[index] != None:
                index = (index+1)%self.size
                
            return index
        
    def insert(self,element):
        
        index = self.hash(element)
        self.table[index] = element
    
    def delete(self, element):
        index = ord(element[0])%self.size
        
        if self.table[index] != element:
            while self.table[index] != element and self.table[index] != None:
                index = (index+1)%self.size
                
        if self.table[index] == element:
            self.table[index] = 'Deleted'  
        
    def member(self,element):
        
        index = ord(element[0])%self.size
        
        if self.table[index] != element:
            while self.table[index] != element and self.table[index] != None:
                index = (index+1)%10
                
        if self.table[index] == element:
            # return index
            return True
        else:
            # return None
            return False

s = MyHashtable(10)
s.insert("amy") #97
s.insert("chase") #99
s.insert("chris") #99
print(s.member("amy"))
print(s.member("chris"))
print(s.member("alyssa"))
s.delete("chase")
print(s.member("chris"))