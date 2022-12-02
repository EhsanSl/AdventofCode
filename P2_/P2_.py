

def win__( my_hand ) -> int:

    if (my_hand == 'rock'):return  1 + 6 
    if (my_hand == 'paper'):return  2 + 6 
    if (my_hand == 'scissor'):return  3 + 6

def draw__(my_hand ) -> int:

    if (my_hand == 'rock'):return  1 + 3
    if (my_hand == 'paper'):return  2 + 3 
        #print(f'my hand type : {type(my_hand)}')
    if (my_hand == 'scissor'):return  3 + 3

def loose__(my_hand ) -> int:

    if (my_hand == 'rock'):return  1
    if (my_hand == 'paper'):return  2
    if (my_hand == 'scissor'):return  3


if __name__ == '__main__': 

    
    OP_RULEBOOK = {
        'A' : 'rock',
        'B' : 'paper',
        'C' : 'scissor'
    }
    MY_RULEBOOK = { 
        'X' : 'rock',
        'Y' : 'paper',
        'Z' : 'scissor' 
    }

    fd = open( 'input.txt', 'r')
    score = 0  
    line_count = 0
    while True :
        
        
        line = fd.readline() 
        line_count += 1
        if line == "\n" or line == "" or line == " " : 
            break 
        print(f"####line_counter : {line_count}")

        arr = [] 
        arr = line.split() 
        #print(f'array : {arr}')
        
        op_choice = arr[0]
        my_choice = arr[1]

        if op_choice == 'A' : 
            if my_choice == 'X' : 
                score += draw__(MY_RULEBOOK[my_choice])
                
            if my_choice == 'Y' : 
                score += win__(MY_RULEBOOK[my_choice])

            if my_choice == 'Z' : 
                score += loose__(MY_RULEBOOK[my_choice])

        if op_choice == 'B' : 
            if my_choice == 'X' : 
                score += loose__( MY_RULEBOOK[my_choice])
                
            if my_choice == 'Y' : 
                score += draw__( MY_RULEBOOK[my_choice])

            if my_choice == 'Z' : 
                score += win__( MY_RULEBOOK[my_choice])
        
        if op_choice == 'C' : 
            if my_choice == 'X' : 
                score += win__( MY_RULEBOOK[my_choice])
                
            if my_choice == 'Y' : 
                score += loose__( MY_RULEBOOK[my_choice])

            if my_choice == 'Z' : 
                score += draw__( MY_RULEBOOK[my_choice])
        
        

    print(f'##The Final Score: {score}##')
    
    fd.close() 


