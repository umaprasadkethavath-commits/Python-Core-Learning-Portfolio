password=input("enter your password:")
masked_password="*"*len(password)
if len(password)>=8 and len(password)<=12:
    print("your masked password is:",masked_password)
else:
    print("invalid! password should be more than 8 digits and less then 12 digits.")