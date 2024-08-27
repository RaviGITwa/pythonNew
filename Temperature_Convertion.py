# Temperature_Convertion

temperature = float(input('Please enter the temperature : '))
unit = input('Celecius or Fahrenheit (C or F): ')

if unit == 'C':
    temperature = round((9*temperature/5 + 32,1))
    print(f'Temperature in Fahrenheit : {temperature} F')
if unit =='F':
    temperature = round((temperature-32)*5/9,1)
    print(f'Temperature in Celcius : {temperature} C')
else:
    print(f'{unit} is invalid')


