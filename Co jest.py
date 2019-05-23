class Member:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fname(self):
        return "{} {}".format(self.name, self.age)

class Fraction(Member):

    def __init__(self, name, age, members = None):
        super().__init__(name, age)
        if members is None:
            self.members = []
        else:
            self.members = members

    def add_mem(self, mem):
        if mem not in self.members:
            self.members.append(mem)

    def remove_mem(self, mem):
        if mem in self.members:
            self.members.remove(mem)

    def print_mem(self):
        for mem in self.members:
            print('-->', mem.fname())

frakcja = ('Czerwoni', 'Niebiescy')

member_1 = Member(frakcja[0], 20)
member_2 = Member(frakcja[0], 25)
member_3 = Member(frakcja[1], 80)
frakcja_1 = Fraction(frakcja[0], 20)


frakcja_2 = Fraction(frakcja[1], 50)



frakcja_1.add_mem(member_1)
frakcja_1.add_mem(member_2)
frakcja_2.add_mem(member_3)


print("Obiekty w frakcji czerwonej: ")
frakcja_1.print_mem()
print("Obiekty w frakcji niebieskiej: ")
frakcja_2.print_mem()