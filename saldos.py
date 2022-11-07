"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. Construye 
los siguientes métodos para la clase: 

- Un constructor.
- mostrar(): Muestra los datos de la cuenta. 
- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos
"""

class Cuenta:
  def __init__(self, titular, cantidad):
    self.titular = titular
    self.cantidad = cantidad

  def mostrar(self):
    print("Titular: ", self.titular)
    print("Cantidad: $", self.cantidad)
  
  def ingresar(self, cantidad):
    self.cantidad += cantidad
    print("Se ingreso $", cantidad)
    print("Monto tolal: $", self.cantidad)

  def retirar(self, cantidad):
    self.cantidad -= cantidad
    if (self.cantidad >= 0):
      print("Se retiro: $", cantidad)
      print("Monto tolal: $", self.cantidad)
    else:
      print("Se retiro: $", cantidad)
      print("Usted tiene una deuda de: $", self.cantidad)

user1 = Cuenta("Maxi", 1000)
user1.retirar(1200)
print()
user1.ingresar(300)
print()
user1.mostrar()