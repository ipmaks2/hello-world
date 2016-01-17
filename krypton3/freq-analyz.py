#!/usr/bin/python
import sys
import string

def dic_val(pair):
    return pair[-1]
chars={}
total=0
lines=''
for file in ['found1','found3']:
    for line in open(file ,'r'):
        lines+=line + '\n' 
	for char in line:
            if char in chars:
                chars[char]+=1
            else:
                chars[char]=1
            total +=1
#for key in sorted(chars.items(),key=dic_val):
    #print key

freq1=' ETAONRISHDLFCMUGYPWBVKJXQZ' # normal - result
freq2=' ETAOINSHRDLCUMWFGYPBVKJXQZ'
#for key in sorted(chars.items(),reverse=True,key=dic_val):
#    print key[0],

print ()


freq_analyzed=''.join([ item[0] for item in sorted(chars.items(),reverse=True,key=dic_val)])
#freq_analyzed='SQJUBNCGDZVWMYTXKELAFIOHRP' # crypted - from
#print (lines)
l=26
l1=26
m=1024
myinput=''
mytrim=0
myhide=1
mylines=lines
mydelete = ' ' 
while myinput !='exit':
    print freq1 #[:l+3] 
    print freq_analyzed[:l]
    print 
    mylines = lines 
    print(mylines[:m].translate(string.maketrans(freq_analyzed[:l1],freq1[:l].lower()+' '*(l1-l)),mydelete))
    myinput=raw_input()
    if (myinput ==  '>'): 
        l+=1
    elif (myinput == '<'):
        l-=1
    elif (myinput == 'nospace'):
        mydelete=' ' 
    elif (myinput == 'space'):
        mydelete=''
    elif (myinput =='r'):
        freq1= freq1[:l-1] + freq1[l] + freq1[l-1]+freq1[l+1:]


#print freq1
#print freq2
#print freq_analyzed


#cat found3 | tr [SQJUBNCGDZVW] [etaoinshrdlu]










                
        
