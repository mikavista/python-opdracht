import random
print("hoeveel dobbelstenen wil je gooien?")
aantal = input()
print("..........")
ogen = [1 ,2 ,3 ,4 ,5 ,6]

kort = 0

for x in range(int(aantal)):
    lang = random.choice(ogen)
    print (lang)
    kort = kort + int(lang)
print("jouw aantal is", + kort)