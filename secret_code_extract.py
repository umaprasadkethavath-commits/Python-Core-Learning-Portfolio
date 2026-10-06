tracking_code = input("enter your trackig code:")
code = tracking_code[-4:]
print(code)
if code =="CONF" :
    print("access approved: confirmed order!")
else:
    print("access denied: invalid code variant!")