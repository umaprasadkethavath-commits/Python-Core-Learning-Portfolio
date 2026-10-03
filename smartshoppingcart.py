items_in_stock=("apple","banana","milk","bread","goa","kiwi","orange")
cart=[]
items_to_buy=input("Enter your item:")
if items_to_buy in items_in_stock:
    cart.append(items_to_buy)
    print("you have buyed :",items_to_buy)
    if items_to_buy == "apple" :
        print("you have buyed apple your bill is 30 per piece!")
    elif items_to_buy == "banana" :
        print("you have buyed banana your bill is 70 per 12 piece!")
    elif items_to_buy == "milk" :
        print("you have buyed milk your bill is 50 per litre!")
    elif items_to_buy == "bread" :
        print("you have buyed bread your bill is 70 per packet!")
    elif items_to_buy == "goa" :
        print("you have buyed goa your bill is 70 per 5 piece!")
    elif items_to_buy == "kiwi" :
        print("you have buyed kiwi your bill is 70 per 2 piece!")
    else:
        print("you have buyed orange your bill is 70 per 4 piece!")    
else:
    print("the item is not availabe in store")