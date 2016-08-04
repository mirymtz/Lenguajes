# Lenguajes
Lenguajes de mi profesor favorito polanco
#Miguel Serrano Ramirez
#Juan Lopez Rodriguez
#Juan Manuel Vera Martinez
#Miguel Angel Toledo Ibarra
#Victor Manuel Rojas Rojas
#Miriam Romero Martinez
#------------------------------------------------------------------------------
entrada = input ("Ingrese cadena (ejemplo: aba*b*)-->")
diccionario={              
       (1,'a'):2,
       (1,'b'):6,
       (2,'b'):3,
       (2,'a'):6,
       (3,'a'):4,
       (3,'b'):5,
       (4,'a'):4,
       (4,'b'):5,
       (5,'b'):5,
       (5,'a'):6,
       (6,'b'):6,
       (6,'a'):6}
estadoA=[3]  
estadoB=[4]  
estadoC=[5]
#------------------------------------------------------------------------------
def reco(letrita, resul, diccionario, estadoA):
    if letrita == "":
        return resul in estadoA 
    else:
        letra= letrita[0] 
        if(resul,letra)in diccionario: 
            letraen=diccionario[(resul,letra)]
            remaining_string=letrita[1:]
            return reco(remaining_string,letraen,diccionario,estadoA)
        else:
            return False
cadena =(reco(entrada,1,diccionario,estadoA))
#------------------------------------------------------------------------------
def reco(letrita, resul, diccionario, estadoB):
    if letrita == "":
        return resul in estadoB
    else:
        letra= letrita[0] 
        if(resul,letra)in diccionario: 
            letraen=diccionario[(resul,letra)]
            remaining_string=letrita[1:]
            return reco(remaining_string,letraen,diccionario,estadoB)
        else:
            return False
cadena1 =(reco(entrada,1,diccionario,estadoB))
#------------------------------------------------------------------------------
def reco(letrita, resul, diccionario, estadoC):
    if letrita == "":
        return resul in estadoC
    else:
        letra= letrita[0] 
        if(resul,letra)in diccionario: 
            letraen=diccionario[(resul,letra)]
            remaining_string=letrita[1:]
            return reco(remaining_string,letraen,diccionario,estadoC)
        else:
            return False
cadena2 =(reco(entrada,1,diccionario,estadoC))
#-----------------------------------------------------------------------------
if cadena == False and cadena1 == False and cadena2 == False:
    print ("NO ACEPTADA")
else:
    print ("ACEPTADA")
#------------------------------------------------------------------------------


