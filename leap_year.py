i=int(input("Enter a year:"))
if i%4==0:
  print("leap year")
elif i%400==0:
  print("leap year")
else:
  print("non leap year")