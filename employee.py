"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        print(self.name)

    def __str__(self):
        return self.name

class EmployeeSalaryContractNoCommission(Employee):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.salary}."

class EmployeeHourlyContractNoCommission(Employee):
    def __init__(self,name,hours,rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
    def get_pay(self):
        return self.hours * self.rate

    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour.  Their total pay is {self.hours * self.rate}.'


class EmployeeSalaryContractBonus(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus

    def get_pay(self):
        return self.salary + self.bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.bonus + self.salary}."

class HourlyContractBonusCommission(Employee):
    def __init__(self,name,hours,rate,bonus):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
        self.bonus = bonus

    def get_pay(self):
        return (self.hours * self.rate) + self.bonus

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {(self.hours * self.rate) + self.bonus}."


class HourlyContractContractCommission(Employee):
    def __init__(self, name, hours, rate,ncontracts,cpc):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
        self.ncontracts = ncontracts
        self.cpc = cpc

    def get_pay(self):
        return (self.hours * self.rate) + (self.ncontracts * self.cpc)

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.ncontracts} contract(s) at {self.cpc}/contract. Their total pay is {(self.hours * self.rate) + (self.ncontracts * self.cpc)}."

class SalaryContractContractCommission(Employee):
    def __init__(self,name,salary,ncontracts,cpc):
        super().__init__(name)
        self.salary = salary
        self.ncontracts = ncontracts
        self.cpc = cpc

    def get_pay(self):
        return self.salary + (self.ncontracts * self.cpc)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.ncontracts} contract(s) at {self.cpc}/contract. Their total pay is {self.salary + (self.ncontracts * self.cpc)}."






# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = EmployeeSalaryContractNoCommission("Billie","4000")


charlie = EmployeeHourlyContractNoCommission("Charlie",100,25)


robbie = EmployeeSalaryContractBonus("Robbie",2000,1500)


ariel = HourlyContractBonusCommission("Ariel",120,30,600)


jan = HourlyContractContractCommission("Jan",150,25,3,220)


renee = SalaryContractContractCommission("Renee",3000,4,200)


