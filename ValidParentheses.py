#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#from solving https://www.codewars.com/kata/52774a314c2333f0a7000688

def is_valid(brackets):
    openBracket = 0
    for i in brackets:
        if (i == "("):
            openBracket = openBracket + 1
        elif (i == ")"):
            if openBracket < 1:
                return False
            openBracket = openBracket - 1
    
    if (openBracket > 0):
        return False
    else:
        return True


# In[2]:


print(is_valid("()"))
print(is_valid(")(()))"))
print(is_valid("("))
print(is_valid("(())((()())())"))


# In[ ]:




