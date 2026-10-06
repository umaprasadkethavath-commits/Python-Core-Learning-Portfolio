# Automated Teller Machine Banking Simulator
correct_pin =7788
account_balance =5000
a = int(input("enter your pin:"))
if a == 7788 :
    withdraw_amnt = int(input("enter the amount you want to withdraw:"))
    if withdraw_amnt <= account_balance:
        print("withdrawal successful! remaining balance:",account_balance-withdraw_amnt)
    else:
        print("insuffiecient balance")
else:
        print("incorect pin. card blocked!")