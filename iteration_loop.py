'''for i in "abc":
    print("softwarica")
    print("dillibazar")
    print("IT-college")

for i in (1,2,3,4):
    print(i) '''
'''for karma in range(4):
    print(karma)
for i in range(4):
    print("softwarica")
    print("dillibazar")
'''
''''#wap to print number from 1-10
for i in range(11):
    print(i)

for i in range(10,-1):
    print(i)

#wap print even number from 1-50
for i in range(0,50,2):
    print(i)
'''
#wap to print a even from 1-50. check each number weather it is even or not?
'''for i in range(50):
    print(i)
    if i%2==0:
        print(i,"is the even number")
        
'''
#for-else loop
'''for i in range(4):
    print(i)
else:
    print("program is over")
'''

#continue
'''for i in range(4):
    if i==2:
        continue
    print(i)
#break
for i in range(4):
     if i==2:
         break
      print(i)

for val in "string":
    if val =="i":
        break
    print(val)
print('End')

fruits=["apple",'banana',"cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break

fruits=["apple",'banana',"cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)

#while loop
i=0             # initialization
while i<=10:    # condition
    print(i)
    i=i+1       # stepping
print("Program is over")

i=10             # initialization
while i>=1:    # condition
    print(i)
    i=i-1       # stepping
print("Program is over")
'''
#wap to print all the odd and even number appropate messsage from 1-50
'''i=0
while i<=50:
    if i%2==0:
        print(i," is even number")
    else:
        print(i," is odd number")
    i=i + 1
'''
#wap to find the sum of element of list using for loop
lst=[10,31,37,40,56,63,70]
sum=0
'''for i in lst:
    sum=sum+i
print(sum)
'''
for i in range(7):
    sum=sum+lst[i]
print("the sum is ",sum)

#wap to find the sum of the element of list using while loop
