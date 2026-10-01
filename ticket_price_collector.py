age=int(input("enter your age"))
fare=int(input("enter fare"))
if age<5:
      total_cost=50
if age<=10:
      total_cost=75
elif age<=20:
       total_cost=100
elif age<=25:
   total_cost=250
elif  age<=75:
    total_cost=500
final_price=fare+total_cost
print(final_price)


