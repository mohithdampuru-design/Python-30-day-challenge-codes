units=int(input("enter number of units"))
if units<=50:
      amount=units*2.5
      fare=250
elif units<=100:
         amount=units*3
         fare=300
elif units<=150:
       amount=units*3.5
       fare=350   
elif units<=250:
       amount=units*4
       fare=400
       total_amount=amount+fare
       print(total_amount)
           
      