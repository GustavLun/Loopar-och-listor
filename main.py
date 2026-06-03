# # Uppgift 1
# # 1.1 Min första gissning är att indes kommer plussas med 2 tills att den blir 15 eller höger, därefter stoppar programmet.
# limit = 15
# index = 5
# while index <= limit:
#     print (index)
#     index = index + 2
#
# # 1.2
# # Programmet kommer göras 10 gånger, så länge i är lägre än 10, varje nummer utom 5 kommer printas ut.
# for i in range (10):
#     if i ==5:
#         print("")
#     else:
#         print(i)
#         i=i+1
import random
from contextlib import nullcontext
from tokenize import blank_re

# #1.3
# # Kan vara så att den köra oändligt då i aldrig blir högre än 0, eller så kör den 6 gånger och den kommer printa varje nummer upp till 5.
# counter = 0
# for i in range (6):
#     counter += i
#     print(counter)
# # Efter att ha kör och googlat, programmet kommer köras 6 gånger, i kommer slänga ut siffor från 0 - 6, där efter kommer counter plusas och bli summan, nästa varv har då counter ett nytt värde som kommer plussas med en mer därav kommer värdet växa eftersom counter blir värdet av I efter varje varv.

# #1.4
# # så länge y är mindre än 10 om y är skillt 2 från 0 så är x - y och sedan blir x det nya Y värdet, annars plussas x med y för att sedan bli nya y gånger Y, Y plussas med 1 varje gång
# x = 0
# y = 1
# while y< 10:
#     if y % 2 == 0:
#         x -= y
#         print(x)
#         print(y)
#     else:
#         x += y * y
#         print(x)
#         print(y)
#     y += 1
# # Jag hade fel. Först så skrivs inget ut då ingen print finns i koden. % är rest, så när vi tar rest så kan man räkna hur många % x som går in i det första talet ex 30 % 11 = 8 11 kan multipliceras 2 gågner och bli 22 men kan inte göras igen, hur mycket rest är det kvar för att det skall bli 30.
# #  i detta fall då så länge y % 2 har en rest på 0 så subtraheras x med Y för att sedan bli Y
# # så fort y blir ojämnt kommer det bli rest kvar och då körs den undre talet.

# #1.4
# message = "its_time_to_get_coding"
# print(message [4:8])
# # Vi fastslår ett värde på variablen message, efter detta körs en print med två klamer som innehåller range där vi specificerar en start och ett slut på värdet vi givit "message"

# #1.5
# for y in range (1,7):
#     s = ""
#     for x in range (1,9):
#         if x == y+1 :
#             s += "#"
#         else:
#             s += "."
#     print(s)
# # Programmet kommer skriva ut 6 rader där varje gång x = y så kommer en # skrivas ut. Raderna är 8 breda som beskrivs i forloppen inuti forloopen.
# # För varje gång x och Y inte är samma skrivs en punkt.
# # För att flytta linjen kan vi ändra if statement till if x == y + 1, då kommer hashtagen alltid ske ett snäpp fram från där x och y är samma.

# # 2 Öva på loopar och listor
#
# # 1A
# answer = 0
# for i in range (1,11): # 11 måste läggas till då man räknar bryter innan sista talet på rangen, hade jag tagit till 10 hade det bara blivit 9.
#     answer += i
# print ("Summan av talen 1 till 10 är:" + str(answer))

# # 1b
# answer = 0
# for i in range (1, 101):
#     answer += i
# print ("Summan av talen 1 till 100 är: " + str(answer))

# # 1c
# answer = 0
# while answer < 5050:
#     for i in range (101):
#      answer += i
# else: print ("Summan av talen 1 till 100 är: " + str(answer))

# # 2
# print (sum(list ([1, -2, 3, -2, 4, -3])))

# 3 Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som står i presentationen.
# 3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan med funktionen print.

# movies = ["inception", "Interstellar", "Super mario", "Spider-man"]
# print (movies)

# # 3b Lägg till "Fellowship of the ring" sist i listan.
#
# movies = ["inception", "Interstellar", "Super mario", "Spider-man", "Fellowship of the ring"]
# print (movies)
#
# # 3c Lägg till "The two towers" på första platsen i listan. (index noll)
# movies = ["The two towers","inception", "Interstellar", "Super mario", "Spider-man", "Fellowship of the ring"]
# print (movies)

# # 3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
# movies = ["The two towers","inception", "Interstellar", "Super mario", "Spider-man", "Fellowship of the ring"]
# index = movies.index("Fellowship of the ring")
# print("Fellowship of the ring ligger på plats ", index)
# # Index för filmen är 5
#
# # 3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
#
# movies = ["The two towers","inception", "Interstellar", "Spider-man", "Fellowship of the ring"]
# index = movies.index("Fellowship of the ring")
# print("Fellowship of the ring ligger nu på plats ", index)
# #Ja programmet säger att index nu är 4
#
# # 3f Ta reda på hur lång listan är. (len)
# movies = ["The two towers","inception", "Interstellar", "Spider-man", "Fellowship of the ring"]
# print("I listan finns totalt",len(movies), "filmer")
#
# # 3g Vänd listan baklänges.
#
# movies = ["The two towers","inception", "Interstellar", "Spider-man", "Fellowship of the ring"]
# movies.reverse()
# print(movies)
#
# # 3h Sortera listan stigande i bokstavsordning.
# movies = ["The two towers","Inception", "Interstellar", "Spider-man", "Fellowship of the ring"]
# movies.sort()
# print(movies)

