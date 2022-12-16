
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
    
    print(f": #{cnt}--{line} ")
    cnt += 1


            
#print(f": #my_LST : {my_lst} ")
print(f": #_arr: {_arr} ")

