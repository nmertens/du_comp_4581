# Hashtable ADT Lab
# Last edited: 2/5/2022

import numpy as np

class MyHashtable() :
    
    def __init__(self,size) :
        self.size = size
        self.hashtable = np.array([None]*self.size)
    
    def __str__(self):
        return str(self.hashtable)
        
    def hash(self,key) :
        
        # Hash function h(x) = x%10
        index = ord(key[0])%self.size
        
        if self.hashtable[index] == None :
            return index
        else :
            
            # Implementing linear probing
            while self.hashtable[index] != None :
                index = (index+1)%self.size
                
            return index
        
    def insert(self,key) :
        
        index = self.hash(key)
        self.hashtable[index] = key
    
    def delete(self, key):
        index = ord(key[0])%self.size
        
        if self.hashtable[index] != key :
            while self.hashtable[index] != key and self.hashtable[index] != None :
                index = (index+1)%self.size
                
        if self.hashtable[index] == key :
            self.hashtable[index] = 'Deleted'
        else :
            next     
        
    def search(self,key) :
        
        index = ord(key[0])%self.size
        
        if self.hashtable[index] != key :
            while self.hashtable[index] != key and self.hashtable[index] != None :
                index = (index+1)%10
                
        if self.hashtable[index] == key :
            return index
        else :
            return None

s = MyHashtable(10)
s.insert("amy") #97
s.insert("chase") #99
s.insert("chris") #99
print(s.search("amy"))
print(s.search("chris"))
print(s.search("alyssa"))
s.delete("chase")
print(s.search("chris"))
