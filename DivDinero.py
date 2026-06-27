import json
import datetime


now = datetime.datetime.now()
Hoy = now.strftime("%Y/%m/%d")
montoactualdiv = 0
DivDinerosDicc = {
    "Ahorros Largo Plazo": (0, 0.1),
    "formacion": (0, 0.1),
    "Basicos": (0, 0.5),
    "Donativos": (0, 0.1),
    "Jugar": (0, 0.1),
    "Libertad Financiera": (0, 0.1),
}


class DinerosClass:
    def MontoDiv(self, MontoActualDividir):
        global DivDinerosDicc
        global montoactualdiv
        montoactualdiv = MontoActualDividir
        for NombreDeMontos, Valores in DivDinerosDicc.items():
            DivDinerosDicc[NombreDeMontos] = (
                MontoActualDividir * Valores[1],
                Valores[1],
            )
        print("Los valores entonces seran:")
        for NombreDeMontos, Dinero in DivDinerosDicc.items():
            print(f"El monto para {NombreDeMontos} = {Dinero[0]:,.2f}")

    def MostrarActuales(self):
        print(f"{montoactualdiv}/{montoactualdiv:,}")
        print(Hoy)
        for NombreDeMontos, Dinero in DivDinerosDicc.items():
            print(f"El monto para {NombreDeMontos} = {Dinero[0]:,.2f}")


class ModificarArchivo:
    def cargar(self):
        global DivDinerosDicc
        try:
            with open("DivDinero.json", "r", encoding="utf-8") as archivo:
                DivDinerosDicc = json.load(archivo)
                print("Se cargaron correctamente los datos")

        except Exception as e:
            print(f"no se pudo cargar correctamente\n error: {e}")

    def Guardar(self):
        global DivDinerosDicc
        try:
            with open("DivDinero.json", "w", encoding="utf-8") as archivo:
                json.dump(DivDinerosDicc, archivo, indent=4, ensure_ascii=False)
                print("Guardo correctamente")
        except Exception as e:
            print(f"no se pudo guardar correctamente\n error: {e}")

    def SumGuar(self):
        global DivDinerosDicc
        try:
            with open("DivDinero.json", "r", encoding="utf-8") as archivo:
                DatosCargados = json.load(archivo)
                for nombre, cantidad in DivDinerosDicc.items():
                    DivDinerosDicc[nombre] = (
                        cantidad[0] + DatosCargados.get(nombre)[0],
                        cantidad[1],
                    )
            self.Guardar()

        except Exception as e:
            print(f"no se pudo cargar correctamente\n error: {e}")

    def Eleccion(self):
        GuardarCargar = input("1.Guardar\n2.cargar\nElige:")
        if GuardarCargar == "2":
            self.cargar()
        elif GuardarCargar == "1":
            EligeSum = input(
                "Quieres sumar los datos actuales con los guardados?:\n1.si\n2.no\nElige: "
            )
            if EligeSum == "1":
                self.SumGuar()
            elif EligeSum == "2":
                self.Guardar()
            else:
                print("ingresa un valor valido")
        else:
            print("Digite un valor valido")


def main():
    Din = DinerosClass()
    Modi = ModificarArchivo()
    while True:
        print("=" * 60)
        print("1.Dividir dinero")
        print("2.Guardar o cargar")
        print("3.Mostrar diviciones actuales")
        print("4.Salir")
        print("=" * 60)
        Elige = input("Elige: ")

        if Elige == "4":
            print("Saliendo...")
            break
        elif Elige == "1":
            print("\n")
            print("=" * 60)
            Din.MontoDiv(int(input("Digite el monto a dividir: ")))

        elif Elige == "2":
            print("\n")
            print("=" * 60)
            Modi.Eleccion()
        elif Elige == "3":
            print("\n")
            print("=" * 60)
            Din.MostrarActuales()
        else:
            print("Ingrese un valor valido")


if __name__ == "__main__":
    main()