# # 3 Kvittouträknaren
# Total = 0
# while True:
#     tal=input("Skriv ett tal eller quit ")
#
#     if tal == "quit":
#         break
#
#     addering = int(tal)
#     Total += addering


# # Version 2
# Total = 0
# while True:
#     tal=input("Skriv ett tal eller quit ")
#
#     if tal == "quit":
#         break
#
#     addering = int(tal)
#     Total += addering
#
# antal_folk = int(input(" hur många är ni i sällskapet? "))
#
# print(f"Totala summan blir", Total, f"Detta motsvarar {Total / antal_folk} kronor per person")

# Version 3
# Total = 0
# while True:
#     tal=input("Skriv ett tal eller quit ")
#
#     if tal == "quit":
#         break
#     if tal .isdigit():
#         addering = int(tal)
#         Total += addering
#     else:
#         print("Endast siffror tack")
#
#
# while True:
#     antal_folk = (input(" hur många är ni i sällskapet? "))
#     if antal_folk.isdigit() and int (antal_folk) > 0:
#         antal_folk = int(antal_folk)
#         break
#     else:
#         print(" Skriv ett heltal större än 0")
#
# print("Totala summan blir", Total, f"Detta motsvarar kronor per person", Total / int(antal_folk))
#
# while True:
#     tip_question = (input("Hur många procent i dricks vill ni betala "))
#
#     if tip_question == "":
#         tip_request = 10
#         print(f" Eftersom du inte valde någon drick blir den automatiskt 10%")
#         break
#
#     if tip_question.isdigit():
#         tip_request = int(tip_question)
#         break
#     else:
#         print(" Endast siffror eller tryck enter")
#
# if tip_request > 0:
#     print(f"Då ska ni betala {Total * (tip_request / 100)} kronor i dricks")
# elif tip_request <= 0:
#     print("Okej ingen dricks tack ändå ")

# 4
#A
# for y in range (1,7):
#     s=""
#     for x in range (1,9):
#         if x == 1 :
#             s += "#"
#         else:
#             s += "."
#     print(s)
 #B
# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if x +1 == y + 1:
#             s += "#"
#         else:
#             s += "."
#     print(s)
#
#C
# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if x == 3 or x == 4 or x == 5:
#             s += "#"
#         else:
#             s += "."
#     print(s)
 #D
# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if x == 3 or y == 3:
#             s += "#"
#         else:
#             s += "."
#     print(s)

#E
# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if x == 5 or x == 7 - y :
#             s += "#"
#         else:
#             s += "."
#     print(s)

#f
# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if x == 0 + y or x == 7 - y :
#             s += "#"
#         else:
#             s += "."
#     print(s)

#g
# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if x == 1 or x == 3 or x == 5 or x == 7:
#             s += "#"
#         else:
#             s += "."
#     print(s)

#h
# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if y == 1 or y == 6   :
#             s += "."
#         elif y == 2 or y == 5:
#             if x == 1 or x == 8:
#                 s += "."
#             else:
#              s += "#"
#         else:
#             if x == 2 or x == 7:
#                 s += "#"
#             else:
#              s += "."
#     print(s)

#i
# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if y == 1 or y == 6   :
#             s += "."
#         elif y == 2 or y == 5:
#             if x == 1 or x == 8:
#                 s += "."
#             else:
#              s += "#"
#         else:
#             if x == 2 or x == 7:
#                 s += "#"
#             else:
#              s += "."
#     print(s) # Nej kommer inte kunna lösa ...

#J
# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if y == 1 or y == 2 or y == 3:
#             if x == 3 or x == 6:
#              s += "#"
#             else:
#                 s += "."
#         if y == 4:
#             s += "."
#         if y == 5:
#             if x == 2 or x == 4 or x == 6 or x == 8:
#                 s += "#"
#             else:
#                 s += "."
#         if y == 6:
#             if x == 1 or x == 3 or x == 5 or x == 7:
#                 s += "#"
#             else:
#                 s += "."
#     print(s)

# # 5 Gissa talet version 1
# secret = random.randint (1,100)
# while True:
#     guess = (int(input("Välkommen, gissa på ett tal mellan 1-100")))
#     if guess < secret:
#         print("Det var för lågt gissa igen")
#     elif guess > secret:
#         print("Det var för högt gissa igen")
#     else:
#         print("Grattis det var rätt")
#         break

# 5 Gissa talet version 2
secret = random.randint (1,100)
while True:
    guess = (int(input("Välkommen, gissa på ett tal mellan 1-100 ")))
    if guess < secret:
        print("Det var för lågt gissa igen")
        if secret - guess <=5:
            print("Nära! Du är max 5 tal ifrån")
    elif guess > secret:
        print("Det var för högt gissa igen")
        if guess - secret <=5:
            print("Nära! du är max 5 tal ifrån")
    else:
        print("Grattis det var rätt")
        break
