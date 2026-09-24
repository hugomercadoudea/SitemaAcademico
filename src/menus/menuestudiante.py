from validaciones import ValidarEntero
def MenuEstudiante():
  Opcion=1
  while Opcion!=5:
    print('Opciones del menu:')
    print('   1. Matricular Curso')
    print('   2. Listar Cursos Matriculados')
    print('   3. Ver notas')
    print('   4. Cancelar Curso')
    print('   5. Salir')
    Opcion=ValidarEntero('Ingrese una opcion: ')
    if Opcion == 1:
      print("Matricular Curso")
    elif Opcion == 2:
      print("Listar Cursos Matriculados")
    elif Opcion == 3:
      print("Ver notas")
    elif Opcion == 4:
      print("Cancelar Curso")
    elif Opcion == 5:
      print("Saliendo del Menu Estudiantes")
    else:
      print("Opcion invalida. Vuelve e intente")