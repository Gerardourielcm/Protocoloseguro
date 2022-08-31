print("Bienvenido")
print(" ")

Miset={}
Milista=list(Miset)

num = int(input("Introduce el tamaño del protocolo: "))
elems = len(Milista)
num1 = num+1
print(" ")

for elems in range (1,num1):
    elem = str(input("Introduce el elemento a añadir: "))
    Milista.append(elem)
    Miset=set(Milista)
    print(" ")

print(Miset)
