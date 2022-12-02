while True :

    print("kies een getal")
    getal1 = int(input())
    print("kies nog een getal")
    getal2 = int(input())
    print("wil je plus min delen of keer?")
    operator = input()

    if operator == "plus":
     print ("het anwtoord is", getal1 + getal2)

    elif operator == "min":
     print ("het antwoord is", getal1 - getal2)

    elif operator == "keer":
     print ("het antwoord is", getal1 * getal2)

    elif operator == "delen":
     print ("het antwoord is", getal1 / getal2)
     
    print("wil je opnieuw?")
    antwoord = input()

    if antwoord == "nee":
        break




