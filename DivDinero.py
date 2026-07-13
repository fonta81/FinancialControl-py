# importa json, datetime
import json
import datetime

# defie dia de hoy -> para imprimirlo
now = datetime.datetime.now()
Hoy = now.strftime("%Y/%m/%d")
DivDinerosDicc = {  # crea las diviciones con sus porcentajes en tupla
    # [0] -> valor para ese monto // [1] -> porcentaje
    "Ahorros Largo Plazo": (0, 0.1),
    "formacion": (0, 0.1),
    "Basicos": (0, 0.5),
    "Donativos": (0, 0.1),
    "Jugar": (0, 0.1),
    "Libertad Financiera": (0, 0.1),
}


class DinerosClass:
    def __init__(self):
        self.montoactualdiv = 0

    def MontoDiv(self, MontoActualDividir):
        global DivDinerosDicc  # para usar el diccionario antes creado
        self.montoactualdiv = MontoActualDividir  # la igualamos con la de la funcion MontoActualDividir -> montoactualdiv
        for NombreDeMontos, Valores in DivDinerosDicc.items():  # dividimos el dinero
            # [0]->monto actual * el procentaje // [1]-> porcentaje
            DivDinerosDicc[NombreDeMontos] = (
                MontoActualDividir * Valores[1],
                Valores[1],
            )
        print("=" * 60 + "\n" + "Se hizo el proceso correctamente")  # style
        # imrpime la cantidad que se dividio:
        print(f"Valor total: {self.montoactualdiv}/{self.montoactualdiv:,}")
        print(f"Fecha de la divicion: {Hoy}")  # imrpime el dia de hoy
        for NombreDeMontos, Dinero in DivDinerosDicc.items():  # imrpime los valores
            print(f"El monto para {NombreDeMontos} = {Dinero[0]:,.2f}")

    def MostrarActuales(self):
        print(f"{self.montoactualdiv}/{self.montoactualdiv:,}")
        print(Hoy)  # imrpime el dia de hoy
        for NombreDeMontos, Dinero in DivDinerosDicc.items():  # imrpime los valores
            print(f"El monto para {NombreDeMontos} = {Dinero[0]:,.2f}")


class ModificarArchivo:
    def cargar(self):  # Se encargara de cargar
        global DivDinerosDicc  # usa el diccionario global
        try:
            # abre el archivo en modo lectura:
            with open("DivDinero.json", "r", encoding="utf-8") as archivo:
                DivDinerosDicc = json.load(archivo)  # Valor cargado -> dicc
                print("Se cargaron correctamente los datos")

        except Exception as e:  # en caso de error:
            print(f"no se pudo cargar correctamente\n error: {e}")

    def Guardar(self):  # se usara para sobrescribir los datos
        global DivDinerosDicc  # usa el diccionario global
        try:
            # abre el archivo en modo escribir:
            with open("DivDinero.json", "w", encoding="utf-8") as archivo:
                # guarda el diccionario en el json:
                json.dump(DivDinerosDicc, archivo, indent=4, ensure_ascii=False)
                print("Guardo correctamente")
        except Exception as e:  # en caso de error:
            print(f"no se pudo guardar correctamente\n error: {e}")

    def SumGuar(self):  # se usara para la suma de los actuales con los guardados
        global DivDinerosDicc  # se usa el dicc global
        try:
            # abre el json en lectura:
            with open("DivDinero.json", "r", encoding="utf-8") as archivo:
                DatosCargados = json.load(archivo)  # carga los datos
                # modifica el dicc original:
                for nombre, cantidad in DivDinerosDicc.items():
                    # [0] -> datos actuales + datos cargados // [1] -> procentaje
                    DivDinerosDicc[nombre] = (
                        cantidad[0] + DatosCargados.get(nombre)[0],
                        cantidad[1],
                    )
            self.Guardar()  # se usa la funcion guardar para sobrescribir los datos

        except Exception as e:  # en caso de error:
            print(f"no se pudo cargar correctamente\n error: {e}")

    def Eleccion(self):  # organiza el codigo para el ususario
        GuardarCargar = input("1.Guardar\n2.cargar\nElige:")  # guardar o cargar
        if GuardarCargar == "2":  # carga
            self.cargar()
        elif GuardarCargar == "1":  # guardar
            EligeSum = input(  # que funcion se usara:
                "Quieres sumar los datos actuales con los guardados?:\n1.si\n2.no\nElige: "
            )
            if EligeSum == "1":  # se suma y se guarda
                self.SumGuar()
            elif EligeSum == "2":  # se guarda y se elimina cualquier dato anterior
                self.Guardar()
            else:  # en caso de error:
                print("ingresa un valor valido")
        else:  # en caso de error:
            print("Digite un valor valido")


def main():
    Din = DinerosClass()  # se asigna valor a DinerosClass
    Modi = ModificarArchivo()  # se asigna valor a ModificarArchivo
    while True:
        print("=" * 60)  # style
        print("1.Dividir dinero")
        print("2.Guardar o cargar")
        print("3.Mostrar diviciones actuales")
        print("4.Salir")
        print("=" * 60)  # style
        Elige = input("Elige: ")

        if Elige == "4":  # salir
            print("Saliendo...")
            break
        elif Elige == "1":  # dividir el dinero
            print("\n")  # style
            print("=" * 60)  # style
            Din.MontoDiv(int(input("Digite el monto a dividir: ")))

        elif Elige == "2":  # guardar o cargar los datos
            print("\n")  # style
            print("=" * 60)  # style
            Modi.Eleccion()
        elif Elige == "3":  # Mostrar el estado actual del dicc
            print("\n")  # style
            print("=" * 60)  # style
            Din.MostrarActuales()
        else:  # en caso de error:
            print("Ingrese un valor valido")


if __name__ == "__main__":  # inicia el programa
    main()
