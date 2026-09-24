from usuarios import RegistrarUsuario
def logeo(usuarios):
  #Diferentes Escenarios al momento de ingresar a un siste:  Diego
  #1 Uruario No existe
  #2 Contraseña Invalada
  #3 preguntar si desea registrarse.
  nombre = input("Ingrese usuario: ")
  clave = input("Ingrese clave: ")
  usuario_encontrado ={}
  existe_usuario = False
  for usuario in usuarios:
    if usuario['Nombre'] == nombre:
      existe_usuario = True
      usuario_encontrado = usuario
      break
  if existe_usuario == False:
    print("El usuario no existe.")
    opcion = input("¿Desea registrarse? (si/no): ")
    if opcion == "si":
      RegistrarUsuario(usuarios)
    return usuario_encontrado,2
  elif usuario_encontrado['Clave'] != clave:
    print("Contraseña invalada.")
    return usuario_encontrado,3
  else:
    print(f"Bienvenido al sistema {nombre}.")
    return usuario_encontrado,1