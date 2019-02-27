'''
Prueba de la clase vehiculos

@author: Rafael Infante
'''

from programasPoo.Bicicleta import Bicicleta
from programasPoo.Coche import Coche

'''
Funcion vacia que muestra un menu
'''
def mostrarMenu():
  print("\t\tMENU")
  print("\t\t====\n")
  print("1. Anda con la bicicleta")
  print("2. Haz el caballito con la bicicleta")
  print("3. Anda con el coche")
  print("4. Quema rueda con el coche")
  print("5. Ver kilometraje de la bicicleta")
  print("6. Ver kilometraje del coche")
  print("7. Ver kilometraje total")
  print("8. Salir")
  print("Elige una opción (1-8): ")

'''instancias'''
miBicicleta=Bicicleta(7)
miCoche=Coche(1400)

'''programa'''

#variables
opcion = 0;
km=0

while opcion != 8:
  print()
  mostrarMenu()
  opcion = int(input())
  if opcion==1:
    print("¿Cuántos kilómetros quiere recorrer en bici? ")
    km = int(input())
    miBicicleta.recorre(km)
    #break;
  if opcion==2:
    miBicicleta.hazCaballito()
    #break;
  if opcion==3:
    print("¿Cuántos kilómetros quiere recorrer en coche? ")
    km = int(input())
    miCoche.recorre(km)
    #break;
  if opcion==4:
    miCoche.quemaRueda()
    #break
  if opcion==5:
    print("La bicicleta lleva recorridos ")
    print(miBicicleta.getKilometrosRecorridos() , " Km")
    #break
  if opcion==6:
    print("El coche lleva recorridos ")
    print(miCoche.getKilometrosRecorridos() , " Km")
    #break;
  if opcion==7:
    print("Los vehículos llevan recorridos ")
    print(miCoche.getKilometrosTotales() , " Km")
    