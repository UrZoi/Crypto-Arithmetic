#!/usr/bin/python
#-*-coding: utf-8-*-


'''Criptoaritmetica
   
   SEND +   eso es igual a esto---->    9567 +
   MORE					1085
 -------			      -------
  MONEY				       10652
  
  Cada una de las letras tiene un valor numerico,
  La operacion no puede comenzar con 0
  
  Notas:
  Tiene que tener listas dividir la lista y asignar un valor a cada letras
  Se tiene que seguir un orden como el alfabetico 
  
  El acertijo contiene solo digitos y representa una suma correcta
  
  idea al final hacer un while dentro de este un if que pregunte si la palabra1 + la palabra2 = a la palabra3 si esto no es cirto entonces que agregue el arrelo de numeros a una lista
  de numeros los cuales no son validos que se generen nuevoos numeros a partir de ahi y asi sucesivamente hasta que se cumpla la sentencia xD
   
   
   1,2,3,4,5,6,7,8,9
   
   a,b,c,d,e,f,g,h,i
   
  
  '''
import random
import itertools 
n=False

def Letras_Usar(palabra1,palabra2,palabra3):
  lista=[]
  for i in range(len(palabra1)):
   lista.append(palabra1[i])
  for i in range(len(palabra2)):
   lista.append(palabra2[i])
  for i in range(len(palabra3)):
   lista.append(palabra3[i])  
  
  return lista

#E,D,M,O,N,S,R,Y
#S,E,N,D,M,O,R,Y

def cnum(numList):
    s = ''.join(map(str, numList))
    return int(s)
  
def Asignar_Numeros(p1,p2,p3,palabras):
  palabras2 = list(set(palabras))
  print(palabras2)
  lista_num=[]
  lista_p1=[]
  lista_p2=[]
  lista_p3=[]
  l1n=[]
  l2n=[]
  l3n=[]
  
  for i in range(len(p1)):
   lista_p1.append(p1[i])
  for i in range(len(p2)):
   lista_p2.append(p2[i])
  for i in range(len(p3)):
   lista_p3.append(p3[i])  
   
  
  print(palabras2)
  d= dict(zip(palabras2,lista_num))

  lista =[]
  digits=range(10)
  for perm in itertools.permutations(digits, len(palabras2)):
    lista.append(list(perm))
  
  print(len(lista))
  verdadero = False
  i=0
  while verdadero == False:
        l1n=[]
	l2n=[]
	l3n=[]
	lista_num = lista[i]
	d = dict(zip(palabras2,lista_num))
	for j in range(len(lista_p1)):
	  l1n.append(d[lista_p1[j]])
	for j in range(len(lista_p2)):
	  l2n.append(d[lista_p2[j]])
	for j in range(len(lista_p3)):
	  l3n.append(d[lista_p3[j]])
	#print(l1n," + ",l2n," = ",l3n)
	if l1n[0] != 0 and l2n[0] != 0 :
	  send= cnum(l1n)
	  more= cnum(l2n)
	  money= cnum(l3n)
	  res = send + more
	  if res == money:
	    verdadero = True
	    print (send,"+ ",more," = ",money)
	i = i+1

  
      

    
  return lista_num

  
dd= "more"    
lol="money"
xD= "send"  

letras = Letras_Usar(xD,dd,lol)

print(letras)
Asignar_Numeros(xD,dd,lol,letras)




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       