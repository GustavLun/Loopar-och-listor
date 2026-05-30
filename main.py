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

#1.5
for y in range (1,7):
    s = ""
    for x in range (1,9):
        if x == y+1 :
            s += "#"
        else:
            s += "."
    print(s)
# Programmet kommer skriva ut 6 rader där varje gång x = y så kommer en # skrivas ut. Raderna är 8 breda som beskrivs i forloppen inuti forloopen.
# För varje gång x och Y inte är samma skrivs en punkt.
# För att flytta linjen kan vi ändra if statement till if x == y + 1, då kommer hashtagen alltid ske ett snäpp fram från där x och y är samma.

