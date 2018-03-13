import unittest

def isunique(string):
    '''
    Returns True, if all characters in string are unique. And False otherwise.
    Implemented with Hash

    >>> isunique('abcde')
    True
    
    >>> isunique('abcdea')
    False
    
    '''
    hash = dict()
    for letter in string:
        if hash.has_key(letter):
            return False
        hash[letter] = 1
     
    return True

def isunique2(string):
    '''
    Returns True, if all characters in string are unique. And False otherwise.
    Implemented without additional structures

    >>> isunique2('abcde')
    True
    
    >>> isunique2('abcdea')
    False
    
    '''
    for i, l in enumerate(string, 1):
        if l in string[i:]:
            return False
    return True

def isunique3(string):
    '''
    Returns True, if all characters in string are unique. And False otherwise.
    TODO: Implemented with bit vector.
    TODO: Assumed we have only letters, case is not important. (26 letters).

    >>> isunique3('abcde')
    True
    
    >>> isunique3('abcdea')
    False
    
    '''
    bits = 0
    for letter in string:
        val = ord(letter.lower()) - ord('a')
        if bits & (1 << val ):
            return False
        bits  = bits | (1 << val )
        print bin(bits)
    return True
    

class TestUnique(unittest.TestCase):
    dataT = ['abcde', 'aqwsxz', '', 'rewqaz', 'qazxswedcvfrtgbnhyujmkiolp']
    dataF = ['abcdea', 'aaqwsxz',   'rewqazz', 'qazxswedcvfrtgbnhyujmkiolpq']
    def test_unq(self):
        for data in self.dataT:
            print data
            self.assertTrue(isunique(data))
            self.assertTrue(isunique2(data))
            self.assertTrue(isunique3(data))

        for data in self.dataF:
            print data 
            self.assertFalse(isunique(data))
            self.assertFalse(isunique2(data))
            self.assertFalse(isunique3(data))

        
####

if __name__ == '__main__':
   unittest.main() 

   #import doctest
   #doctest.testmod()
   
   #print isunique3('abcdefgha')
   