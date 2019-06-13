from Simulation import Simulation

if __name__ == "__main__":

    print("Witaj w symulacji cywylizacji!")

    print("Podaj wielkość mapy: ")

    #Podanie wielkości mapy i przechwycenie błędu w razie potrzeby
    a = True
    while a == True:
        size = input()
        try:
            val1 = int(size)
            a = False
        except ValueError:
            print("Podaj poprawną liczbę!")
            a = True

    # Podanie progu punktów rozwoju i przechwycenie błędu w razie potrzeby
    print("Podaj wymagane punkty do wygrania: ")

    while a == False:
        req_points = input()
        try:
            val2 = int(req_points)
            a = True
        except ValueError:
            print("Podaj poprawną liczbę!")
            a = False

    sim = Simulation(val1, val2)
    sim.start()