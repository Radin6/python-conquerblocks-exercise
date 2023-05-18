'''REPITE LOS CARACTÉRES:
Crea un script que acepte un string de 5 caracteres y devuelva otro string con todos los caracteres
duplicados. Si el input es ‘sbc56’, el output deberá ser ‘ssbbcc5566’'''

texto = str(input('Escribe un texto de cinco carácteres '))
for i in texto: 
   print(i+i,end ="")