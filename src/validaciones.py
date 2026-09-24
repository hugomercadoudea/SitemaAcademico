#Validacion de numeros Enteros, garantizando que si ingresan texto no se genere error.
def ValidarEntero(mensaje):
 while True:
  try:
    valor = int(input(mensaje))
    return valor
  except ValueError:
    print("Debe ingresar un numero entero, no aceptamos Caracteres!!!")

#Validacion de numeros Enteros, garantizando que si ingresan texto no se genere error.
def ValidarFlotante(mensaje):
 while True:
  try:
    valor = float(input(mensaje))
    return valor
  except ValueError:
    print("Debe ingresar un numero entero, no aceptamos Caracteres!!!")