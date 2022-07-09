
i = 0

while i < 10:
    print(i, end=",")
    i+=1

print("\nDone\n")

semana = {
    #1 = key, 2 = Value
    1 : "Monday",
    2 : "Tuesday",
    3 : "wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday",
}

for dia in semana:
    print(semana[dia], end=",")

print()

for l in "Manuel":
    print(l,end=",")

print()

for i in range(1,11): #EL LIMITE NO LO TOMA
    print(i,end=",")