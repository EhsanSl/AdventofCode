import numpy as np
import string

def find__(str) :

    str_arr =  list(str)#string_list
    center = int(len(str)/2)
    first_half = []
    second_half = []
    
    print(f"str_array: {str_arr}")
    print(f"center: {center}")
    print("                      ____")


    for i in range(0, len(str_arr))  :
        
        if i < len(str_arr)/2 : #it was in the first half 
            first_half.append(str_arr[i])
        else : 
            second_half.append(str_arr[i])

    #decalring them as numpy arary
    first_half = np.array(first_half)
    second_half = np.array(second_half)

    print(f"first_half : {first_half}")
    print (f'second_half: {second_half}')
    print("")
    
    # Common values between two arrays
    #print(np.intersect1d(first_half, second_half))
    return np.intersect1d(first_half, second_half)

def calc__(lst) : 
    # need two dictionaries then we need to fill them up with 1 loop for each and then assign their values 
    #then we just call the element from the argument and find they value in the dicts , and return it 
    lowercase_dict = { }

    uppercase_dict = { }

    lowercase_alph = list(string.ascii_lowercase) # created a list of all lower case alphaber
    #print(lowercase_alph)
    uppercase_alph = list(string.ascii_uppercase) # created a list of all uppr case alphaber
    #print(uppercase_alph)

    for i in range (0, len(lowercase_alph)) :
        lowercase_dict.update({lowercase_alph[i] : i+1})

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
    if lst[0] in lowercase_dict: 
        return lowercase_dict[lst[0]]
    elif  lst[0] in uppercase_dict:
        return uppercase_dict[lst[0]]
    
if __name__ == '__main__': 

    #str = 'afbcda'
    final_array = [] 
    fd = open('input.txt','r')
    
    while True : 
        
        str = fd.readline().rstrip()
        
        if not str : 
            fd.close() 
            break 
        #print(f"str: {str}")

        '''
        some_thing = "qrlZCwlqZrqqpWdlRqCRqdqcVNsVMzQzmNgNPBsRhVQVVzMs"
        sth_len = len("qrlZCwlqZrqqpWdlRqCRqdqcVNsVMzQzmNgNPBsRhVQVVzMs")
        half_sth_len = sth_len/2 
        print(f"sth_len: {sth_len}") 
        print(f"half_sth_len: {half_sth_len}") 
        '''

        result = find__(str) # return the mutual character from the first & second half 
        
        print(f"result: {result}") 
        print(f"final_array: {final_array}")
        print("")

        if len(result) : 
            calc_result = calc__(result) # return the number associated with the found character 
            final_array.append(calc_result)
    
            print(f"calc_result:  {calc_result}")
            print(f"_______________________________________") 
            

           
    print(f"sum of all strings: {sum(final_array)}")     
    print(f"_______________________________________")   
    
    fd.close() 

    


    #TzhhdJTqJzcBdJJnzjtQrLdj wgLtpbgrLQ