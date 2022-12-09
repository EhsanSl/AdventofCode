

#f = open('input.txt', 'r' )
#line = f.readline()
#n = 0 # row counter 
#= 0 # column counter 


#jng = [i.split() for i in string.split('\n')]

def check_up(arr, i, j):   
        while i - 1 >= 0 : 
            if arr[i][j] <= arr[i-1][j]: #shorter the not visible 
                return False 
            i -= 1
        return True 

def check_down(arr, i, j):   
        while i + 1 < len(arr) : 
            if arr[i][j] <= arr[i+1][j]: #shorter the not visible 
                return False 
            i += 1
        return True 
    
def check_right(arr, i, j):    
        while j + 1 < len(arr[0]) : 
            if arr[i][j] <= arr[i][j+1]: #shorter the not visible 
                return False 
            j += 1
        return True 


def check_left(arr, i, j):   
        while j - 1 >= 0 : 
            if arr[i][j] <= arr[i][j-1]: #shorter the not visible 
                return False 
            j -= 1
        return True 



def _check(arr, i , j) :
        if i == 0 or j == 0 or i == len(arr) or j == len(arr[0]): 
            return 1 # the tree is on the edge
        elif  check_up(arr, i , j) or check_down(arr, i , j) or check_right(arr, i , j) or check_left(arr, i , j) : 
            return 1 #its visible from some direction
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