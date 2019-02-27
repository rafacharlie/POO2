'''
Crea la clase Vehiculo, así como las clases Bicicleta y Coche como subclases de
la primera. Para la clase Vehiculo, crea los atributos de clase vehiculosCreadosy
kilometrosTotales, así como el atributo de instancia kilometrosRecorridos. Crea
también algún método específico para cada una de las subclases. Prueba las
clases creadas mediante un programa con un menú como el que se muestra
a continuación:

VEHÍCULOS
=========
1. Anda con la bicicleta
2. Haz el caballito con la bicicleta
3. Anda con el coche
4. Quema rueda con el coche
5. Ver kilometraje de la bicicleta
6. Ver kilometraje del coche
7. Ver kilometraje total
8. Salir
Elige una opción (1-8):

@author: Rafael Infante
'''

class Vehiculo:
  
  kilometrosTotales=0
  vehiculosCreados=0
  
  '''constructor'''
  def __init__(self):
    self.kilometrosRecorridos=0;
  
  '''metodos getter'''
  def getKilometrosRecorridos(self):
    return self.kilometrosRecorridos
  
  def getKilometrosTotales(self):
    return Vehiculo.kilometrosTotales
  
  '''*Metodo:
   * Hace que un vehículo recorra una distancia determinada.
   * 
   * Cuando un vehículo recorre una distancia k, se
   * incrementan su propio cuentakilómetros, es decir, su atributo
   * kilometrosRecorridos y también se incrementa la cuenta
   * global de kilómetros que recorren todos los vehículos, es decir, el
   * atributo de clase kilometrosTotales.
   *
   * @param k kilómetros a recorrer
   '''
  def recorre(self,k):
    self.kilometrosRecorridos+= k
    Vehiculo.kilometrosTotales+=k
  