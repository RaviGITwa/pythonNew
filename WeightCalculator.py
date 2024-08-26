# Weight Calculator

weight = float(input('Please enter your weight: '))
unit = input('Kilogram or Pound? (K or P): ')

if unit == 'K':
    weight = weight * 2.205
    print(f'Your weight in pound is {weight}')
elif unit == 'P':
    weight = weight/2.205
    print(f'Your weight in Kilogram is {weight}')
else:
    print('Invalid weight')
    print('Invalid unit')
