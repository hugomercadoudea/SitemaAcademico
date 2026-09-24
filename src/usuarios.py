from validaciones import ValidarEntero
def RegistrarUsuario(usuarios):
  print("Registrando usuario")
  nombre = input("Ingrese nombre de usuario: ")
  Edad= ValidarEntero("Ingrese edad: ")
  PIN = ValidarEntero("Ingrese PIN numerico: ")
  clave = input("Ingrese clave")
  rol = input("Ingrese rol: (Admin-Estudiante-Docente) ").upper()
  usuarios.append({'Nombre':nombre,'Edad':Edad,'Pin':PIN,'Clave':clave,'Rol':rol})
  print(f"-> ¡Usuario '{nombre}' registrado con éxito!")
  return usuarios

def ListarUsuarios(usuarios):
  print("Listando usuarios registrados")
  for usuario in usuarios:
    print(f"Nombre: {usuario['Nombre']}, Edad: {usuario['Edad']}, PIN: {usuario['Pin']}, Clave: {usuario['Clave']}, Rol: {usuario['Rol']}")
