

#f = open('input.txt', 'r' )
#line = f.readline()
#n = 0 # row counter 
#= 0 # column counter 


#jng = [i.split() for i in string.split('\n')]

def check_up(arr, i, j):
        k=j   
        while j - 1 >= 0 : 
            if int(arr[i][k]) <= int(arr[i][j-1]): #shorter or same size the not visible 
                    #print("HiidenFromUp!") 
                    
                    return False 
            j -= 1
        return True 

def check_down(arr, i, j):  
        k=j
        while j + 1 < len(arr[0]) : 
            if int(arr[i][k]) <= int(arr[i][j+1]): #shorter or same size the not visible

                return False 
            j += 1
        return True          
    
def check_right(arr, i, j):    
        k=i
        while i + 1 < len(arr) : 
            if int(arr[k][j]) <= int(arr[i+1][j]): #shorter or same size the not visible 
                #print(f" #i: {i} &i+1: {i+1}")
                return False 
            i += 1
        return True 

def check_left(arr, i, j): 
        k = i 
        while i - 1 >= 0 : 
            if int(arr[k][j]) <= int(arr[i-1][j]): #shorter or same size the not visible 
                return False 
            i -= 1
        return True   

def _check(arr, i , j) :
        if i == 0 or j == 0 or i == len(arr)-1 or j == len(arr[0]): 
            return 1 # the tree is on the edge
        elif  check_up(arr, i , j) or check_down(arr, i, j) or \
            check_right(arr, i, j) or check_left(arr, i, j) : 
            return 1 #its visible from some direction
        return 0 


####
# read the file Here

fd = open('input.txt', 'r' )
cnt = 0 
_arr = [] 

while True : 
    line = fd.readline().rstrip()
    
    if not line : 
        fd.close() 
        break 

    my_lst = list(line)
    _arr.append(my_lst)
    
    #print(f": #{cnt}--{line} ")
    cnt += 1


####


lst = []  

'''
_arr = [[3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0]]
'''

#operation
for  i in range (len(_arr)) : #rows
    for j in range(len(_arr[0])): #columns 
        
        result = (_check(_arr, i, j)) #add the number of visibles to list
        lst.append(result)
        #if result == 1 : 
            #print(f"i: {i}, j:{j}, val: {_arr[i][j]}, VISIBLE")
            
        #else : 
            #print(f"i: {i}, j:{j}, val: {_arr[i][j]}, HIDDEN")
    #print(f"_________________________________________")
print(f"Number of visible Trees: {sum(lst)}")