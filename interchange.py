
# creating a innber  list 
numbers=[1,2,3,4,5,6]

# creating the function to swap the first and last elmenet from list 
def swap_Element(inn):
    if len(inn)>1:
        #swapping the first and last element
        inn[0],inn[-1]=inn[-1],inn[0]
    return inn

print(swap_Element(numbers))    

#written by zala nirbhay(TY-BCA)

