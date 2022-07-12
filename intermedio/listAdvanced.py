
# lista: ordenar, permite duplicar elementos, variable
'''
l = ["A","B", "C"]
print(l)
l2 = ["Hola",120,1.1,'1']
print(l2)

item = l[-1] #último item, -2 penúltimo y así...
print(item)


for i in l:
    print(i)

if "Hola" in l2:
    print("y")
else:
    print("n")

print(len(l))
l.append("D") #insert on the end of de list
l.insert(1, "A0") #insert on the index u want
item2 = l.pop() #remove the last item
print(item2)
l.remove("A") #remove specific item
print(l)
l.clear() #clear complete list
print(l)

l.reverse() #revierte el orden

l.sort() #ordena ascendente

new_list = sorted(l) #ordena la lista en una nueva
'''
m = [0] * 5
m2 = [1,2,3,4,5]
print(m)
m3 = m + m2 #concatena las listas
print(m3)

#m4 = m3[1:] #en rango
#m4 = m3[::2] #toma uno sí uno no
m4 = m3[::-1] #en reversa
print(m4)

#copy = m4 #la asignación se hace por referencia
copy = m4.copy() #forma correcta si queremos copiarlo
#otra opción
copy = m4[:]

a = [1,2,3,4]
b = [i*i for i in a] #forma fancy

print(b)
