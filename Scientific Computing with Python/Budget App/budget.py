class Category:
    def __init__(self,category):
        self.category = category
        self.ledger = []

    def __str__(self):
        output = self.category.center(30,'*')
        for item in self.ledger:
            description = item['description']
            if len(description) > 23:
                description = description[:23]
            amount = '{:.2f}'.format(item['amount'])
            if len(amount) > 7:
                amount = amount[:7]
            output = '\n'.join([output, description + ' '*(30-len(description)-len(amount)) + amount])
        output = '\n'.join([output, 'Total: {}'.format('{:.2f}'.format(self.get_balance()))])

        return output

    def deposit(self,amount,description=''):
        self.ledger.append({'amount':amount, 'description':description})

    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount':amount*(-1), 'description':description})
            return True
        return False
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total
    
    def transfer(self,amount,other):
        if self.check_funds(amount):
            self.ledger.append({'amount':amount*(-1), 'description':'Transfer to {}'.format(other.category)})
            other.deposit(amount,'Transfer from {}'.format(self.category))
            return True
        return False

    def check_funds(self,amount):
        total = self.get_balance()
        if amount > total:
            return False
        return True



def create_spend_chart(categories):
    # Handle math and calculations
    space = 5+3*len(categories)
    spending = dict()
    for category in categories:
        total = 0
        for items in category.ledger:
            if items['amount'] < 0:
                total += items['amount']
        spending[category.category] = total*-1

    spending_total = sum(spending.values())
    for key, value in spending.items():
        spending[key] = int((value/spending_total*100)//10)

    # Handle output
    output = 'Percentage spent by category\n'
    for i in reversed(range(11)):
        output += str(i*10).rjust(3,' ') + '|'
        for value in spending.values():
            if value >= i:
                output += ' o '
            else:
                output += '   '
        output += ' \n'
    output += '    ' + '-'*(3*len(categories)+1) + '\n'

    max_length = 0
    for key in spending.keys():
        if len(key) > max_length:
            max_length = len(key)
    
    for i in range(max_length):
        output += '    '
        for key in spending.keys():
            if len(key) > i:
                output += ' {} '.format(key[i])
            else:
                output += '   '
        output += ' \n'
    return output
            


if __name__ == '__main__':
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)

    print(create_spend_chart([food, clothing, auto]))
