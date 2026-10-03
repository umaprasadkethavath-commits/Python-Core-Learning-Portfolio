has_badge =input("do you have an access badge? (yes/no):")
if has_badge == "yes":
    print("door 1 opened! scaning your badge code...")
    badge_code =int(input("enter your 4 digit badge code:"))
    if badge_code == 7788:
        print("door 2 opened! access granted.welcome inside!")
    else:
        print("door 2 locked! invalid badge code.access denied!")
else:
    print("access denied you can not enter without badge.")