user_name=input("Enter your full name before proceeding to book your ticket:")
birth_year=int(input("Enter your birth year:"))
age_of_customer=2026-birth_year
ticket_price=5000
stripped=user_name.strip()
formatted_user_name=stripped.upper()
prefix_3_char=formatted_user_name[:3]
alpha_numeric_code=input("Enter your alpha numeric code:")
end_3_char=alpha_numeric_code[-3:]

if end_3_char == "IND":
    print("your ticket price to the india is :$5000")
    loyalty_database=[101,202,303]
    premium_loyalty_id=int(input("Enter your premium loyalty id:"))
    print("Your age is :",age_of_customer)
    if age_of_customer>=60  and (premium_loyalty_id in loyalty_database):
        f_ticket_price=ticket_price-2000
        print("YOu have got massive discount of $2000 from your ticket! $",f_ticket_price)
    elif age_of_customer >=18 and age_of_customer<=59 and (premium_loyalty_id in loyalty_database):
        f_ticket_price=ticket_price-1500
        print("Your are now elgible for premium discount! $",f_ticket_price)
    elif age_of_customer<=60 or (premium_loyalty_id  in loyalty_database):
        f_ticket_price=ticket_price-1000
        print("You have elgible for $1000 discount from your ticket! $ ",f_ticket_price)
    else:
        print("Standard pricing applied! price is : $",ticket_price)
else:
    f_ticket_price=15000
    print("Your ticket price is : $15000")
final_boarding_pass=(formatted_user_name,prefix_3_char,age_of_customer,f_ticket_price)
print("your boarding pass details are :",final_boarding_pass)