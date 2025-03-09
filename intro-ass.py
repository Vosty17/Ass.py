def calculator()
# Get user input
num1=float(input("Enter the first number:"))  
num2=float(input("Enter the second number:"))
operation=input("Enter the operation (+,-,*,/)")
#Perform the choosen operation 
if operation =='+':
    result=num1+num2
elif operation=='-':
    result=num1-num2
elif operation=='*':
    result=num1*num2
elif operation=='/':
    result=num1/num2
else:
    result="Invalid operation"