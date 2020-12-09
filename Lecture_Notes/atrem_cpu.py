'''         Atrem's Lecture CSPT8      
        https://youtu.be/9Pyi64vlqgQ

                BASIC NUMBER BASES
'''


'''
               -------     DECIMAL      ------
                        
BASE 10 system 0-9

        1 2 3 4     =    1234 Decimal
        -------
        10th place  
        10^3  | 10^2  | 10^1 | 10^0
       1*1000 | 2*100 | 3*10 |  4*1 

       Another way to view this is
       (1 * 10^3) + (2 * 10^2) + (3 * 10^1) + (4 * 10^0)  = 1234



                -------     BINARY      ------

BASE 2 System 0-1

        14 Decimal --> Binary

                        
                   _1_  _1_  _1_  _0_
                   2^3  2^2  2^1  2^0
                   =8   =4   =2   =1

                Another way to view this is
                (1 * 2^3) + (1 * 2^2) + (1 * 2^1) + (0 * 2^0)  = 1110


        10101 Binary --> Decimal

                   _1_  _0_  _1_  _0_  _1_
                   2^4  2^3  2^2  2^1  2^0
                   =16  =8   =4   =2   =1

                Another way to view this is
                (1 * 2^4) + (0 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0)  = 16+4+1 = 21 Decimal
'''

# Conversions in Python

num = 21
print('This is our original number:' , num)

# set to integer with BASE 10 (Decimal)
print('Number as Base 10 Decimal:', int(num))

# set to BASE 2 Binary
print('Number as Base 3 Binary:', bin(num))

# set to BASE 16 Hexadecimal
print('Number as Base 16 Hexadecimal:', hex(num))


'''
                 -------     CODING A CPU      ------
'''

# what we want to happen:
        # if the computer is on, 
        # read from memory
        # do something

import sys

# Operation Codes (OP Codes)
# first task
PRINT_HELLO_WORD        = 1 # 0b00000001
# stop the program
HALT                    = 2 # 0b00000010
# second task
PRINT_NUM               = 3 # 0b00000011
# save register
SAVE_REG                = 4
# print register
PRINT_REG               = 5
# add numbers together
ADD                     = 6


# hard code a program                                   Command Numbers
# adds two numbers together
memory = [
        PRINT_HELLO_WORD,                               # 1
        PRINT_NUM, # this will print what follows       # 3
        5, # number 5 will be printed                   # value 5
        PRINT_NUM, # this will print what follows       # 3
        0, # number 0 will be printed                   # value 0
        PRINT_NUM, # this will print what follows       # 3
        5, # number 5 will be printed                   # value 5
        SAVE_REG,                                       # 4
        1,                                              # value 1
        1,                                              # register index 1
        SAVE_REG,                                       # 4
        2,                                              # value 2
        2,                                              # register index 2
        PRINT_REG,                                      # 5
        2,                                              # register index 2
        ADD,                                            # 6
        1,                                              # register index 1
        2,                                              # register index 2
        PRINT_REG,                                      # 5
        1,                                              # register index 1
        HALT, # must be last step                       # 2
        
]

# registers are special working space (e.i. hands) that get memory
registers = [0] * 8 # eight bits or 8 hands :)


# switch for computer (ON or OFF)
running = True

# how to iterate through memory --> Program Counter
p_counter = 0

# while computer is ON (True)
while running:
        # read line by line from memory
        # set the instruction to be the current place in memory
        instruction = memory[p_counter] 

        # first task
        if instruction == PRINT_HELLO_WORD:
                # print Hello World
                print('Hello World')
                # move the PC counter up 1
                p_counter += 1

        # third task
        elif instruction == PRINT_NUM:
                # print the number in the next memory slot
                # grab the PC counter in memory, then add 1 to get to #5 slot
                num = memory[p_counter + 1]
                # then print the number
                print(num)
                # move the counter TWO steps
                p_counter += 2

        # fourth task
        elif instruction == SAVE_REG:
                # save some value to a register
                # take two params - value to store and which register
                num = memory[p_counter +1] # one step after the SAVE_REG instruction
                reg_location = memory[p_counter + 2] # two steps after the SAVE_REG instruction

                # store the value in temporary memory
                registers[reg_location] = num

                # advance the program counter THREE steps
                p_counter += 3

        # fifth task
        elif instruction == PRINT_REG:
                # get the memory location and the next value
                reg_location = memory[p_counter +1]
                # print what is in that location
                print(registers[reg_location])
                # advance the program counter
                p_counter += 2
        
        # sixth task
        elif instruction == ADD:
                # take TWO registers, add their value
                # store the result in the first register
                
                # get register 1
                reg_1 = memory[p_counter + 1]
                # get register 2
                reg_2 = memory[p_counter + 2]
                
                # add their values
                # store new sum in register 1
                registers[reg_1] += registers[reg_2]

                # advance the program counter
                p_counter += 3
                

        
        # need a way to end the program and avoid crashing
        elif instruction == HALT:
                # set running to OFF
                running = False
                # move counter up
                p_counter += 1 # this counter is optional - really doesn't matter

        # handle a error: unknown instruction
        else:
                print('Unknown Instruction:', instruction)
                # end without crashing
                sys.exit(1)











