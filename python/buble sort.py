import random 
import time
arr=[]
tiempoTotal=[]
def mostrar():
    for i in arr:
        print(i)


def burbuja(arr,nu):
    n=nu-1
    band=False
    while band==False:
        band=True
        for i in range(n):
            if arr[i]>arr[i+1]:
                aux=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=aux
                band=False


for i in range(100000):
        num=random.randint(0,100000)
        arr.append(num)
mostrar()
#100 numeros
tiempoInicio=time.time()
burbuja(arr,100)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#500 numeros
tiempoInicio=time.time()
burbuja(arr,500)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#1000 numeros
tiempoInicio=time.time()
burbuja(arr,1000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#2000 numeros
tiempoInicio=time.time()
burbuja(arr,2000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#3000 numeros
tiempoInicio=time.time()
burbuja(arr,3000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#4000 numeros
tiempoInicio=time.time()
burbuja(arr,4000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#5000 numeros
tiempoInicio=time.time()
burbuja(arr,5000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#6000 numeros
tiempoInicio=time.time()
burbuja(arr,6000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#7000 numeros
tiempoInicio=time.time()
burbuja(arr,7000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#8000 numeros
tiempoInicio=time.time()
burbuja(arr,8000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#9000 numeros
tiempoInicio=time.time()
burbuja(arr,9000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#10000 numeros
tiempoInicio=time.time()
burbuja(arr,10000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#20000 numeros
tiempoInicio=time.time()
burbuja(arr,20000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#30000 numeros
tiempoInicio=time.time()
burbuja(arr,30000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#40000 numeros
tiempoInicio=time.time()
burbuja(arr,40000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#50000 numeros
tiempoInicio=time.time()
burbuja(arr,50000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#60000 numeros
tiempoInicio=time.time()
burbuja(arr,60000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#70000 numeros
tiempoInicio=time.time()
burbuja(arr,70000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#80000 numeros
tiempoInicio=time.time()
burbuja(arr,80000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#90000 numeros
tiempoInicio=time.time()
burbuja(arr,90000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

#100000 numeros
tiempoInicio=time.time()
burbuja(arr,100000)
tiempoFinal=time.time()
tiempoTotal.append((tiempoFinal-tiempoInicio)*1000)

print("el tiempo de ordenamiento de 100 numeros aleatorios es ",tiempoTotal[0]," milisegundos")
print("el tiempo de ordenamiento de 500 numeros aleatorios es ",tiempoTotal[1]," milisegundos")
print("el tiempo de ordenamiento de 1000 numeros aleatorios es ",tiempoTotal[2]," milisegundos")
print("el tiempo de ordenamiento de 2000 numeros aleatorios es ",tiempoTotal[3]," milisegundos")
print("el tiempo de ordenamiento de 3000 numeros aleatorios es ",tiempoTotal[4]," milisegundos")
print("el tiempo de ordenamiento de 4000 numeros aleatorios es ",tiempoTotal[5]," milisegundos")
print("el tiempo de ordenamiento de 5000 numeros aleatorios es ",tiempoTotal[6]," milisegundos")
print("el tiempo de ordenamiento de 6000 numeros aleatorios es ",tiempoTotal[7]," milisegundos")
print("el tiempo de ordenamiento de 7000 numeros aleatorios es ",tiempoTotal[8]," milisegundos")
print("el tiempo de ordenamiento de 8000 numeros aleatorios es ",tiempoTotal[9]," milisegundos")
print("el tiempo de ordenamiento de 9000 numeros aleatorios es ",tiempoTotal[10]," milisegundos")
print("el tiempo de ordenamiento de 10000 numeros aleatorios es ",tiempoTotal[11]," milisegundos")
print("el tiempo de ordenamiento de 20000 numeros aleatorios es ",tiempoTotal[12]," milisegundos")
print("el tiempo de ordenamiento de 30000 numeros aleatorios es ",tiempoTotal[13]," milisegundos")
print("el tiempo de ordenamiento de 40000 numeros aleatorios es ",tiempoTotal[14]," milisegundos")
print("el tiempo de ordenamiento de 50000 numeros aleatorios es ",tiempoTotal[15]," milisegundos")
print("el tiempo de ordenamiento de 60000 numeros aleatorios es ",tiempoTotal[16]," milisegundos")
print("el tiempo de ordenamiento de 70000 numeros aleatorios es ",tiempoTotal[17]," milisegundos")
print("el tiempo de ordenamiento de 80000 numeros aleatorios es ",tiempoTotal[18]," milisegundos")
print("el tiempo de ordenamiento de 90000 numeros aleatorios es ",tiempoTotal[19]," milisegundos")
print("el tiempo de ordenamiento de 100000 numeros aleatorios es ",tiempoTotal[20]," milisegundos")

