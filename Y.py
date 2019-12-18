s = ''
a = 0
t = int(input('Enter a number: '))
for i in range(t, 0, -1):
    for j in range(0, a):
        s = s + ' '
    s = s + '*'
    for j in range(0, i*2+1):
        s = s + ' '
    s = s + '*'
    print(s)
    s = ''
    a+=1
for i in range(0, t):
    for j in range(0, a):
        s = s + ' '
    print(s, '*'  )
    s = ''