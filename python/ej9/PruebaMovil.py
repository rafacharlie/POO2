'''
Prueba de la clase movil

@author: Rafael Infante
'''
from programasPoo.Movil import Movil

'''
instancias
'''
m1=Movil("663654985","rata") #0.06
m2=Movil("664665063","bisonte") #0.12
m3=Movil("66512972","mono") #0.30

'''print(m1)
print(m2)
print(m3)'''

m1.llama(m2, 1989);
m2.llama(m1, 2365);
m3.llama(m1, 2369)

print(m1)
print(m2)
print(m3)



