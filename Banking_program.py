'''
banking program 
1. Show Balance
2. Deposit
3. Withdraw
'''

def show_balance(balance):
    print("*********************")
    print(f'The Balance is ${balance : .2f}')
    print("*********************")

def deposit():
    print("*********************")
    amount = float(input("Enter a amount to be deposited : "))
    print("*********************")
    if amount <0:
        print("*********************")
        print("thats not a Valid deposit")
        print("*********************")
        return 0
    else:
        return amount
    
def withdraw(balance):
    print("*********************")
    amount = float(input("Please enter te amount to withdraw: "))
    print("*********************")
    if amount > balance:
        print("*********************")
        print("Insufficient balance")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    else: 
        return amount    
    
def main():
    balance =0
    is_running =True

    while is_running:
        print("*********************")
        print("   Banking program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")

        print("*********************")
        choice = input('Please select a choice from (1-4): ')
        print("*********************")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print('Invalid Choice')
print("*********************")            
print("Thank you have a nice day!")

if __name__ == '__main__':
    main()
        