import os
import subprocess
from subprocess import Popen

def obtener_alumnos():
    lista=[]
    with open("salida.txt", mode="r", encoding="utf-8") as archivo:
         for a in archivo:
              #print(a)
              lista.append(a.strip())
         print(lista)
         return lista


def setPassword(userName:str, password:str):
    p = Popen([ "/usr/sbin/chpasswd" ], universal_newlines=True, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate(userName + ":" + password + "\n")
    assert p.wait() == 0
    if stdout or stderr:
        raise Exception("Error encountered changing the password!")

def eliminar_usuarios(lista:list):
    #lista=["daniela", "Carolina", "Liz"]
    for a in lista:
       os.system("userdel -r {}".format(a))
       print("eliminando usuario: {}".format(a))

def crear_usuarios(lista:list):
        #lista=["danielarodriguez","carolina", "liz"]
        for a in lista:
             os.system("useradd {}".format(a))
             setPassword(a, 'aws1234')
             print("usuari@: {}  Cread@!".format(a))

if __name__=="__main__":
      print("Hola mundo")
      url="/home/edgardo/codigos/python/alumnos.txt"
      with open(url, mode="a") as archivo:
          archivo.write("usuario:{}".format("Edgardo"))
      os.system("clear")
      lista=obtener_alumnos()
      print("hay {} alumnos".format(len(lista)))
      #crear_usuarios(lista)
      eliminar_usuarios(lista)
      print("Fin del programa")

