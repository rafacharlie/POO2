'''
Implementa la clase Terminal. Un terminal tiene asociado un número. Los
terminales se pueden llamar unos a otros y el tiempo de conversación corre
para ambos. A continuación se proporciona el contenido del main y el resultado
que debe aparecer por pantalla.
Contenido del main
Terminal t1 = new Terminal("678 11 22 33");
Terminal t2 = new Terminal("644 74 44 69");
Terminal t3 = new Terminal("622 32 89 09");
Terminal t4 = new Terminal("664 73 98 18");
System.out.println(t1);
System.out.println(t2);
t1.llama(t2, 320);
t1.llama(t3, 200);
System.out.println(t1);
System.out.println(t2);
System.out.println(t3);
System.out.println(t4);
Salida
Nº 678 11 22 33 - 0s de conversación
Nº 644 74 44 69 - 0s de conversación
Nº 678 11 22 33 - 520s de conversación
Nº 644 74 44 69 - 320s de conversación
Nº 622 32 89 09 - 200s de conversación
Nº 664 73 98 18 - 0s de conversación

@author: Rafael Infante
'''

class Terminal:
  
  '''constructor'''
  def __init__(self,numero):
    self.numero=numero
    self.tiempoConversacion=0
  
  '''setters'''
  def setNumero(self,numero):
    self.numero=numero
  
  def setTiempoConversacion(self,tiempoConversacion):
    self.tiempoConversacion=tiempoConversacion
  
  '''getters'''
  def getNumero(self):
    return self.numero
  
  def gettiempoConversacion(self):
    return self.tiempoConversacion
  
  '''
  metodo vacio llama. Para que se le asigne el tiempo de conversacion a los 2 terminales.
   * 
   * @param: instancia, otro telefono.
   * @param: tiempo en segundos
  '''
  def llama(self,terminal,segundosLlamada):
    self.tiempoConversacion+=segundosLlamada
    terminal.tiempoConversacion+=segundosLlamada
  
  '''
  metodo toString vacio devuelve una cadena.
  '''
  def __str__(self):
    return "Terminal [numero=" + str(self.numero) + ", tiempoConversacion=" + str(self.tiempoConversacion) + "]";
    
    
    
