
def SimpleSymbols(str):
  
  for i in range(len(str)):
    #print i
    #print str[i]
    #print str[i].isalpha()
    if str[i].isalpha()  and (i==0 or i== len(str)-1):
      return "false"
    elif str[i].isalpha():
      if  (str[i-1] != "+")  or (str[i+1] != "+"):
        return "false"
    
  return "true" 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SimpleSymbols(raw_input()) 

