"""
main.py
====================================
"""

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
            if int(size) >= 4:
                a = False
            else:
                print("Podaj poprawną liczbę!")

        except ValueError:
             print("Podaj poprawną liczbę!")
             a = True



    # Podanie progu punktów rozwoju i przechwycenie błędu w razie potrzeby
    print("Podaj wymagane punkty do wygrania: ")

    while a == False:
        req_points = input()
        try:
            val2 = int(req_points)
            if int(req_points) >= 10:
                a = True
            else:
                print("Podaj poprawną liczbę!")

        except ValueError:
            print("Podaj poprawną liczbę!")
            a = False

    sim = Simulation(val1, val2)
    sim.start()
    input()