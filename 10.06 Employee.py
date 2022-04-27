class Employee:
    def __init__(self, first, last, id, hours, wage):
        self.FirstName = first
        self.LastName = last
        self.IDNumber = id
        self.HoursWorked = hours
        self.Wage = wage
    def weeklypay(self):
        if float(self.HoursWorked) > 40:
            ot = float(self.HoursWorked) - 40
            weekly = float(self.HoursWorked) * float(self.Wage) + (1.5 * ot * float(self.Wage))
        else:
            weekly = float(self.HoursWorked) * float(self.Wage)
        return weekly
emp = open('10.06 Payroll.txt')
e = emp.readline()
e = e.split(',')
employee1 = Employee(e[0].strip(), e[1].strip(), e[2].strip(), e[3].strip(), e[4].strip())
e = emp.readline()
e = e.split(',')
employee2 = Employee(e[0].strip(), e[1].strip(), e[2].strip(), e[3].strip(), e[4].strip())
e = emp.readline()
e = e.split(',')
employee3 = Employee(e[0].strip(), e[1].strip(), e[2].strip(), e[3].strip(), e[4].strip())
print("First".rjust(8), "Last".rjust(8), "ID".rjust(8), "Hours".rjust(8), "Hourly".rjust(8), "Weekly".rjust(8))
print("Name".rjust(8), "Name".rjust(8), "Number".rjust(8), "Worked".rjust(8), "Wage".rjust(8), "Pay".rjust(8))
print(employee1.FirstName.rjust(8), employee1.LastName.rjust(8), employee1.IDNumber.rjust(8), "{0:.2f}".format(float(employee1.HoursWorked)).rjust(8), employee1.Wage.rjust(8), "{0:.2f}".format(employee1.weeklypay()).rjust(8))
print(employee2.FirstName.rjust(8), employee2.LastName.rjust(8), employee2.IDNumber.rjust(8), "{0:.2f}".format(float(employee1.HoursWorked)).rjust(8), employee2.Wage.rjust(8), "{0:.2f}".format(employee2.weeklypay()).rjust(8))
print(employee3.FirstName.rjust(8), employee3.LastName.rjust(8), employee3.IDNumber.rjust(8), "{0:.2f}".format(float(employee1.HoursWorked)).rjust(8), employee3.Wage.rjust(8), "{0:.2f}".format(employee3.weeklypay()).rjust(8))
emp.close()