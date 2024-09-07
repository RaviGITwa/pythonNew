'''
Python credit card validator program
1. Remove any '-' or ' '
2. Add all digits in the odd places from right to left
3. Double every second digit from right to left.
(If result is a two-digit number,
add the two-digit number together to get a single digit.)
4. Sum the totals of steps 2 & 3
5. If sum is divisible by 10, the credit card # is valid
'''

sum_odd_digit = 0
sum_even_digit =0
total = 0

#step 1
card_number = input("Enter a Credit card number: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

#step 2
for num in card_number[::2]:
    sum_odd_digit += int(num)

#step 3
for num in card_number[1::2]:
    num = int(num)*2
    if num >= 10:
        sum_even_digit += (1+(num%10))
    else:
        sum_even_digit += num
#step 4
total = sum_even_digit + sum_odd_digit

#step 5
if total%10 == 0:
    print("Valid Credit Card")
else:
    print("Invalid Credit Card")

