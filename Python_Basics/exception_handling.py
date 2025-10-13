try:
    i = 0
    number = 10/i
except (ZeroDivisionError, ValueError): # like catch
    number = 0
else: # else is executed when exception isn't thrown
    print("else")
finally: # it'll always print
    print("Finally")

print(number)


class Amount:
    def __init__ (self, currency, amount):
        self.currency  = currency
        self.amount = amount

    def add(self, that):
        if(self.currency == that.currency):
            self.amount += that.amount
        else:
            raise CurrencyDoNotMatchException(self.currency + " " + that.currency)
    
    def __repr__(self):
        return repr((self.currency, self.amount))
    
class CurrencyDoNotMatchException(Exception):
    def __inti__ (self, message):
        super().__init__(message)
    

amount1 = Amount('EUR', 35)
amount2 = Amount('INR', 70)

amount2.add(amount1)
print(amount2)