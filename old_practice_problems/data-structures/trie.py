# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:19:21 2020

@author: rowe1
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.tail = False #redundant since we also use '*' to denote word end, but good practice

class TrieTree(object):
    def __init__(self, val = ''):
        self.root = Node(val)
        self.root.tail=True
    
    def add(self, word):
        '''
        Adds word to trie
        '''
        curr = self.root
        for letter in word:
            
            #CHECK IF LETTER IS IN CHILDREN
            if letter in curr.children:
                curr = curr.children[letter]

            else: #IF LETTER IS NOT IN CHILDREN THEN APPEND LETTER TO CHILDREN
                curr.children[letter] = Node(letter)
                curr = curr.children[letter]
                
        if curr.tail: #CHECK IF WORD WAS ALREADY IN THE TRIE
            print(word,'already exists')
        else: #OTHERWISE MAKE NOTE THAT THIS IS THE END OF A WORD
            curr.tail = True

            
        return None
    
    def find(self, word):
        '''
        Locates word within trie, returns: (Existence as Prefix, Existence as Complete Word)
            
            True, True if word appears as a full word
            
            True, False if it appears in the trie, but only as a prefix
            
            False, False if it is not in the trie as a prefix or a word
        '''
        curr = self.root
        for letter in word:
            #SEE IF LETTER IS IN CHILDREN OF CURRENT NODE
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False, False #WORD IS NOT IN TREE
        
        if curr.tail:
            return True, True #WORD IS A PREFIX AND A FULL WORD
        else:
            return True, False #PREFIX BUT NOT A FULL WORD




if __name__ == '__main__':
    root = TrieTree()
    
    words = ['wait', 'waiter', 'shop', 'shopper', 'wait']
    
    for word in words:
        root.add(word)
    
    for word in ['','wait','waits','shopp','wai','shop','shopping','shoppings','shipping']:
        print(word,root.find(word))
    
                    
                
        
        
        
        
        
        
        
        
        
        
        
        
        