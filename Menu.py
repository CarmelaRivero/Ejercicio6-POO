from ClaseMenu import menu
from ListasViajero import ListasViajero
from Clase import Viajero
import csv
if __name__ == "__main__":
    lista=ListasViajero()
    archivo=open('C:\\Users\\csv\\archivo_viaj.csv',"r")
    reader=csv.reader(archivo,delimiter=";")
    print(reader)
    for fila in reader:
        viajero=Viajero(int(fila[0]), fila[1], fila[2] ,fila[3], int(fila[4]))
        lista.crearviajero(viajero)
        
    archivo.close()
    Menu=menu()
    op=None
    
    while(op!=4):
        print("|---------------------------------------------------|")
        print("| Ingresar 1 para Consultar Cantidad de Millas      |")
        print("| Ingresar 2 para Acumular Millas                   |")
        print("| Ingresar 3 para Canjear Millas                    |")
        print("| Ingresar 4 para Mayor cantidad de millas acumulada|")
        print("| Ingresar 5 para salir                             |")
        print("|---------------------------------------------------|")
        op=int(input("ingresar opcion: "))
        num=int(input("ingresar numero de viajero frecunte "))
        Menu.opcion(op,lista,num)