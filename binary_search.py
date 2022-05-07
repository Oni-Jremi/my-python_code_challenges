# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:04:51 2022

@author: Oni Remi John
"""

def binary_search(list, target):
    """
    Binary search only works well with an ordered list of numbers
    1. Compares the middle number with the target number
        a. If the middle number is greater than the target number,
        then the target number is on the left side of the list.
        b. If the middle number is lesser than the target number,
        then the target number is on the right side of the list.
    2. Splits the list into two parts and discard the part where the
    target number is not existing based on the comparison above.
    3. Keeps repeating steps (1a or 1b) and then step 2 till the target
    number is found. Else return None
    """
    # Set a variable to point to the index of the first element in the list
    first = 0
    
    #Set a variable to point to the index of the last element in the list
    last = len(list) - 1
    
    #Initialize a loop to keep checking if there is atleast an element
    #in the list
    while first <= last:
        
        #Set a variable to get the index of the mid element in the list
        midpoint = (first + last) // 2
        print(midpoint)
        #If element is found through slicing using the mid indexing
        if list[midpoint] == target:
            
            #If there's another duplicate element just before the currently
            #found element
            if midpoint-1 >= 0 and list[midpoint-1] == target:
                
                #Update the variable last to point to the index of this 
                #duplicate element
                last = midpoint - 1
                
            #If not, return the index of the found element    
            else:
                return midpoint
            
        # -- Step 1b from the docstring above
        elif list[midpoint] < target:
            
            #Update the variable first to point to the index of the 
            #element after the mid element
            first = midpoint + 1
            
        # -- Step 1a from the docstring above
        elif list[midpoint] > target:
            
            #Update the variable last to point to the index of the 
            #element before the mid element
            last = midpoint - 1
    #If the element still hasn't been found, return None
    return None

num = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,24,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,8,10,12,21,25,30]
print(binary_search(num, 2))
