eno=input("enter employee number")
edesi=input("enter employee designation")
basic_salary=float(input("enter basic salary"))
if basic_salary>2000:
    hra=200
    da=45
    ta=12
    pf=150
    lic =250
    if basic_salary>5000:
     hra=500
    da=65
    ta=15
    pf=250
    lic =450
    if basic_salary>10000:
     hra=1000
    da=100
    ta=25
    pf=350
    lic =550
    if basic_salary>20000:
     hra=2000
    da=200
    ta=30
    pf=450
    lic =750
total_salary=basic_salary+hra+da+ta-pf-lic
print(eno)
print(edesi)
print(total_salary)
