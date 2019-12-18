import math, os
while True:
    os.system('cls')
    str = input("Enter the expression: ")
    m=math
    #str = ' 3'
#-----------------------------------------------------------------------
    str = str.replace(" ", "")             #Eliminating ' ' (space) char
    
#-----------------------------------------------------------------------    
    print('ans = ',eval(str))
    input()
#----------Restart the program-------------------------------------------
    choice = input('Do you wish to continue (Y / N): ')
    if choice == 'n' or choice == 'N':
        break