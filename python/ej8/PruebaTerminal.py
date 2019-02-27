'''
Prueba de la clase terminal.

@author: Rafael Infante
'''
from programasPoo.Terminal import Terminal

t1=Terminal("663654985")
t2=Terminal("703644864")
t3=Terminal("713654464")

t1.llama(t2, 340)
t1.llama(t3,500)

print(t1)
print(t2)
print(t3)