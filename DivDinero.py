#nesesito un programa que sea capaz de dividir el dinero -> guararlo(0 o sum) -> cargarlo
import datetime; import json
n = datetime.datetime.now() #dia de hoy
Hoy = n.strftime('%Y/%m/%d')

Montos = { #datos a guardar
    'El monto para Jugar es de: ': (0.0,0.1),
    'El monto para Libertad financiera es de: ': (0.0,0.1),
    'El monto para los ahorros a largo plazo es de: ': (0.0,0.1),
    'El monto para la formacion es de: ': (0.0,0.1),
    'El monto para los basicos es de: ': (0.0,0.5),
    'El monto para las donaciones es de: ': (0.0,0.1)
}

def DivDinero():
    global Montos
    while True:
        try: MontoaDividir = int(input('Dijite el monto a dividir: ')); break # preguntando el monto a dividir
        except: print('inrgese un valor valido')
    for nombre in Montos: #dando valores 
        div = Montos.get(nombre)[1]  
        valor = MontoaDividir * div
        Montos[nombre] = (valor,div)
    print('\n\n')    
    print(f'Total = {MontoaDividir:,.0f} / {MontoaDividir}')
    print(Hoy) #mostrando los valores    
    print('='*60)
    for nombre in Montos:        
        print(f'{nombre} {Montos.get(nombre)[0]:,.2f}')
    print('='*60)
    
def Guardar0():
    try:
        with open('Ahorros.json', 'w', encoding='utf-8') as archivo: #guardando datos desde 0
            json.dump(Montos,archivo,indent=4,ensure_ascii=False)
        print('Los datos se guardaron correctamente')
    except: print('no se guardaron correctamente')

def GuardarSuma():
    global Montos
    try:
        with open('Ahorros.json', 'r', encoding='utf-8') as archivo: #cargando los datos
            MontosC = json.load(archivo)
            for key in Montos:
                ValorActual = Montos.get(key)[0] #lo separamos de los dato 
                Porcentaje = Montos.get(key)[1] # lo separamos de los dato 
                valor = ValorActual + MontosC.get(key)[0] #hallamos la suma
                Montos[key] = (valor,Porcentaje) # y lo volvemos a guardar
        Guardar0()
        print('los datos se guardaron correctamente')
    except: print('no se pudo guardar correctamente')

def Cargar():
    global Montos
    try:
        with open('Ahorros.json', 'r', encoding='utf-8') as archivo: #cargando los datos
            Montos = json.load(archivo)                    
    except: print('no se pudo cargar correctamente')

def EleccionGuar():    
    print('1. Guardar y sumar datos actuales o 2.Guardar y eliminar datos anteriores') #se pregunta que funcion de guardado se usara 
    while True:
        try: Tguar = int(input('Elige: ')); break
        except: print('ingrese un valor valido')        
    if Tguar in (1,2): # dentro de parametros?
        if Tguar == 1: #si es guardado normal es decir: sumguar
            GuardarSuma()
        elif Tguar == 2: 
            print('Estas seguro?\n1.si  2.no') # se verifica que el wey esta seguro 
            while True:
                try: Seguro = int(input('Elige: ')); break
                except: print('ingrese un valor valido')
            if Seguro in (1,2):
                if Seguro == 1: # si la respuesta es si entonces se guarda
                    Guardar0()
                elif Seguro == 2: # si no lo esta se usa return para salir 
                    return
            else: print('Ingrese un valor valido') # si pone un valor afuera de los parametros
    else: print('ingrese un dato valido')

def MostrarDatos():
    print(Hoy) #mostrando los valores    
    for nombre in Montos:        
        print(f'{nombre} {Montos.get(nombre)[0]:,.2f}')        


def main():
    while True:
        print('='*60)
        print('1.Dividir dinero')
        print('2.guardar')
        print('3.cargar')
        print('4.Mostrar datos actuales')
        print('5.salir')
        while True:
            try: elige = int(input('Elige: ')); break
            except: print('inrgese un valor valido')
        if elige in (range(1,6)):
            if elige == 1:
                print('='*60)
                DivDinero()
            elif elige == 2:
                print('='*60)
                EleccionGuar()
            elif elige == 3:
                print('='*60)
                Cargar()
            elif elige == 4:
                print('='*60)
                MostrarDatos()
            else:
                break
        else: print('ingrese un valor valido')

main()