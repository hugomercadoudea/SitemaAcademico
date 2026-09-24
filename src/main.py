from autenticacion import logeo
from menus.menuadmin import Menuadmin
from menus.menudocente import MenuDocente
from menus.menuestudiante import MenuEstudiante
def Main():
  usuarios = [{'Nombre':'Goku',
               'Edad':30,
               'Pin':34566543,
               'Clave':'ukog567',
               'Rol':'ADMIN'},
              {'Nombre':'crilin',
               'Edad':30,
               'Pin':34566543,
               'Clave':'ukog567',
               'Rol':'ESTUDIANTE'},
              {'Nombre':'vegeta',
               'Edad':30,
               'Pin':34566543,
               'Clave':'ukog567',
               'Rol':'DOCENTE'}]
  UsuarioLogueado,Estado=logeo(usuarios)
  if Estado==1:
    if UsuarioLogueado['Rol'] == "ADMIN":
      usuarios=Menuadmin(usuarios)
    elif UsuarioLogueado['Rol'] == "ESTUDIANTE":
      MenuEstudiante()
    elif UsuarioLogueado['Rol'] == "DOCENTE":
      MenuDocente()
  elif Estado==2:
    print("El usuario no existe.")
  elif Estado==3:
    print("Contraseña invalada. :()")
Main()