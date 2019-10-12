#!/usr/bin/env python
# coding: utf-8

# DFA starting with strings with 00

# In[ ]:



d={'a':{'1':'0','0':'1'},'b':{'0':'0','1':'1'}}
def reverse(string):
    string = string[::-1]
    return string
n=int(input())
while(n):
    _str=input()
    _str=reverse(_str)
    o=''
    st='a'
    for i in _str:
        o=o+d[st][i]
        if o[-1]=='1':
          st='b'
    print(f"RESULT= {reverse(o)}")


# In[ ]:


mealy machine for two compliments


# In[ ]:


def twos_comp(val, bits):
    
    if (val & (1 << (bits - 1))) != 0: 
        val = val - (1 << bits)     
    return val                  


# regular expression
# 

# In[ ]:


n={'a':{'0':'even','1':'odd'},'b':{'0':'odd','1':'even'}}
_str=input()
st='a'
for i in _str:
  o=d[st][i]
  if o=='odd':
    st='b'
  else:
    st='a'
print(f"RESULT= {o}")


# In[ ]:





# In[ ]:




