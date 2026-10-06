#Password Strength Evaluator
password_database=[]
password=input("Enter your password:")
a=password_database.append(password)
if len(password) >=8 and  not password.endswith(" "):
    print("Password successfully registered and saved!")
    print("Recheck your password saving in database,your password is:",password)
else:
    print("Weak password ! It must be at least 8 characters long and cannot end with a space.")
print("All saved passwords in Database:",password_database)