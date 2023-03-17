sal=float(input('Enter the basic salary:'))
if(sal<=10000):
    hra=0.2*sal
    da=0.8*sal
    Salary=sal+hra+da
elif(sal<=20000):
    hra=0.25*sal
    da=0.9*sal
    Salary=hra+da+sal
else:
    hra=0.3*sal
    da=0.95*sal
    Salary=hra+da+sal
print('The gross salary is',Salary)
