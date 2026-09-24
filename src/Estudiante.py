from validaciones import ValidarEntero,ValidarFlotante
Cursos = [
    {
        "codigo": 2559101,
        "nombre": "Algebra y Trigonometria",
        "creditos": 3,
        "nivel": 1
    },

    {
        "codigo": 2559121,
        "nombre": "Geometria Vectorial y Analitica",
        "creditos": 3,
        "nivel": 1
    },

    {
        "codigo": 2559131,
        "nombre": "Calculo Diferencial",
        "creditos": 3,
        "nivel": 1
    },

    {
        "codigo": 2559221,
        "nombre": "Algebra Lineal",
        "creditos": 3,
        "nivel": 2
    },

    {
        "codigo": 2559231,
        "nombre": "Calculo Integral",
        "creditos": 3,
        "nivel": 2
    }
]
UsuarioLogueado={'Nombre':'crilin',
               'Edad':30,
               'Pin':34566543,
               'Clave':'ukog567',
               'Rol':'ESTUDIANTE'}
def listarCursos(Cursos):
    for curso in Cursos:
        print('-'*50)
        print(f'Codigo:{curso['codigo']}')
        print(f'Nombre:{curso['nombre']}')
        print(f'Creditos: {curso['creditos']}')
        print('-'*50)
def BuscarCursoCodigo(codigo):
    print('Entro a buscar el codigo')
    for curso in Cursos:
        if curso["codigo"]==codigo:
            print(curso["codigo"])
            return curso
    return None


def MatricularCurso(UsuarioLogueado):
    listarCursos(Cursos)
    #DEbe listar los cursos, y preguntarle al estudiante que curso va a matricular, que ingrese el codigo, 
    #verificar si el codigo ingresado 
    # existe y realizar la matricula si no exite el codigo ingresado indicar que el codigo no es valido.
    CodigoCursoMat=ValidarEntero('Ingresa el codigo del curso a matricular')
    Cursoingresado=BuscarCursoCodigo(CodigoCursoMat)
    #print(Cursoingresado)
    if Cursoingresado is None:
        print('el codigo ingresado no es valido')
    else:
        print('Curso Matriculado Correctamente.')


MatricularCurso(UsuarioLogueado)
