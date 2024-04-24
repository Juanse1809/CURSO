class Curso:
    """------------------------
    #Atributos
    ---------------------------"""

    notas = [4, 5, 3, 2, 3.5, 1, 3.5, 4, 3.5, 5, 4.5, 4.2]

    """------------------------
    #Metodos
    ---------------------------"""
    def __init__(self):
        self.__notas = [4, 5, 3, 2, 3.5, 1, 3.5, 4, 3.5, 5, 4.5, 4.2]


    def numeroDeArreglos (Self):
        numeroDeArreglos = len (Self.notas)
        return numeroDeArreglos
    
    def promedio (self):
        suma = 0.0
        indice = 0

        while indice < 12:
            suma = suma + self.__notas[indice]
            indice = 1 

    def calcularCantidadAprobados(Self):
        aprobados = 0
        indice = 0

        while indice < 12:
            if (Self.__notas[indice]>=3)and(Self.__notas[indice]<=5):
                aprobados += 1
        return aprobados
    
    def calcularCantidadAprobados(self):
        aprobados = 0
        
        for indice in range(12):
            if (self.__notas[indice]>=3)and(self.__notas[indice]<=5):
                aprobados += 1
        return aprobados

    def calcularCantidadAprobados3(Self):
        aprobados = 0
        for nota in Self.__notas:
            if nota >= 3.0 and nota <= 5.0:
                aprobados+=1 
        return aprobados
    
    def MayorNota (self):
        mayor = 0
        for nota in self.__notas:
            if nota > mayor:
                mayor = nota 
        return mayor
    
    def hacerCurva (self):
        indice = 0 
        while indice < 12:
            if self.notas[indice]<=4.75:
               self.notas[indice]*=1.05
               indice *= 1
               return self.notas 
                 
    def HayAlgunCinco_uno(self):
        i=0
        hayCinco = False
       
        while (i< len(self.__notas)) and not hayCinco:
            if (self.__notas[i] == 5):
                hayCinco = True
            i += 1

        return hayCinco
    
    def HayAlgunCinco_dos(self):
        hayCinco = False

        for i in range(len(self.__notas)):
            if (self.__notas[i] == 5):
                hayCinco = True
                break
        
        return hayCinco
    
    def HayAlgunCinco_tres (self):
        hayCinco = False
        for nota in self.__notas:
            if nota == 5:
                hayCinco = True
                break

        return hayCinco
    
                          