from validaciones import ValidarEntero
def MenuDocente():
  print('Opciones del menu:')
  print('   1. Ver Cursos Asignados')
  print('   2. Ingresar Notas')
  print('   3. Listar Estudiantes')
  print('   4. Salir')
  Opcion=ValidarEntero('Ingrese una opcion: ')
  if Opcion == 1:
    print("Ver Cursos Asignados")
  elif Opcion == 2:
    print("Ingresar Notas")
  elif Opcion == 3:
    print("Listar Estudiantes")
  elif Opcion == 4:
    print("Saliendo del Menu Docente")
  else:
    print("Opcion invalida. Vuelve e intente")