import random
from random import randint



# pod indeksem 0 ile hp, pod 1 atak, pod 2 leczenie

Michał = [1000, 323, 277]
Andrzej = [1000, 500, 100]

print("Wiataj w grze Andzrej and Michał")
print("Wybierz Michał albo Andzrej ")     

inp = input()

if inp == "Michał":

    print("Jesteś michałem zaatakuj andrzeja")
    print("co chcesz zrobić Michale?")
    print("Atak / Leczenie")

    while Michał[0] > 0:

        
        print(f"Twoje dane to {Michał}")
        print(f"HP przeciwnika to {Andrzej[0]}")
        print("co chcesz zrobić Michale?")
        print("Atak / Leczenie")

        i = input()

        if i == "Atak":

            Andrzej[0] -= Michał[1]
            kontr = random.randint(199, 450)
            Michał[0] -= kontr

            print(f"Andzrej ma teraz{Andrzej[0]}")
            print(f"Teraz masz Michał ci hp o  {Michał[0]}")
            print(f"Andrzej kontruje i zadaje ci {kontr} obrazen!")

        elif i == "Leczenie":

            leczenia_gracza = Michał[2]
            Michał[0] += leczenia_gracza
            leczenie_andrzeja = random.randint(150, 450)
            Andrzej[0] += leczenie_andrzeja

            print(f"twoje hp wynosi{Michał[0]}")
            print(f"Andrzej hp wynosi{Andrzej[0]}")

        else:
            print("Nie możesz czegó takiegoś wpisać ok?")

        if Andrzej[0] <= 0:
            print("Michał król wygrał")
            break
        if Michał[0] <= 0:
            print("Andzrej wygrał michał przgrał")
            break

    print("Andzrej wygrał michał przgrał,")
    print("Good game,well playd sigmo")


elif inp == "Andrzej":

    print("Jesteś andrzejem zaatakuj michała")
    print("co chcesz zrobić Andzreju ?")
    print('Atak / Leczenie')

    while Andrzej[0] > 0:

        
        print(f"twoje dane to {Andrzej}")
        print(f"HP przeciwnika to {Michał[0]}")
        print("co chcesz zrobić Andzreju ?")
        print('Atak / Leczenie')
        i = input()

        if i == "Atak":
            
            Michał[0] -= Andrzej[1]
            kontr = random.randint(100, 400)
            Andrzej[0] -= kontr

            print(f"Michał ma teraz{Michał[0]}")
            print(f"Teraz masz andrzej {Andrzej[0]}")
            print(f"Michał kontruje i zadaje ci {kontr} obrazen!")

        elif i == "Leczenie":

            leczenie_andrzeja = Andrzej[2]
            Andrzej[0] += leczenie_andrzeja
            leczenie_michala = random.randint(150, 450)
            Michał[0] += leczenie_michala

            print(f"twoje hp wynosi{Andrzej[0]}")
            print(f"michał hp wynosi{Michał[0]}")

        else:
            print("nie mozesz czegós takiego zrobić okej?")

        if Michał[0] <= 0:
            print("Andzrje król wygrał")
            break
        if Andrzej[0] <= 0:
            print("Michał wygrał andrzej przgrał")
            break

    print("Michał wygrał andrzej przgrał")
    print("Air Frajer")
