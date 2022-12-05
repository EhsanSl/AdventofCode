#After the rearrangement procedure completes,
#what crate ends up on top of each stack?

#lst1 ,lst2 , lst3 , lst4, lst5 , lst6 ,lst7 , lst8 , lst9 = [] , , , 
#print(lst1.pop())

strs= ['DLVTMHF',  'HQGJCTNP', ' RSDMPH', 'LBVF', 'NHGLQ', 'WBDGRMP', 'GQMNRCHLQ' , 'CLW', 'RDLQJZMT'] 

n = 9
lists = [[] for _ in range(n)]
print(lists) 

for i in range(n): # i index for lists  
    #strs.append(strs[i]) #j index for strs 
    for j in strs[i] : 
        for k in j : # for each char in a str  
            lists[i].append(k)         

print(f"lists:{lists}")


# ta in marhale , hameye radifa az ham joda shodan , va to lists save shodan
#va har package ro mishe indexeshu moshakhas kard ke bad beshe 
# az source bere be destination 


# az inja bayad line haro az texfile bekhunim :

destination = 0 
#with open :
#read every line store i line  
f = open('input.txt', 'r')
while True : 
    line = f.readline().rstrip()
    print(f"line:{line}")
    if not line  :  
            f.close()
            break 
    #line = 'move 1 from 7 to 6'
    arr = []  

        # 3 entries, first selects the numbr of packages 
        # # 2nd & 3rd show the number of source and destination str in strs
        ###############
    arr = [int(num) for num in str.split(line) if num.isdigit()]
    #print(arr)
    number_of_packages = int(arr[0]) 
    source = int(arr[1]-1) 
    destination = int(arr[2]-1) 
    print(f"lists[source]:{lists[source]}")

    packages = [] 
    for i in range(number_of_packages): 
        #removed the package
        #print(source)
        print(lists[source][0])
        packages.append(lists[source][-1])
        print(f"packages: {packages}")
        lists[source] = lists[source][:-1] #updated the source column
        print(lists[source])
     
    print(lists[source])
    print("source UP , Destination Down")
    
    packages.reverse()
    for package in packages : 
        lists[destination].append(package)
    
    print(lists[destination])
    print(f"packages: {packages}")
    print(f"Destinatio: {lists[destination]} ")
    #ta in marhale mitoni ye package ro az ye list be ye liste dige bebarim 

    print("___")

#print at the end 
#print(lists[destination]) 
#print(lists[-1])
#print(lists[3])
for i in range(n) : 
     
    print( lists[i][-1],end=" ")


