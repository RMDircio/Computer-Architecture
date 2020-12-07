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