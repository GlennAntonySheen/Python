import enchant 

d = enchant.Dict("en_US")   #initialising dictionary words
abc = [chr(x) for  x in range(ord('a'), ord('z')+1)]    #Asigning alphabet to abc
flag2 = 0
msg = input("Enter the Encoded Caesar Cipher message: ")   #Encoded msg

for i in range(52):
    decod = []
    for j in msg:   #Every letter in sentence        
        if abc.count(j) == 0:  #Doesnot increment for space finding by checking with alphabets
            decod.append(j)    
            continue
        decod.append(abc[ (abc.index(j) + int(i)) % 26 ])        
    decod = ''.join(decod)  #Converting char array to string
    
    decod = decod.split()   #Extracting words from sentecne
    for j in decod:
        flag = 1
        if (d.check(j) is False) and flag2 != 2:  #Checking words
            flag = 0
            break
    if flag == 1:   
        decod = ' '.join(decod)
        print(decod)
        if flag2 != 2:  flag2 = 1
        
    if i == 25:
        if flag2 == 1:  break
        elif flag2 == 0:
            if input("No Results Found :(\nDo you want to see all the possible results Y/N: ") == 'n':     break            
            else: 
                print("The possible results are:-")
                flag2 = 2
