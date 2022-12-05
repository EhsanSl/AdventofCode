strs= ['DLVTMHF',  'HQGJCTNP', ' RSDMPH', 'LBVF', 'NHGLQ', 'WBDGRMP', 'GQMNRCHLQ' , 'CLW', 'RDLQJZMT'] 

n = 9
lists = [[] for _ in range(n)]
print(lists) 

for i in range(n): # i index for lists   
    for j in strs[i] : 
        for k in j : # for each char in a str  
            lists[i].append(k)         

print(f"lists:{lists}")

destination = 0  
f = open('input.txt', 'r')
while True : 
    line = f.readline().rstrip()
    print(f"line:{line}")
    if not line  :  
            f.close()
            break 
    #line = 'move 1 from 7 to 6'
    arr = []  
    arr = [int(num) for num in str.split(line) if num.isdigit()]

    number_of_packages = int(arr[0]) #first selects the numbr of packages
    source = int(arr[1]-1) #2nd shows the number of source
    destination = int(arr[2]-1)  #3rd shows the number of destination 
    print(f"lists[source]:{lists[source]}")

    packages = [] 
    for i in range(number_of_packages): 
        #removed the package
        print(f"counter:{i}")
        packages.append(lists[source][-1])
        lists[source] = lists[source][:-1] #updated the source column
        print(lists[source])
     
    packages.reverse()
    print(f"packages: {packages}")
    for package in packages : 
        lists[destination].append(package)
    
    print(f"Destinatio: {lists[destination]} ")
    print("___")


for i in range(n) : 
     
    print( lists[i][-1],end=" ")


