'''
Implementa la clase Movil como subclase de Terminal (la clase del ejercicio
anterior que ya no hace falta modificar). Cada m?vil lleva asociada una tarifa
que puede ser �rata�, �mono� o �bisonte�. El coste por minuto es de 6, 12 y
30 c?ntimos respectivamente. Se tarifican los segundos exactos. Obviamente,
cuando un m?vil llama a otro, se le cobra al que llama, no al que recibe la
llamada. A continuaci?n se proporciona el contenido del main y el resultado
que debe aparecer por pantalla. Para que el total tarificado aparezca con dos
decimales, puedes utilizar DecimalFormat.
Contenido del main
Movil m1 = new Movil("678 11 22 33", "rata");
Movil m2 = new Movil("644 74 44 69", "mono");
Movil m3 = new Movil("622 32 89 09", "bisonte");
System.out.println(m1);
System.out.println(m2);
m1.llama(m2, 320);
m1.llama(m3, 200);
m2.llama(m3, 550);
System.out.println(m1);
System.out.println(m2);
System.out.println(m3);
Salida
N? 678 11 22 33 - 0s de conversaci?n - tarificados 0,00 euros
N? 644 74 44 69 - 0s de conversaci?n - tarificados 0,00 euros
N? 678 11 22 33 - 520s de conversaci?n - tarificados 0,52 euros
N? 644 74 44 69 - 870s de conversaci?n - tarificados 1,10 euros
N? 622 32 89 09 - 750s de conversaci?n - tarificados 0,00 euros

@author: Rafael Infante
'''
from programasPoo.Terminal import Terminal

class Movil(Terminal):
  
  tarificados=0
  
  '''constructor'''
  def __init__(self, numero, tarifa):
    super().__init__(numero)
    self.tarifa=tarifa
    
  '''
  Mirar este metodo como se sobreescribe en el pildoras
  '''
  def llama(self,terminal,segundosLlamada):
    Terminal.llama(self, terminal, segundosLlamada)
   #super().__init__(terminal,segundosLlamada)
    min=segundosLlamada/60
    
    if self.tarifa=="rata":
      self.tarificados=min*0.06
    elif self.tarifa=="mono":
      self.tarificados=min*0.12
    elif self.tarifa=="bisonte":
      self.tarificados=min*0.30
  
  '''
  Metodo toString 
    
  @return String
  '''
  def __str__(self):
    cadena="Nº" + str(self.getNumero()) + " - " + str(self.gettiempoConversacion()) + " s de conversacion" + " - tarificados " + str("{0:.2f}".format(self.tarificados)) + " euros."
    return cadena
  
    

