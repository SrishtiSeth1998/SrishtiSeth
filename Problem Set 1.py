#!/usr/bin/env python
# coding: utf-8

# # Question 1
# 

# What data type is each of the following (evaluate where necessary)?
# 
# 1. 5 
# 2. 5.0
# 3. 5 > 1
# 4. '5'
# 5. 5 * 2
# 6. '5' * 2
# 7. '5' + '2'
# 8. 5 / 2
# 9. 5 % 2
# 10. {5, 2, 1}
# 11. 5 == 3
# 12. Pi (the number)

# In[7]:


print(type(5))
print(type(5.0))
print(type(5>1))
print(type(5*2))
a = '5'*2
print(type(a))
print(type('5'+'2'))
print(type('5/2'))
print(type('5%2'))
print(type({5,2,1}))
print(type(5==2))
Pi = 3.14
print(type(Pi))


# # Question 2

# Write (and evaluate) python expressions that answer these questions:
# 1. How many letters are there in 'Supercalifragilisticexpialidocious'?
# 2. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring?

# In[8]:


a = 'Supercalifragilisticexpialidocious'
print(len(a)) 
print('ice' in a)


# 3. Which of the following words is the longest: Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or Bababadalgharaghtakamminarronnkonn? 

# In[73]:


lst = ['Bababadalgharaghtakamminarronnkonn','Honorificabilitudinitatibus','Supercalifragilisticexpialidocious']

longest = len(lst[0]) #setting the first number in the list as the longest length 
temp = lst[0]   # creating a temp variable and giving it the index 0 value

for i in lst:
    if len(i) >= longest:  # now comparing the list values with the longest variable
        longest = len(i)   # swapping if the len(i) is greater 
        temp = i           # saving the i value in temp
    else:
        continue
          
    print("Longest word=",temp , longest)
        


# 4. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?
# 

# In[75]:


composer = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
composer.sort() # simply just using the sort function
print(composer)


# # Question 3

# Implement function triangleArea(a,b,c) that takes as input the lengths of the 3 sides of a triangle and returns the area of the triangle. By Heron's formula, the area of a triangle with side lengths a, b, and c is s(s - a)(s -b)(s -c), where s = (a+b+c)/2. 

# In[83]:


def triangleArea(a,b,c):
    import math as m  # math function for the square root function

    s = (a+b+c)/2
    print(s)
    
    area = m.sqrt(s*(s-a)*(s-b)*(s-c)) 
    return area
    
triangleArea(2,2,2)


# # Question 4

# Write a program in python to separate odd and even integers in separate arrays.

# In[6]:


from array import *

arr = array('i', [])         # defining an empty array
EvenArr = array('i', []) 
OddArr = array('i', [])

lg = int(input('Enter the length of the array =')) # length of the input array 

for i in range(lg):
    ele = int(input('Enter Element {}: ' .format(i)))
    arr.append(ele)                                    # adding elements one by one
    
print(arr)

for e in arr:                
    if e%2 == 0:                   
        EvenArr.append(e)
    else:
        OddArr.append(e)
        
print('The even arrays are:', EvenArr)
print('The odd arrays are:', OddArr)          

#same steps are applied for working in a list 


# # Question 5

# a.  Write a function inside(x,y,x1,y1,x2,y2) that returns True or False 
# depending on whether the point (x,y) lies in the rectangle with lower left 
# corner (x1,y1) and upper right corner (x2,y2).
# 

# In[12]:


def inside(x, y, x1, y1, x2, y2):     
    if x1 <= x <= x2 and y1 <= y <= y2:   # the point lies between the corner points 
        return True
    else:
        return False
    
res1 = inside(1, 1, 0, 0, 2, 3)     #calling the function
print(res1)
res2 = inside(-1, -1, 0, 0, 2, 3)
print(res2)


# b.   Use function inside() from part a. to write an expression that tests whether 
# the point (1,1) lies in both of the following rectangles: one with lower left 
# corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower 
# left corner (0.5, 0.2) and upper right corner (1.1, 2)

# In[15]:


rec1 = inside(1, 1, 0.3, 0.5, 1.1, 0.7)  
rec2 = inside(1, 1, 0.5, 0.2, 1.1, 2)

print(rec1)   
print(rec2)   

if rec1 and rec2 == True:      
    print("point(1,1) inside the triangle")
else:
    print("point(1,1) is NOT inside the triangle")


# #  Question 6

# You can turn a word into pig-Latin using the following two rules (simplified):
# 1. If the word starts with a consonant, move that letter to the end and append 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
# 2. If the word starts with a vowel, simply append 'way' to the end of the word. For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
# 
# Write a function pig() that takes a word (i.e., a string) as input and returns its pigLatin form. Your function should still work if the input word contains upper case 
# characters. Your output should always be lower case however

