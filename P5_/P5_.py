strs= ['DLVTMHF',  'HQGJCTNP', ' RSDMPH', 'LBVF', 'NHGLQ', 'WBDGRMP', 'GQMNRCHLQ' , 'CLW', 'RDLQJZMT'] 
strs_lst =[]


n = 9
lists = [[] for _ in range(n)]
print(lists) 

for i in range(n): # i index for lists  
    #strs.append(strs[i]) #j index for strs 
    for j in strs[i] : 
        for k in j : # for each char in a str  
            lists[i].append(k)         
print(f"lists:{lists}")


destination = 0 
f = open('input.txt', 'r')
while True : 
    line = f.readline().rstrip()
    if not line  :  
            f.close()
            break 
    arr = []  
    arr = [int(num) for num in str.split(line) if num.isdigit()]
    number_of_packages = int(arr[0]) #first selects the numbr of packages 
    source = int(arr[1]-1) #show the index of source
    destination = int(arr[2]-1) # show the index of destination


    for _ in range(number_of_packages): 

        package = lists[source][-1]
        lists[source] = lists[source][:-1] #updated the source column
        lists[destination].append(package)
    print("___")

for i in range(n) :  
    print( lists[i][-1],end=" ")


