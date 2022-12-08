"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(
        self,
        name,
        contractType,
        salary,
        commissionType,
        commission,
        numberOfContracts,
        numberOfHours,
    ):
        self.name = name
        self.contractType = contractType
        self.salary = salary
        self.commissionType = commissionType
        self.numberOfContracts = numberOfContracts
        self.commission = commission
        self.numberOfHours = numberOfHours

    def get_pay(self):
        totalSalary = 0
        if self.contractType == "monthly":
            totalSalary += self.salary
            if self.commissionType == "None":
                return totalSalary
            elif self.commissionType == "contract":
                totalSalary += self.numberOfContracts * self.commission
                return totalSalary
            elif self.commissionType == "bonus":
                totalSalary += self.commission
                return totalSalary
        else:
            totalSalary += self.salary * self.numberOfHours
            if self.commissionType == "None":
                return totalSalary
            elif self.commissionType == "contract":
                totalSalary += self.numberOfContracts * self.commission
                return totalSalary
            elif self.commissionType == "bonus":
                totalSalary += self.commission
                return totalSalary

    def __str__(self):
        str = ""
        if self.contractType == "monthly":
            if self.commissionType == "None":
                str = f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.salary}."
            elif self.commissionType == "contract":
                val = self.get_pay()
                str = f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.numberOfContracts} contract(s) at {self.commission}/contract. Their total pay is {val}."
            elif self.commissionType == "bonus":
                val = self.get_pay()
                str = f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}. Their total pay is {val}."

        else:
            if self.commissionType == "None":
                val = self.get_pay()
                str = f"{self.name} works on a contract of {self.numberOfHours} hours at {self.salary}/hour. Their total pay is {val}."
            elif self.commissionType == "contract":
                val = self.get_pay()
                str = f"{self.name} works on a contract of {self.numberOfHours} hours at {self.salary}/hour and receives a commission for {self.numberOfContracts} contract(s) at {self.commission}/contract. Their total pay is {val}."
            elif self.commissionType == "bonus":
                val = self.get_pay()
                str = f"{self.name} works on a contract of {self.numberOfHours} hours at {self.salary}/hour and receives a bonus commission of {self.commission}. Their total pay is {val}."
        return str


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", "monthly", 4000, "None", 0, 1, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", "hourly", 25, "None", 0, 1, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", "monthly", 3000, "contract", 200, 4, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", "hourly", 25, "contract", 220, 3, 150)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", "monthly", 2000, "bonus", 1500, 1, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", "hourly", 30, "bonus", 600, 1, 120)

