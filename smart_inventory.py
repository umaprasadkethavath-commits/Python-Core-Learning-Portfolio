#E-Commerce Inventory Lookup & Coupon Engine
unique_visitors={"salaar10","rebal10","bahubali10","darling10"}
user_id=input("enter your user id:")
cleaned_user_id=user_id.lower()
product_inventory={
    "laptop":{"price":45000,"stock":5},
    "phone":{"price":15000,"stock":0},
    "headphones":{"price":2500,"stock":12}
}
active_coupon={
    "FESTIVE500":500,
    "MEGA2000":2000
}

if cleaned_user_id in unique_visitors:
    print("Welcome back! Tracking active session.")
else:
    print("your user id is not available!")
    new_user_entry=input("enter your new user id to continue:")
    print("New user detected! Registration added to unique databse logs.")
    unique_visitors.add(new_user_entry)
product_to_buy=input("enter the product name:").strip().lower()
if product_to_buy in product_inventory:
    current_stock=product_inventory[product_to_buy]["stock"]
    base_price=product_inventory[product_to_buy]["price"]
    if current_stock>0:
        print("Product available! Base price $",base_price)
        coupon_code=input("enter your coupon code:").strip().upper()
        if coupon_code in active_coupon:
            discount=active_coupon[coupon_code]
            final_payable_amount=base_price-discount
            print("coupon applied suuccessfully! final payable amount $",final_payable_amount)
        else:
            print("Invalid coupon code. processing transaction at standard catlog rate:",base_price)
    else:
        print("Transaction Declined: Out of stock!")
else:
    print("Error: product not found in our catlog!")
    