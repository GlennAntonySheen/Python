
n=int(input('Enter number of Fibinocci series: '))

if n<2:
    if n==1:
        print('0')
    else:
        print('Enter a number greater then 0')
else:
    a, b, = 0, 1
    print('0\n1')
    for i in range(2, n):
        c = a + b
        a, b = b, c        
        print(c)
