balance = 0.0
kyc_documents = {}
def check_balance():
    print(f"Your current balance is {balance}")
    print("==================================")

def deposit(amount):
    global balance
    if amount > 0:
        balance =+ amount
        print()
        print("======================================")
        print("======================================")
        print(f"An amount of {amount} is deposited in your account.")
        print(f"Your current balance is {balance}")
        print("======================================")
        print()
    else:
        print("Cannot Deposit negative or zero amount")
        print("======================================")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Cannot Withdraw negative or zero amount")
        print("=======================================")
    elif amount > balance:
        print("Cannot Withdraw. Insufficient balance")
        print("=====================================")
    else:
        balance -= amount
        print()
        print("=============================================================")
        print(f"Withdrawn an amount {amount}. Remaining balance is {balance}")
        print("=============================================================")
        print()

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("No documents available")
    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")

if __name__ == "__main__":
    print("=========================================")
    print("Welcome to Vikas Personal Banking App")
    print("=========================================")
    print()

    while True:
        print("1. Check your balance")
        print("2. Deposit an amount")
        print("3. Withdrawal an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")
        print()

        if choice == '1':
            check_balance()
        elif choice == '2':
            amount = float(input("Enter your amount: "))
            deposit(amount)
        elif choice == '3':
            amount = float(input("Enter an amount to be withdrawn: "))
            withdraw(amount)
        elif choice == '4':
            check_kyc()
        elif choice == '5':
            n_documents = int(input("Enter number of documents to be added: "))
            kyc_doc = {}
            for i in range (n_documents):
                key = input("Enter the type of document: ")
                value = input("Enter the uniq ID of document: ")
                kyc_doc[key] = value
            update_kyc(kyc_doc)
            print("KYC Updated")

        elif choice == '6':
            break
        else:
            print("Invalid choice, Try again")
    print("===================================")
    print("Thank you for using Banking with us")
    print("===================================")

