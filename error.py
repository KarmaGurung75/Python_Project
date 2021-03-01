'''d= input("how far did you travel today (in miles) ?")
t= input("How long did it take you (in hour)?")
s=d/t
print("your speed was "+s+ "miles per hour")
'''

#fixig above error
'''dString= input("how far did you travel today (in miles) ?")
tString= input("How long did it take you (in hour)?")
dFloat= float(dString)
tFloat= float(tString)
s=dFloat/tFloat
print("your speed was "+s+ "miles per hour")
'''
#final output without error
dString= input("how far did you travel today (in miles) ?")
tString= input("How long did it take you (in hour)?")
dFloat= float(dString)
tFloat= float(tString)
s=dFloat/tFloat
print("your speed was "+str(s) + "miles per hour")