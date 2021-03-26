# n!=n*(n-1)*n......n
num=int(input("Enter the number"))
product=1
for i in range(1,num+1):
    product=product*i
print(product,"is the fractroral of the given number")

lst=[1,2,3,4,5]
product=1
for i in lst:
    product=product*i
print(product)
