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
from programasPoo.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
  
  '''constructor'''
  def __init__(self, pinones):
    super().__init__()
    self.pinones=pinones
  
  '''metodo vacio.
   * 
   * hace un caballito la bicicleta
  '''
  def hazCaballito(self):
    print("Estoy haciendo el caballito") 
    