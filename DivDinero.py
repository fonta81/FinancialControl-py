import json
import datetime

n = datetime.datetime.now()
Hoy = n.strftime('%Y/%m/%d') #para poder imprimir el dia de hoy sin problema 

DatosPrincipales = { #los datos que se usaran durante todo el codigo 
    'MJugar': 0,
    'Libertad': 0,
    'AhorrosLargoPlazo': 0,
    'Formacion': 0,
    'Basicos': 0,
    'Donativos': 0
}
def cargar():
    global DatosPrincipales
    try:
        with open("DinerosDiv.json", "r", encoding="utf-8") as archivo: #carga los datos
            datos_cargados = json.load(archivo)
            
            for clave in DatosPrincipales.keys(): #remplaza los datos del diccionario actual con los que cargo
                DatosPrincipales[clave] = datos_cargados.get(clave, 0)
                
        print("Datos cargados correctamente en el sistema.")

    except: print('No se pudo cargar correctamente los datos')#en caso de error 


def Guardar():
    try:        
        with open("DinerosDiv.json", "w", encoding="utf-8") as archivo: #guarda los archivos desde 0
            json.dump(DatosPrincipales, archivo, indent=4, ensure_ascii=False)
        print('Los datos se guardaron correctamente')
    except: print('no se pudo guardar correctamente') #en caso de error

def SumGuar():
    global DatosPrincipales 
    try:
        with open("DinerosDiv.json", "r", encoding="utf-8") as archivo: #carga los archivos
            DatosPrincipales = json.load(archivo)
                
        for clave in DatosPrincipales.keys():
            DatosPrincipales[clave] += DatosPrincipales.get(clave, 0) #le suma los actuales a los q ya estaban 
            
        Guardar() #los guarda
        print('Los datos se actualizaron correctamente')
    except: print('no se pudo guardar correctamente') #en caso de error

def main():
    cargar() 
    while True:
        try: mon = float(input('Ingresa el monto de $: ')); break #dato correcto = salir del bucle
        except: print('ingrese un dato valido')#dato que no sea float = repetir la pregunta

    global DatosPrincipales #se halla el valor de cada uno segun lo que nos dio el usuario 
    DatosPrincipales['MJugar'] = mon * 0.1
    DatosPrincipales['Libertad'] = mon * 0.1
    DatosPrincipales['AhorrosLargoPlazo'] = mon * 0.1
    DatosPrincipales['Formacion'] = mon * 0.1
    DatosPrincipales['Basicos'] = mon * 0.5
    DatosPrincipales['Donativos'] = mon * 0.1

    print('\n') # se imprimen los datos de la division al usuario 
    print(Hoy)
    print('='*60)

    print(f"El monto para Jugar es de: {DatosPrincipales['MJugar']:.2f}")
    print(f"El monto para Libertad financiera es de: {DatosPrincipales['Libertad']:.2f}")
    print(f"El monto para los ahorros a largo plazo es de: {DatosPrincipales['AhorrosLargoPlazo']:.2f}")
    print(f"El monto para la formacion es de: {DatosPrincipales['Formacion']:.2f}")
    print(f"El monto para los basicos es de: {DatosPrincipales['Basicos']:.2f}")
    print(f"El monto para las donaciones es de: {DatosPrincipales['Donativos']:.2f}")
    
    print('='*60)

def MostrarDatos():

    print('\n') # se imprimen los datos de la division al usuario 
    print(Hoy)
    print('='*60)

    print(f"El monto para Jugar es de: {DatosPrincipales['MJugar']:.2f}")
    print(f"El monto para Libertad financiera es de: {DatosPrincipales['Libertad']:.2f}")
    print(f"El monto para los ahorros a largo plazo es de: {DatosPrincipales['AhorrosLargoPlazo']:.2f}")
    print(f"El monto para la formacion es de: {DatosPrincipales['Formacion']:.2f}")
    print(f"El monto para los basicos es de: {DatosPrincipales['Basicos']:.2f}")
    print(f"El monto para las donaciones es de: {DatosPrincipales['Donativos']:.2f}")
    
    print('='*60)

def menu():
    while True:
        print('\n')
        print('='*60)
        print('1.Guardar')
        print('2.Cargar')
        print('3.Mostrar datos actuales')
        print('4.main')
        print('5.Salir')
        while True:
            try: elg = int(input('Elige: ')); break
            except: print('ingrese un valor valido')
        
        if elg in (range(1,6)):
            if elg == 1:
                print('1. Guardar y sumar datos actuales o 2.Guardar y eliminar datos anteriores') #se pregunta que funcion de guardado se usara 
                while True:
                    try: Tguar = int(input('Elige: ')); break
                    except: print('ingrese un valor valido')
                    
                if Tguar in (1,2): # dentro de parametros?

                    if Tguar == 1: #si es guardado normal es decir: sumguar
                        SumGuar()

                    elif Tguar == 2: 
                        print('Estas seguro?\n1.si  2.no') # se verifica que el wey esta seguro 
                        while True:
                            try: Seguro = int(input('Elige: ')); break
                            except: print('ingrese un valor valido')
                        if Seguro in (1,2):
                            if Seguro == 1: # si la respuesta es si entonces se guarda
                                Guardar()
                            elif Seguro == 2: # si no lo esta se usa return para salir 
                                return
                        else: print('Ingrese un valor valido') # si pone un valor afuera de los parametros

                else: print('Ingrese un valor valido')            
            elif elg == 2:
                cargar()
            elif elg == 3:
                MostrarDatos()
            elif elg == 4:
                main()
            else: break



menu()