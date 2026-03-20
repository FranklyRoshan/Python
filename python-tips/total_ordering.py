from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr(self.currency, self.amount)
    
    def __eq__(self, other):
        return (self.currency, self.amount) == (other.currency, other.amount)
    
    # Any one of the comparision operator implementation
    def __ge__(self, other):
        return (self.currency, self.amount) > (other.currency, other.amount)
    

amount1 = Money('EUR', 10)
amount2 = Money('EUR', 20)
amount3 = Money('EUR', 10)

print(amount1 > amount2)
print(amount2 > amount3)
print(amount3 > amount1)
print(amount3 <= amount1)
print(amount3 >= amount1)