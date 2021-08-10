import random as ra #Importa librerias
import numpy as np
#TODO ESTE CODIGO ES DIDACTICO
#Tomar como ejemplo para ver la sintaxis de python

class planilla:   #Define una clase 
    "Las clases proveen una forma de empaquetar datos y funcionalidad juntos.\
    Al crear una nueva clase, se crea un nuevo tipo de objeto, permitiendo crear \
    nuevas instancias de ese tipo. Cada instancia de clase puede tener atributos \
    adjuntos para mantener su estado. Las instancias de clase también pueden tener\
    métodos (definidos por su clase) para modificar su estado  . \
     En Python todo es un objeto. Cuando creas una variable y le   \
     asignas un valor entero, ese valor es un objeto; una función es un objeto;\
     las listas, tuplas, diccionarios, conjuntos, … son objetos; \
     una cadena de caracteres es un objeto. "
    
    
    
    
    "En este caso esta clase crea objetos que tienen un diccionario como variable global \
     planilla.Planilla_ "
    "planilla.crear_planilla() es un metodo para cargar Planilla_ a mano"
    "etc.."
#    Planilla_ ={'':[]}
    def __init__(self,*arg):
        planilla.Planilla_ = dict({'':[]})
        self.Planilla_ = dict(*arg)
        print ("iniciando: "+str(self.Planilla_))
    
    def crear_planilla(self): #define función
        planilla.Planilla_={}
        numKeys=int(input('Cantidad de Alumnos: ')) #numeros de llaves del diccionario que devuelve
        for nameValuePair in range(numKeys):
            key = input("Nombre completo: ") # la llave puede ser el ALIAS o Nom. Comp.
            valList = [] #utiliza un vector y lo define.
            valList.append(input("alias: ")) # al vector le va agregando "valores"
            valList.append(input("Correo: ")) #se puede poner dentro de un loop.
#           valList.append(input("sim, calc o prog"))
            planilla.Planilla_[key] = valList #el vector["LISTA"] es el valor vinculado a la llave 
##___________________________________________________________________

    def guardar_planilla(self):
        "Guarda en un archivo .txt la planilla (diccionario) de forma directa."
    # open file for writing
        f = open(input("nombre")+".txt","w") #Abre eel archivo txt y habilita escribir "w"
    # write file
        f.write(str(self.Planilla_)) #escribe en f = (file.txt) el string del diccionario  
    # close file
        f.close()
        
    def abrir_planilla(self):
        "Abrir el archivo .txt que se guardo el diccionario"
        self.Planilla_ = dict
        f = open(input("nombre")+'.txt', 'rt') 
        self.Planilla_ = eval(f.read())
        f.close()
    
    def abrir_datos(self): # nombre, alias, correo
        "Abrir un archivo que tiene guardada la info [key], [Val[0]],[Val[1] ... ]"
        vec =[]
        dicc = {}
        f = open(input("nombre")+'.txt', 'rt') 
        for line in f:
            vec=line.strip('\n').split(', ')
            dicc[str(vec[0])]=list(vec[1:])
        f.close()
        print(dicc)
        self.Planilla_=dict(dicc)  
##___________________________________________________________________
  
    def buscar_alia(self,alias):
        "busca en el diccionario el alias=value[0] donde [key:value] value=[value[0],...]"
        for key, value in self.Planilla_.items(): #bucle for  donde i = [key, value] dentro de [k,v]=planilla_.items()
            if (alias) == (value[0]):
                return key
        return "no existe registro"

    def buscar_valor(self,palabra_,index_):
        "busca en el diccionario cualquier pablra dentro de value[index_], \ 
        hay que indicarle el index_ \
        donde index_=0 -> alias ; index_=1 -> Correo"
        for key, value in self.Planilla_.items():
            if palabra_ == value[index_]:
                return key
        return "no existe registro"
    
    def crear_lista(self):
        "Crea una lista con los ALIAS"
        participantes_= []
        for key, value in self.Planilla_.items():
             participantes_.append(str(value[0])) 
        self.Participantes_=participantes_
        return self.Participantes_
    
    def llamar(self):
        "Crea una lista con participantes, elije al ganador y \
        devuelve una lista de participantes sin el ganador"
        self.llamar_a=ra.sample(self.Participantes_,1)[0]
        self.Participaron_=list(self.Participantes_)
        self.Participantes_.remove(self.llamar_a)
        return [self.Participaron_ , self.llamar_a , self.Participantes_]
    
    def crear_grupo(self, cant_):
        "crear_grupo(cant_) crea una cant_ de grupos conformado aleatoriamente"
        
        self.crear_lista() #Llama el metodo crear lista para tener la lista Participantes_ actualizada
        listaC_ = list(ra.sample(self.Participantes_,len(self.Participantes_)))
        #listaC_ es una lista como 
        self.Grupos_= {}
        for i in range(cant_):
            key = str("Grupo: "+str(i))
            datos = [[],[]]
            self.Grupos_[key] = datos #Resetea self.Grupos_
            
        while listaC_ != []: #Mantiene este boclet hasta que listaC_ se quede sin elementos
            for ikey, ivalue in self.Grupos_.items():
                if listaC_ != []:
                    elegido_=listaC_.pop()
                    ivalue[0].append(elegido_)
                    ivalue[1].append(self.Planilla_[self.buscar_alia(elegido_)][1])
                else: 
                    break
        return self.Grupos_
    
    def escribir_lista(self,lista_):
        string=""
        ultima = len(lista_)
        j = 0
        for i in lista_:
            j += 1
            if j<ultima: string = string + i +", "
            else : string = string + i
        return string
    
    def caritafeliz(self,dia):
        self.Planilla_[self.buscar_alia(self.llamar_a)].append(str(dia))
        print("Felicitaciónes %s  \U0001f600 ! "%(self.llamar_a))
  
    def medallero(self):
        lista =[]
        val : int
        for key, value in self.Planilla_.items():
            if (len(value) > 2):
                lista.append(len(value))
        lista.sort()
        while True:
            val=int(lista.pop())
            for key, value in self.Planilla_.items():
                if (len(value)==val):
                    print(value[0]+": " + " ".join("\U0001f600" for i in range(len(value)-2))+"\n")
            if len(lista)==0:
                break
