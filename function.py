# defining the function sum

def sum():
    # print("inside the function")
    num=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))
    ans=num+num2
    ans1=num-num2
    ans2=num*num2
    print(f"the sum of {num} and {num2} is {ans}")
    print(f"the sub of {num} and {num2} is {ans1}")
    print(f"the mul of {num} and {num2} is {ans2}")
    # print("function end")
# calling of the function
# print("calling the function")
sum()

def sub():
    # print("inside the function")
    num=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))
    ans1=num-num2
    print(f"the sub of {num} and {num2} is {ans1}")

sub()

def mul():
    # print("inside the function")
    num=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))
    ans2=num*num2
    print(f"the mul of {num} and {num2} is {ans2}")
mul()
# print("first sum call is over")
#print("second call")
sum()
sub()
mul()
print("program is over")