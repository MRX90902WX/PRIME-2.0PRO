import sys
from random import randint
from os import system
import datetime                              
import random

print("") 
print(" \033[1;31mBY: \033[1;32mD³M⁰")
print(" \033[1;32m≧◉◡◉≦")
print("")
system("sleep 1")
print("")
print(" \033[1;31m-----> \033[1;34mBIN 552490 \033[1;31m<------")
system("sleep 2")

cantidad = input(" \033[1;37mGen: ")
print("")
print(" \033[1;31m------------------------------------")
print("        \033[1;36mBIN       | FECHA |  STATUS |")
print(" \033[1;31m------------------------------------")

bin_format = "55249036xxxx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 12:
    for i in range(11):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc

def dategen():
  now = datetime.datetime.now()                            
  date = ""                                                                  
  month = str(randint(3, 8))
  current_year = str(now.year)                                               
  year = str(random.randint(23, 28))
  date = month + "/" + year

  return date


def main():
  for i in range(int(cantidad)):                
    cc = generar_cc(bin_format)
    f = open('BIN-CA.txt', "a+")
    f.write(f'{cc}xxxx | {dategen()}  | APROVED\n')
    f.close()
    print(f" \033[1;37m{cc}xxxx \033[1;36m| \033[1;37m{dategen()}  \033[1;36m| \033[1;37mAPROVED \033[1;36m|")
main()

print("")
system("cat dir2.txt")
print("")

num = input("Desea generar el Tlf (y/n): ")

if num == "y":
   system("python num2.py")
else:
   exit()
