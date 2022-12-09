"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, type_of_contract, hours=None, pay=None, bonus_comm=0, cont_comm=0, commission_per_contr=0):
        self.person_name = name
        self.type_of_contract = type_of_contract
        self.hours = hours
        self.pay = pay
        self.bonus_comm = bonus_comm
        self.cont_comm = cont_comm
        self.commission_per_contr = commission_per_contr

    def get_pay(self):
        if self.type_of_contract == 'salary':
            contract_pay = self.pay
        else:
            contract_pay = self.hours * self.pay

        if self.bonus_comm:
            commission_pay = self.bonus_comm
        elif self.cont_comm:
            commission_pay = self.cont_comm * self.commission_per_contr
        else:
            commission_pay = 0

        return contract_pay + commission_pay

    def __str__(self):
        string = self.person_name

        if self.type_of_contract == 'salary':
            string += ' works on a monthly salary of {}'.format(self.pay)
        else:
            string += ' works on a contract of {} hours at {}/hour'.format(
                self.hours, self.pay)

        if self.bonus_comm:
            string += ' and receives a bonus commission of {}'.format(
                self.bonus_comm)
        elif self.cont_comm:
            string += ' and receives a commission for {} contract(s) at {}/contract'.format(
                self.cont_comm, self.commission_per_contr)

        string += '.  Their total pay is {}.'.format(self.get_pay())

        return string


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = Employee('Billie', 'salary', pay=4000)

# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', hours=100, pay=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.
renee = Employee('Renee', 'salary', pay=3000, cont_comm=4, commission_per_contr=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = Employee('Jan', 'hourly', hours=150, pay=25, cont_comm=3, commission_per_contr=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.
robbie = Employee('Robbie', 'salary', pay=2000, bonus_comm=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', hours=120, pay=30, bonus_comm=600)
