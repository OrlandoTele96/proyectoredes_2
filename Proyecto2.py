
def to_bytes(n):
    Arraybyte=[0,0,0,0,0,0,0,0]#Generamos un vector de 8 bits
    return Arraybyte
##Apertura y lectura de la imagen en formato .txt
archivo=open("/Users/jorgeorlandogonzalez/Desktop/Tareas/proyecto2/imagen.txt","rb")
BytesFrame=0
buffer=archivo.read(1)#Lee el primer byte
while(buffer):
    n=int.from_bytes(buffer,'big')#Convierte a tipo entero
    n=format(n,'b')
    BytesFrame=to_bytes(n)
    print(BytesFrame)
    buffer=archivo.read(1)# Aumenta el buffer al siguiente byte.
    

