
def check_arr(arr) -> bool : 
    flag = 0 
    flag = len(set(arr)) == len(arr)
    if (flag) : 
        return True
    return False


with open('input.txt') as f:
    string = f.readline().rstrip()

j,k,h = 0,0,0

for i in range(len(string) - 14):
    arr = [] 
    for j in range(i, i + 14):
        
        arr.append(string[j])
        print(f"j => {j}")
        #print(f"appending => {string[j]}")
    news = check_arr(arr)
    #print(f"news => {news}")
    if news == True :
        result = j + 1
        print(f"####result: = {result}") 
        break ; 


