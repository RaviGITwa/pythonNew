# Calculator
operators = input('Please Select an Operator (+ - * /):')
num1 = float(input('Please enter first number: '))
num2 = float(input('Please enter second number: '))

if operators == '+' :
    result = num1+num2
    print(round(result,3))
elif operators == '-' :
    result = num1-num2
    print(round(result,3))
elif operators == '*' :
    result = num1*num2
    print(round(result,3))
elif operators == '/' :

    result = num1/num2
    print(round(result,3))
else:
    print(f'{operators} selected is Invalid')
 