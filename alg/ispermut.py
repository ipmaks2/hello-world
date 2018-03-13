import unittest

def ispermut(strA, strB):
    '''
    Returns True, if strA is permutation of strB. And False otherwise.
    Implemented with Hash

    >>> ispermut('abcde', 'edcba')
    True
    
    >>> ispermut('abcdea', 'asds')
    False
    
    '''
    hashA = dict()
    hashB = dict()
    
    if len(strA) != len(strB):
        return False
        
    for letter in strA:
        hashA[letter] = hashA.get(letter, 0) + 1

    for letter in strB:
        hashB[letter] = hashB.get(letter, 0) + 1
        # TODO Add early return False
        # letter not present in hashA
        # letter present, but count > then in hashA
    
    if hashA == hashB:
        return True
        
    return False


class TestUnique(unittest.TestCase):
    dataT = [('abc', 'cba'), ('', ''), ('qqwweerr', 'qwerqwer')]
    dataF = [('a', ''), ('qwerqwer', 'qwer'), ('qwert', 'asdfg')]
    def test_perm(self):
        for data in self.dataT:
            print data
            self.assertTrue(ispermut(*data))
            
        for data in self.dataF:
            print data 
            self.assertFalse(ispermut(*data))
            
        
####

if __name__ == '__main__':
    pass
    #unittest.main() 

    #import doctest
    #doctest.testmod()
   
    #print isunique3('abcdefgha')
   