class Pet ():
    def __init__(self, petname="Fido", pettype="Dog", petage=3):
        self.Name = petname
        self.Type = pettype
        self.Age = petage
pets = open("10.01 Pets.txt")
p = pets.readline()
p = p.split(',')
pet1 = Pet(p[0].strip(), p[1].strip(), p[2].strip())
p = pets.readline()
p = p.split(',')
pet2 = Pet(p[0].strip(), p[1].strip(), p[2].strip())
p = pets.readline()
p = p.split(',')
pet3 = Pet(p[0].strip(), p[1].strip(), p[2].strip())
print("Name".rjust(8), "Type".rjust(8), "Age".rjust(8))
print(pet1.Name.rjust(8), pet1.Type.rjust(8), pet1.Age.rjust(8))
print(pet2.Name.rjust(8), pet2.Type.rjust(8), pet2.Age.rjust(8))
print(pet3.Name.rjust(8), pet3.Type.rjust(8), pet3.Age.rjust(8))
pets.close()