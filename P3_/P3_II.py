import numpy as np
import string

def calc__(badge_array, final_array) : 
    # need two dictionaries then we need to fill them up with 1 loop for each and then assign their values 
    #then we just call the element from the argument and find they value in the dicts , and return it 
    lowercase_dict = { }

    uppercase_dict = { }

    lowercase_alph = list(string.ascii_lowercase) # created a list of all lower case alphaber
    #print(lowercase_alph)
    uppercase_alph = list(string.ascii_uppercase) # created a list of all uppr case alphaber
    #print(uppercase_alph)

    #building the dict for lowecase letters 
    for i in range (0, len(lowercase_alph)) :
        lowercase_dict.update({lowercase_alph[i] : i+1})

    #building the dict with upeprcase letters 
    index = 0 
    for i in range (len(uppercase_alph), 52) :
        uppercase_dict.update({uppercase_alph[index] : i+1})
        index += 1
    #print("      ______________________________         ")
    #print(lowercase_dict)
    #print("      ______________________________         ")
    #print(uppercase_dict)
    #print (f"lst[0]: {lst[0]}")
    #print(f"lst :{lst}")
    for i in badge_array : 
        if i in lowercase_dict: 
            final_array.append(lowercase_dict[i])
        elif  i in uppercase_dict:
            final_array.append(uppercase_dict[i])
    return None 


if __name__ == '__main__': 

    #str = 'afbcda'
    badge_array = [] 
    final_array = [] 
    fd = open('input.txt','r')
    switch = 0
    while True : 
 
        str1 = fd.readline().rstrip()
        if not str1 : 
            fd.close() 
            break
        str2 = fd.readline().rstrip()
        str3 = fd.readline().rstrip()

        #print strings 
        print(f"str1: {str1}")
        print(f"str2: {str2}")
        print(f"str3: {str3}")

        #splitting each string into a list
        str1_arr = list(str1)
        str2_arr = list(str2)
        str3_arr = list(str3)

        #defining them as np array
        str1_arr = np.array(str1_arr)
        str2_arr = np.array(str2_arr)
        str3_arr = np.array(str3_arr)
        print(f"str1_arr: {str1_arr}")

        intermed = np.intersect1d(str1_arr,str2_arr)
        print(f"intermed: {intermed}")
        final = (np.intersect1d(intermed,str3_arr)) 
        final = final.tolist() #conver it back to normal list 
        print(f"final: {final}")

        badge_array.append(final[0])

        #badge_array.append(np.intersect1d(intermed,str3_arr)) 

        '''
        if len(result) : 
            
        '''
        
        #print(f"final_array: {final_array}")
        #print(f"_______________________________________") 

    calc_result = calc__(badge_array,final_array) # return the number associated with the found character 
        

    print(f"calc_result:  {calc_result}")
    print(f"_______________________________________") 
    print(f"badge_array: {badge_array}")
    print(f"_______________________________________") 
    print(f"final_array: {final_array}")
    print(f"_______________________________________") 
    print(f"final_array_sum: {sum(final_array)}")
    print("")   
           
    #print(f"sum of all strings: {sum(final_array)}")     
    print(f"_______________________________________")   
    
    fd.close() 

    