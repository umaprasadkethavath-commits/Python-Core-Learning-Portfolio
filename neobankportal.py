#Neo-Banking Multi-Stage Authentication Gateway
user_name=input("Enter Your Full Name :")
user_aadhaar=(input("Enter Aadhaar number:"))
cleaned_name=user_name.strip()
cleaned_name_length=len(cleaned_name)
user_lowercase=cleaned_name.upper()
unique_code="999"
prefix_3_char=user_name[:3]
account_prefix=prefix_3_char+unique_code
user_aadhaar_end_4=user_aadhaar[-4:]
number_of_x=len(user_aadhaar)-4
aadhaar_verified=(number_of_x*"x")+user_aadhaar_end_4
blocked_aacouts=["sri999","ind999","uma999","yas999","mad999","raj999","sid999"]
bank_balance=10000
fee_charged=200
transfer_amount=int(input("Enter the Amount You want to transfer:" ))
if account_prefix  not in blocked_aacouts:
    print("Wait for a second checking account balance!")
    print("Transaction is underway!")
    if transfer_amount<=bank_balance:
        print("Transaction is Processing!")
        if transfer_amount>=5000:
            remaining_balance=bank_balance-transfer_amount-fee_charged
            print("Your Charges for Transaction is $200, as your Transaction is above $5000.")
        else:
            remaining_balance=bank_balance-transfer_amount
            print("Transfer Successfully Done!")
    else:
        print("Transaction Declined Due to Insufficient Funds!")
else:
    remaining_balance=bank_balance
    print("Security Alert : Account Blocked due to Fraud!")
frozen_account_statement=(user_lowercase,account_prefix,aadhaar_verified,remaining_balance)
print("YOUR ACCOUNT DETAILS AND BALANCE AFTER TRANSACTION is in the Format 'Name','Accountname',Aadhaar,'Balance':",frozen_account_statement)