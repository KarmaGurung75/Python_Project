#print("softwarica\n"*10)

#str='softwarica'
"""#lst=['30,4']
tup=['apple,orange']
"""
'''str='karma'
for i in str:
    print('softwarica')

for karma in [1,2,3,4,5,'karma',6]:
    print(karma)'''

'''nested for loop'''
'''for i in range(3):
    for j in range(3):
        print("*",'\t',end='')
    print()'''

'''for i in range(6):
    for j in range(i+1):
        print(j,"\t",end='')
    print()
'''
'''for i in range(5):
    for j in range(i+1):
        print('a',end='')
        a=a+1:
    print()
    '''
'''for i in range(11):
    for j in range(11):
        print(j,'*',i,'=',(i*j),end='\t')

    print()'''

'''else loop'''
for i in range(5):
    print(i)
else:
    print('loop is over')

'''break statement'''
for i in range(5):
    if i==3:
        break
    print(i)
else:
    print('loop is over')

print()

'''continue statement'''
for i in range(5):
    if i==3:
        continue
    print(i)
else:
    print('loop is over\n')

'''while statement'''
i=1#start
while i<=10:#stop
    print(i)
    i=i+1 #increment

