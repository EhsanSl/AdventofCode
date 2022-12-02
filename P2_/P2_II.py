## tHIS WAS THE SCENARIO WHERE THE ELF CAME BACK AND TOLD US TO READ THE SECOND COLUMN AS THE SUGGESTED RESULT OF THOSE ROUNDS

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
    ELF_RULEBOOK = { 
        'X' : 'loose',
        'Y' : 'draw',
        'Z' : 'win' 
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
        result = arr[1]

        if op_choice == 'A' : #MEANS HE HAS ROCK
            if result == 'X' : #I HAVE TO LOOSE
                score += loose__(OP_RULEBOOK['C'])
                
            if result == 'Y' : #IHAVE TO DRAW
                score += draw__(OP_RULEBOOK[op_choice])

            if result == 'Z' : #I HAVE TO WIN
                score += win__(OP_RULEBOOK['B'])

        if op_choice == 'B' : #MEANS HE HAS PAPER
            if result == 'X' : #I HAVE TO LOOSE
                score += loose__(OP_RULEBOOK['A'])
                
            if result == 'Y' : #IHAVE TO DRAW
                score += draw__(OP_RULEBOOK[op_choice])

            if result == 'Z' : #I HAVE TO WIN
                score += win__(OP_RULEBOOK['C'])
        
        if op_choice == 'C' : #MEANS HE HAS Scissor
            if result == 'X' : #I HAVE TO LOOSE
                score += loose__(OP_RULEBOOK['B'])
                
            if result == 'Y' : #IHAVE TO DRAW
                score += draw__(OP_RULEBOOK[op_choice])

            if result == 'Z' : #I HAVE TO WIN
                score += win__(OP_RULEBOOK['A'])   

    print(f'##The Final Score : {score}##')
    
    fd.close() 


