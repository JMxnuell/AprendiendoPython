
import sys
ptr = open("file.txt", "r+")

print(ptr.readable()) # ¿se puede leer?
#print(ptr.read()) #leer
#print(ptr.readline()) #leer línea
#print(ptr.readlines()) #en un arreglo

for n in ptr.readlines():
    print(n)

for i in range(0,10):
    ptr.write("\n" + str(i))

ptr.close()

