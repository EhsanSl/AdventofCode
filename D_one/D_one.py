from elf import Elf

#Openning the input file to read 
f = open('input.txt', 'r')

elfArr = [ ]
calArr = []

count = 1 

while True: 
    line = f.readline() 
     
    if (line == "\n"):
        print(f"elf #{count}")
        count += 1 #increment the counter to track each elf  
        
        elf = Elf(calArr)
        elfArr.append(elf)
        calArr.clear()    #clears the callory array to store new values 

    else : 
        print(line)
        calArr.append(line)
    #stops the look when there
    if not line:
        f.close()  
        break 

of = open('output.txt', 'w')
result = max(elfArr, key=lambda x: x.totalCal)
of.write("the Elf with the highest total_calory:{}".format(result.totalCal))

elfArr.sort(key=lambda x: x.totalCal)

elfArrSize = len(elfArr) 
top3_result = []
top3_totalCal = 0 
i = 0  

#since we want the last 3 
while i < 3 : 

    top3_result.append(elfArr[elfArrSize -1 -i])
    #temp = elfArr.pop(max(elfArr, key=lambda x: x.totalCal))
    #top3_result.append(temp)
    i += 1

of.write(f"\nthe top_3 Elfs with the highest total_calory: ")
j = 0 
while j < 3 : 
    if j == 2 : 
        of.write(f"{top3_result[j].totalCal}. ")
        top3_totalCal += top3_result[j].totalCal
    else : 
        of.write(f"{top3_result[j].totalCal}, ")
        top3_totalCal += top3_result[j].totalCal
    j +=1 

#top3_totalCal = sum(top3_result, key=lambda x: x.totalCal) #see if there is a way to use lamba to solve this
of.write(f"they are carrying the total of {top3_totalCal} calories! ^_^)/\(^_^ \n")

f.close 
