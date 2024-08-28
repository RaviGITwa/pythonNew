# Shopping Cart

foods = []
prices = []
total = 0

while True:
 food = input('Please enter the food item(q to quit):')
 if food.lower() == 'q':
  break
 else:
  price =  float(input('Please enter the price: $'))
  foods.append(food)
  prices.append(price)

print("-----your cart-----")  
for food in foods:
 print(food)
for price in prices: 
 total += price
print(f'your total prices {total}')