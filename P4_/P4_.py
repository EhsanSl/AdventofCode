
if __name__ == '__main__': 

    #reads and stores in a list as strings
    fd = open('input.txt','r')
    counter = 0 #final result ( the number of sets that are completely in their paired set) 


    while True : 
        #now reads each string , seperate the numbers
        lst = fd.readline().rsplit()
        if not lst : 
            fd.close() 
            break 
        
        
        print (lst)
        print(" _________________________________________") 
        
        
        new_lst =[]
        for k in lst :    
            new_lst.append(k.split(','))
        print(new_lst)
        print("           _________________________________________") 
        
        #then we have to create a set for  each number \
        final_lst =[] 

        for i in new_lst:  
            for j in i : 
                final_lst.append(j.split('-'))  
        print(final_lst)
        print(" _________________________________________ ") 

        a =[] 
        b =[]
        '''
        print(final_lst[0])
        print(final_lst[1])
        print(final_lst[0][0])
        print(final_lst[0][1])
        print(final_lst[1][0])
        print(final_lst[1][1])
        '''
        for i in range (int(final_lst[0][0]),int(final_lst[0][1])+1): 
            a.append(i)
        for i in range (int(final_lst[1][0]),int(final_lst[1][1])+1): 
            b.append(i)

        print(f"a: {a}")
        print(f"b: {b}")
        print(" _________________________________________ ") 
        if set(a).issubset(b) : 
            counter +=1
        elif set(b).issubset(a) : 
            counter +=1
        

        

    print(" _________________________________________ ") 
    print(f"counter: {counter}")


    








    










    

    
