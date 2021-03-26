'''num=int(input("Enter the number"))
for i in range(1,11):
    pro=num*i
    print(pro)
'''
def table():
    num=int(input("Enter the number"))
    for i in range(1,11):
        pro=num*i
        print(f'{num}*{i}=',pro)
table()