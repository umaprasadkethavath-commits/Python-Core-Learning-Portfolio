 # Project Title : Dynamic student Grade Evaluation Engine
a=float(input("enter your marks you scored in math:"))
b=float(input("enter your marks you scored in science:"))
c=float(input("enter your marks you scored in english:"))
avg_score=((a+b+c)/300)*100
if avg_score>=90:
    print("excellent! you have got an A grade")
elif avg_score<=40:
     print("you need to work harder")
else:
    print("good job! you passed")
