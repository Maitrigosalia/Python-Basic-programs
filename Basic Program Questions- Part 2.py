#Basic Program Questions- PART 2

def Q1():
    import math
    r=eval(input("Enter the radius of circle = "))
    area= math.pi * r * r
    print("Area of Circle = ",area)
    cir=2 * math.pi* r
    print("Circumferance of Circle =",cir)
Q1()

def Q2():
    t=eval(input("Enter Centigrade temperature = "))
    c= (t-32) * 5/9
    print("Temperature converted from Fahrenheie to centigrade is =",c)
Q2()

def Q3():
    n1=eval(input("Enter 1st no ="))
    n2=eval(input("Enter 2nd no ="))
    a= n1 + n2
    print("Addition of 2 numbers= ",a)
    s= n1-n2
    print("Substraction of 2 numbers= ",s)
    m= n1 * n2
    print("Multiplication of 2 numbers= ",m)
    d= n1/n2
    print("Division of 2 numbers= ",d)
Q3()

def Q4():
    l=eval(input("Enter length in centimeter ="))
    m= l/100
    print("Centimer to meter =",m)
    k= 1/100000
    print("Centimeter to kilomter=",k)
Q4()

def Q5():
    n1= eval (input ("Enter n1 : "))
    n2= eval (input ("Enter n2 : "))
    n3= eval (input ("Enter n3 : "))
    n4= eval (input ("Enter n4 : "))
    n5= eval (input ("Enter n5 : "))
    t= n1+n2+n3+n4+n5
    print("Total Marks = ",t)
    a= t/5
    print("Average Marks = ",a)
    p=t/500*100
    print("Marks in Precentage= ",p)
Q5()

def Q6():
    p=eval(input("Enter Principle amount:"))
    t=eval(input("Enter time in years:"))
    r=eval(input("Enter rate:"))
    s= p*t*r/100
    print("Simple Interest=",s)
Q6()

def Q7():
    import math
    LC= eval (input ("Enter Inductance (LC)="))
    R= eval (input ("Enter Resistance (R) ="))
    C= eval (input ("Enter C ="))
    ans= math.sqrt((1/LC)-(R*R)/(4*C*C))
    print ("Damped Natural Frequency = ", ans)
Q7()

def Q8():
    m1= eval (input ("Enter m1 ="))
    m2= eval (input ("Enter m2 ="))
    g= eval (input ("Enter g ="))
    ans= (2*m1*m2)*g/(m1+m2)
    print("Torque Formula Answer= ",ans)
Q8()

def Q9():
    b=eval(input("Enter basic Salary ="))
    da= b*0.1
    print("Dearness Allowance =",da)
    Hra= b * 0.75
    print("House Rent Allowance =",Hra)
    ma=300
    pf= b % 0.125
    print("Provident Fund =",pf)
    Gross= b + da + Hra + ma
    print("Gross amount= ",Gross)
    nt= Gross- pf
    print("Net =",nt)
    print("Thank you")
Q9()

def Q10():
    import math
    dr=eval(input("Enter demand rate ="))
    sc=eval(input("Enter setup cost ="))
    hc=eval(input("Enter holding cost ="))
    EOQ = math.sqrt((2*dr*sc)/hc)
    print("EOQ =",EOQ)
    TBO= math.sqrt((2*sc)/(dr*hc))
    print("TBO =",TBO)
Q10()

def Q11():
    d=eval(input("Enter no of days ="))
    y= d/365
    print("Days in Years =",y)
    w= d/7
    print("Days in Weeks =",w)
Q11()

def Q12():
    import math
    s=eval(input("Enter side of the triangle ="))
    a= math.sqrt((3)/4)*s*s
    print("Area of an equilateral triangle",a)
Q12()
