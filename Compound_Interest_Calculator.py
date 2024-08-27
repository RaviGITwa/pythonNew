# Compound Interest Calculator
principle = float(input('Please enter principle: '))
rate = float(input('Please enter rate: '))
time = int(input('Please enter time: '))

compund_interest = principle * pow((1+rate/100),time)
print(f'Compond interest Calculted is {compund_interest:.2f}')