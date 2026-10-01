sno=input("enter student name")
rollno=int(input("enter student roll no"))
s1=float(input("enter s1 marks"))
s2=float(input("enter s2 marks"))
s3=float(input("enter s3 marks"))
avg_marks=s1+s2+s3/3
print("student name:\n",sno)       
print("roll number:\n",rollno)    
print("average marks :\n",avg_marks)      

if avg_marks>75:
 result= print( "distinction")
elif avg_marks>50 and avg_marks<75:
 result= print("first class")
elif avg_marks<50 and avg_marks>40:
 print("second class")
elif avg_marks<40 and avg_marks>35:
   result=print("third class")
elif avg_marks<35:
        result= print("fail")
        print(result)
