'''
Crea la clase Tiempo con los métodos suma y resta. Los objetos de la clase Tiempo
son intervalos de tiempo y se crean de la forma Tiempo t = new Tiempo(1, 20,
30) donde los parámetros que se le pasan al constructor son las horas, los
minutos y los segundos respectivamente. Crea el método toString para ver los
intervalos de tiempo de la forma 10h 35m 5s. Si se suman por ejemplo 30m 40s y
35m 20s el resultado debería ser 1h 6m 0s. Realiza un programa de prueba para
comprobar que la clase funciona bien.

@author: Rafael Infante
'''

class Tiempo:
  
  '''Constructor'''
  def __init__(self,horas,minutos,segundos):
    self.horas=horas
    self.minutos=minutos
    self.segundos=segundos
  
  '''Metodo que suma
   * 
   * @param: objeto 
   * @return: objeto
  '''
  def suma(self,tiempo):
    self.horas= self.horas+tiempo.horas
    self.minutos=self.minutos+tiempo.minutos
    self.segundos=self.segundos+tiempo.segundos
    
    if self.minutos>=60:
      self.horas+=1
      self.minutos-=60
    
    if self.segundos>=60:
      self.minutos+=1
      self.segundos-=60
  
  '''Metodo que suma
   * 
   * @param: objeto 
   * @return: objeto
  '''
  def resta(self,tiempo):
    self.horas= self.horas-tiempo.horas
    self.minutos=self.minutos-tiempo.minutos
    self.segundos=self.segundos-tiempo.segundos
    
    if self.minutos>=60:
      self.horas+=1
      self.minutos-=60
    
    if self.segundos>=60:
      self.minutos+=1
      self.segundos-=60
    
  #return tiempo(horas,minutos,segundos)
  
  def __str__(self):
    cadena="Tiempo [hora=" + str(self.horas) +", min=" + str(self.minutos) + ", seg=" + str(self.segundos) + "]"
    return cadena
    