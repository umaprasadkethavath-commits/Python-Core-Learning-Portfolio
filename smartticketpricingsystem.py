name=input("Enter your name :")
age=int(input("Enter your age: "))
movie_name=input("Enter movie name your intreseted to watch:")
ticket=0.0
if age<=12:
    ticket="$7.00"
    print("you are child below 12 years or 12, your ticket price is:",ticket)
elif age>=13 and age<=64:
    ticket="$12.0"
    print("your standard ticket price is:",ticket)
else:
    ticket="$9.0"
    print("you are an senior citizen you got a discount of $3, your ticket price is:",ticket)

if len(movie_name)>=3:
    print("Error : Invalid movie Title!")
else:
    print("you have entered valid movie title")
receipt_code=name[-3:]+movie_name[:2]+str(ticket)
print("your movie receipt code is:",receipt_code)