# In[19]:


def pig(word):     # defining the function
    
    vowels = ['a','e','i','o','u','A', 'E', 'I', 'O', 'U']   # storing the vowels in a list
    if word[0] in vowels:       # using indexing 
        pigLatin = word + 'way'
        return pigLatin
    else:                                 # others are the constants
        pigLatin = word[1:]+word[0]+'ay'   # using indexing
        return pigLatin

print(pig('happy'))
print(pig('Enter'))    


# # Question 7

# File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic. Write a function bldcount() that reads the file with name name and reports (i.e., prints) how many patients there are in each bloodtype.

# In[2]:


f = open('bloodtype.txt', 'r')
print(f.read())


# In[19]:


def bldcount(filename):
    # 'will count patients in each bloodtype'
    
    bld = ['AB', 'A', 'B', 'O', 'OO']  # storing diffrent types of bloodtypes
    infile = open(filename) 
    content = infile.read()
    bloodtype = content.split()   # this function will make the list of the data in file
    
    for i in bld:    
        count = bloodtype.count(i)   # counting loop for 'bld list' of patients
        if count == 0:               # condition to get the no of patient according the the bloodtype
            print(f'There are no patient for blood type {i}.')
        else:
            print(f'There are {count} patient for blood type {i}.')
    
bldcount('bloodtype.txt')


# # Question 8

# Write a function curconv() that takes as input:
# 1.  a currency represented using a string (e.g., 'JPY' for the Japanese Yen or 'EUR' for the Euro)
# 2. and amount
# and then converts and returns the amount is US Dollars.
# 

# In[132]:


def curconv(currency, amount):
    'will convert the currency into US'
    
    import re                             # regualr expression to extract patterns from the file 
    
    infile = open('currencies.txt')
    content = infile.read()
    data = content.strip('\t').split()    # this removes the spaces b/w the data and converting it to a list
    #print(content)
    
                # finding a pattern of captial letters as the currency is in all caps
    code = []             
    for line in data:
        if re.search(r"^[A-Z]+$", line):  # selecting the pattern for generating all caps
            code.append(line)             # storing a retrived currency to a list 
        
    #print(code)
    
    
    exchange_rate = []
    for rate in data:                     # picking out the numbers
        if re.search("\d", rate):         # '/d' for numbers
            exchange_rate.append(rate)    # creating a list 
    
    #print(exchange_rate)
    
    
    
    # now we can create a dictionary of the 2 lists
    file_dict = dict(zip(code,exchange_rate))
    #print(file_dict)
    
                   
    for i in file_dict:
        if currency == i:                     # condition will look for the curriency that was called in the function
            rates = float(file_dict.get(i))   # converting from string to float as the exchange rate was in a string format
            result = rates*amount             # storing the final result
            return result
    


# In[133]:


curconv('AUD', 100)


# In[134]:


curconv('JPY', 100)


# # Question 9

# 1. Trying to add incompatible variables, as in adding 6 + ‘a
# 
# Answer - 'Syntax Error'

# In[112]:


6 = 'a'


# 2. Referring to the 12th item of a list that has only 10 items
# 
# Answer: IndexError - List index out of range

# In[117]:


lst = [19,66,75,32,56,46,43,3,332,89]
print(lst[9])
print(lst[11])


# 3. Using a value that is out of range for a function’s input, such as calling math.sqrt(-1.0)
# 
# Answer: TypeError - math.sqrt() takes exactly one argument (2 given)

# In[118]:


from math import *

print(sqrt(-1,0))


# 4. Using an undeclared variable, such as print(x)when x has not been defined 
# answer: NameError

# In[119]:


y = 10
print(x)


# 5. Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory. 
# 
# Answer: 'NAmeError' 

# In[120]:


infile = open(text.txt)
print(infile)


# # Question 10

# Encryption

# In[127]:


def frequencies(text):                     # defining a function to count the occurence of alphabets in the string
    letters = 'abcdefghijklmnopqrstuvwxyz'
    counts = [0] * 26                      # initialize a list of zeros to store the counts for all alphabets 

    for char in text:
        char = char.lower()                # convert character to lowercase as the frequency func is only in lower cases
        
        if char in letters:
            index = letters.index(char)   # getting the index of the character in the string
            counts[index] += 1            # increment the count for that character

    return counts

result1 = frequencies('The quick red fox got bored and went home')  # storing the function into result1
print(result1)

result2 = frequencies('apple')
print(result2)

