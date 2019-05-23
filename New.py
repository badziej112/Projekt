class Member:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        print("{} {}".format(self.name, self.age)

class Fraction(Member):

    def __init__(self, name, age, members = None):
        super().__init__(name,age)
        if members = None:
            self.members = []
        else:
            self.members = members


    def add_member(self, mem):
        if mem not in self.members:
            self.members.append(mem)

    def remove_member(self, mem):
        if mem in self.members:
            self.members.remove(memb)

    def print_members(self):
        for mem in self.members
            print("--> ", mem.name())




#frakcja = ("Czerwoni", "Niebiescy")

#frakcja_1 = Fraction(frakcja[0], 20)

#Fraction.print_members()

