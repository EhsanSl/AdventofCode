

#f = open('input.txt', 'r' )
#line = f.readline()
#n = 0 # row counter 
#= 0 # column counter 


#jng = [i.split() for i in string.split('\n')]

def check_up(arr, i, j):   
    if  i-1 > 0 :
        if arr[i][j] > arr[i-1][j]: #if equal; or shorter

            return True # visible  
        else : 
            print("Visible from up")
            return False # not visible 

    return True 

def check_down(arr, i, j):   
    if  i+1 < len(arr) :
        if arr[i][j] > arr[i+1][j]: #if equal; or shorter

            return True # visible  
        else : 
            print("Visible from down")
            return False #not visible

    return True 
    
def check_right(arr, i, j):    
    if  j+1 < len(arr[0]):
        if arr[i][j] > arr[i][j+1]: #if equal; or shorter

            return True #  visible  
        else : 
            print("Visible from right")
            return False #not visible 

    return True 

def check_left(arr, i, j):    
    if  j-1 > 0 :
        if arr[i][j] > arr[i][j-1]: #if equal; or shorter

            return True # visible  
        else : 
            print("Visible from left")
            return False #not visible 
    return True 

def _check(arr, i , j) :
    if check_up(arr, i , j) or check_down(arr, i , j) or check_right(arr, i , j) or check_left(arr, i , j) : 
        return +1 #its visible from some direction
    return 0 



lst=[]
_arr = [[3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0]]

for  i in range (len(_arr)) : #rows
    for j in range(len(_arr[0])): #columns 
        print(f"i: {i}, j:{j}, val: {_arr[i][j]}")
        lst.append(_check(_arr, i, j)) #add the number of visibles to list

print(f"Number of visible Trees: {sum(lst)}")