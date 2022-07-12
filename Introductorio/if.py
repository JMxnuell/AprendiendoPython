vive = False
dormido = True
if vive:
    print("its live")
elif dormido:
    print("sleeping")
else:
    print("its not live")

def compar(a,b,c):
    if a >= b and a >= c:
        print(str(a),"mayor",sep=" ",end="\n")
    elif b >= a and b >= c:
        print(str(b), "mayor", sep=" ", end="\n")
    else:
        print(str(c), "mayor", sep=" ", end="\n")

compar(1,2,3)