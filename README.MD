# Gestor de Finanzas Personales (6 Jarras)

Este es un script interactivo en Python diseñado para automatizar la división de ingresos basada en el método de las **6 jarras de la libertad financiera**. Permite ingresar un monto acumulado, distribuirlo automáticamente en diferentes categorías según porcentajes asignados, y gestionar un historial persistente utilizando un archivo local en formato JSON.

## Características

* **División Automática:** Calcula de forma instantánea los montos destinados a cada categoría a partir de una cantidad base.
* **Persistencia de Datos (JSON):** Guarda tu progreso financiero en un archivo local (`Estudio.json`).
* **Modos de Guardado Flexibles:**
  * **Guardar y Sumar:** Añade los montos recién calculados al balance acumulado que ya tenías guardado.
  * **Guardar desde Cero:** Sobrescribe los datos anteriores para reiniciar tus cuentas.
* **Formateo Limpio:** Muestra las cifras con separadores de miles y dos decimales (`1,000.00`) para una lectura cómoda.

---

## Distribución de Porcentajes

El programa utiliza la siguiente configuración predeterminada para la división de los ingresos:

| Categoría | Porcentaje | Descripción |
| :--- | :---: | :--- |
| **Basicos** | `50%` | Gastos necesarios para vivir (arriendo, servicios, comida). |
| **MJugar** | `10%` | Dinero destinado a ocio, diversión y caprichos. |
| **Libertad** | `10%` | Inversiones o capital destinado a generar más ingresos. |
| **AhorrosLargoPlazo** | `10%` | Fondos para metas futuras o emergencias. |
| **Formacion** | `10%` | Libros, cursos y educación personal. |
| **Donativos** | `10%` | Ayuda social o regalos. |

---

## Estructura de Datos Interna

Para evitar la pérdida de los multiplicadores al guardar y cargar datos, el script implementa un sistema de **tuplas** dentro del diccionario principal:

```python
# Estructura: 'Nombre de la Jarra': (MontoAcumulado, PorcentajeDeDivisión)
Montos = {
    'El monto para Jugar es de: ': (0.0, 0.1),
    'El monto para los basicos es de: ': (0.0, 0.5),
    # ...
}