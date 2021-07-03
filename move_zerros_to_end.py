"""https://www.codewars.com/kata/moving-zeros-to-the-end/train/python
Write an algorithm that takes an array and moves all of the
zeros to the end, preserving the order of the other elements.
move_zeros([False,1,0,1,2,0,1,3,"a"]) # return [1,2,2,1,3,"a", False]
"""
def move_zeros(array):
    #your code here
    new = []
    zeros = []
    strbool = []
    
    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            zeros.append(array[i])
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(array[i])
            elif type(array[i]) == bool or type(array[i]) == str:
                strbool.append(array[i])
            else: 
               new.append(array[i])
        else:
            new.append(array[i])
    
    return new + strbool + zeros

print(move_zeros([False,1,0,1,2,0,1,3,"a", True, 0, "Wellcome"]))
#%%
ddef move_zeros(array):
    new = []
    zeros = []
    
    for i in range(len(array)):
        if array[i] == 0 :
            zeros.append(array[i])
        else:
            new.append(array[i])
    return new + zeros
print(move_zeros([13,0,12,0,21,0,1,2,4,5,6,0,3,0,1]))
# %%


# %%
