def getPayerName():
    payer = input("Payer name: ")
    return payer

def getPaidAmount():
    amount = float(input("Amount paid: "))
    return amount

def getParticipantsName():
    participants = []
    number_of_participants = int(input('Participants count: '))
    for i in range(number_of_participants):
        print('Participant -', i+1, ' Name - ')
        participant = input()
        participants.append(participant)
    return participants

def getNote():
    note = input('Add note: ')
    return note

class Splitwise:
    expenses = []
    users = {}

    class Expense:
        def __init__(self, payer, amount, participants, note):
            self.payer = payer
            self.amount = amount
            self.participants = participants
            self.note = note


    def addMembers(self):
        n = int(input('Members Count - '))

        for i in range(n):
            print('Member-', i+1, ' Name - ')
            participant_name = input()
            self.users[participant_name] = 0
        print(self.users)


    def add_expense(self):
        expense = self.Expense(getPayerName(), getPaidAmount(), getParticipantsName(), getNote())
        self.expenses.append(expense)
        split_amount = expense.amount / (len(expense.participants) + 1)
        self.users[expense.payer] += (expense.amount - split_amount)
        for member in expense.participants:
            self.users[member] -= split_amount


    def printExpenses(self):
        for expense in self.expenses:
            print("Payer:", expense.payer)
            print("Amount:", expense.amount)
            print("Participants:", expense.participants)
            print("Note:", expense.note)


    def showParticipantsOutstandingBalance(self):
        for user, balance in self.users.items():
            if balance > 0:
                print(f"{user} gets back {balance} in total")
            if balance < 0:
                print(f"{user} owes {balance} in total")


    def simplifyDebts(self):
        debts = {}
        for key in self.users.keys():
            for expense in self.expenses:
                if key == expense.payer:
                    split_amount = expense.amount / (len(expense.participants) + 1)
                    for member in expense.participants:
                        if key not in debts:
                            debts[key] = dict()
                        debts[key][member] = split_amount
        for creditor, debitor_info in debts.items(): 
            print(f"{creditor} owes") 
            for debitor, balance in debitor_info.items(): 
                print(f"{balance} from {debitor}")


if __name__ == "__main__":
    splitwise = Splitwise()
    while True:
        print("\nOptions:")
        print("1. Add Members")
        print("2. Add expense")
        print("3. Show outstanding balance")
        print("4. Simplify debts")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            splitwise.addMembers()

        elif choice == '2':
            splitwise.add_expense()
            print(splitwise.users)  

        elif choice == '3':
            splitwise.showParticipantsOutstandingBalance()

        elif choice == '4':
            splitwise.simplifyDebts()

        elif choice == '5':
            print("Exiting Splitwise. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid option (1-5).")
