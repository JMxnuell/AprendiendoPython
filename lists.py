myList = ['a','b','c'] #así sabe python que es una lista
print(myList[0]) #primer valor
print(myList[-1]) #ultimo valor
print(myList) #lista entera
print(myList[1:]) #rango específico
numbers = [3,2,1]
#Functions

#extens
myList.extend(numbers) # lista append lista
myList.append('d') #agrega al final
myList.insert(0,'0') #agrega al inicio
print(myList)
myList.remove('d') #elimita objeto específico
print(myList)
myList.pop() #remove final
print(myList.index('a'))
print(myList.count('a'))
numbers.sort()
numbers.reverse()
myList2 = myList.copy() #una copia de la lista
print(numbers)