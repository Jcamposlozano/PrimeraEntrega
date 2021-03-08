from Servidor import *


class Operaciones():
    
    servidor = Servidor()

    def menu(self):
        trm = self.servidor.indicadoresEconomicos()
        print("*************************************")
        print("TRM DEL DIA", trm)
        print("*************************************")
        while True:
            print("1. Pesos - Dolares")
            print("2. Dolares - Pesos")
            print("3. Salir")
            operacion = input("Opcion : ")
            respuesta = 0
            if operacion == "1":
                valor = input("Ingrese en pesos : ")
                respuesta = float(valor) / float(trm)
                print("\n\n" , "Valor convertido ", respuesta , "\n\n")
            elif operacion == "2":
                valor = input("Ingrese en dolares : ")
                respuesta = float(trm) * float(valor)
                print ("\n\n", "Valor convertido ",respuesta,"\n\n")
            else:
                print("Salir")
                break
        
 
