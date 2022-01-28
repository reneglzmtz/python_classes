class Account:
    """A class that represent a type of bank account"""

    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count +=1

    @classmethod
    def message_number_accounts(cls):
        print(f'Accounts created so far = {Account.instance_count}')

    def __init__(self, account_number, name_holder, opening_balance):
        Account.increment_instance_count()
        Account.message_number_accounts()
        self.account_number = account_number
        self.name_holder = name_holder
        self._balance = opening_balance

    @property
    def balance(self):
        '''The docstring for the balance property'''
        return self._balance
    
    def __str__(self):
        return f"Account[{self.account_number}] - {self.name_holder}, account = {self.balance}"

    def deposit(self, value):
        self._balance += value
    
    def withdraw(self, value):
        self._balance -= value

class CurrentAccount(Account):
    '''subclass of the Account class, adds an overdraft limit as well as redefines the withdraw method'''

    def __init__(self, account_number, name_holder, opening_balance, overdraft_limit):
        super().__init__(account_number, name_holder, opening_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, value):
        if self.balance + self.overdraft_limit >= value:
            return super().withdraw(value)
        else: print('Withdrawal would exceed your overdraft limit')

class DepositAccount(Account):
    def __init__(self, account_number, name_holder, opening_balance, interest_rate):
        super().__init__(account_number, name_holder, opening_balance)
        self.interest_rate = interest_rate

class InvestmentAccount(Account):
    def __init__(self, account_number, name_holder, opening_balance, investment_type):
        super().__init__(account_number, name_holder, opening_balance)
        self.investment_type = investment_type

class Manhattan():
    def __init__(self, x_coord, y_coord):
        self._x = x_coord
        self._y = y_coord

    def get_x(self):
        return self._x
    
    def set_x(self, new_x):
        if isinstance(new_x, int):
            self._x = new_x

    x = property(get_x, set_x, doc='x coordinate property')

    def get_y(self):
        return self._y
    
    def set_y(self, new_y):
        if isinstance(new_y, int):
            self._y = new_y

    y = property(get_y, set_y, doc='y coordinate property')


    def __add__(self, other):
        x,y = self.x + other.x, self.y + other.y
        return Manhattan(x,y)

    def __sub__(self, other):
        x,y = self.x - other.x, self.y - other.y
        return Manhattan(x,y)

    def __str__(self):
        return f'Manhattan({self.x}, {self.y})'

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other):
        return self.manhattan_distance(other) == 0

    def __gt__(self, other):
        return self.manhattan_distance(Manhattan(0,0)) > other.manhattan_distance(Manhattan(0,0))


# CurrentAccount(account_number, account_holder, opening_balance, overdraft_limit)
acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
# DepositAccount(account_number, account_holder, opening_balance, interest_rate)
acc2 = DepositAccount('345', 'John', 23.55, 0.5)
# InvestmentAccount(account_number, account_holder, opening_balance, investment_type)
acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')


acc1.deposit(23.45)
acc1.withdraw(12.33)
print('balance:', acc1.balance)
acc1.withdraw(300.00)
print('balance:', acc1.balance)

print(f'Number of Account instances created: {Account.instance_count}')

vector1 = Manhattan(2,3)
vector2 = Manhattan(3,4)

vector3 = vector1 + vector2

vector4 = vector1 - vector2
print(vector3)
print(vector4)

vector4.x, vector4.y = 10,"a"

print(vector4)

d = vector1.manhattan_distance(vector2)

print(d)

print(vector1 < vector2)