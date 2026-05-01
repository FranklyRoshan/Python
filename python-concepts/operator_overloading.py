class Money:
    def __init__ (self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency, self.amount))
    

    def __add__(self, other):
        return Money(self.currency, self.amount + other.amount)
    
    def __sub__(self, other):
        return Money(self.currency, self.amount - other.amount)

    
    def __eq__(self, other):
        return ((self.currency, self.amount) == (other.currency, other.amount))
    
    # Not Equal Operator will be automatically done by python, No need write the separate method code for Not Equal
    # def __ne__(self, other):
    #     return ((self.currency, self.amount) != (other.currency, other.amount))


    def __gt__(self, other):
        return ((self.currency, self.amount) > (other.currency, other.amount))
    
    def __ge__(self, other):
        return ((self.currency, self.amount) >= (other.currency, other.amount))
    
    def __lt__(self, other):
        return ((self.currency, self.amount) < (other.currency, other.amount))
    
    def __le__(self, other):
        return ((self.currency, self.amount) <= (other.currency, other.amount))


amount1 = Money('EUR', 10)
amount2 = Money('EUR', 20)
amount3 = Money('EUR', 10)

print(amount1 > amount2)
print(amount2 > amount3)
print(amount3 > amount1)

print(amount3 <= amount1)
print(amount3 >= amount1)

# print(amount1 == amount2)
# print(amount1 != amount2)
# print(amount1 + amount2)
# print(amount1 - amount2)


# object.__add__(self.other)
# object.__sub__(self.other)
# object.__mul__(self.other) *
# object.__matmul__(self.other)
# object.__truediv__(self.other) \
# object.__floordiv__(self.other) \\
# object.__mod__(self.other) %
# object.__pov__(self.other[, modulo]) **
# object._and__(self.other) and
# object.__xor__(self.other) ^
# object.__or__(self.other) or
#
# i method


''' >>> (1,1) == (1,1)
    True
    >>> ('1',1) == ('1',1)
    True
    >>> ('1',1) == ('1',2)
    False
    >>> ('1',1) > ('1',2)
    False
    >>> (1,1) > (0,1)
    True
    >>>
    >>> (1,2) > (1,1)
    True
    >>> (1,2) > (1,3)
    False
    >>> (1,2) < (1,3)
    True
    >>> '''