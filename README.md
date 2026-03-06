# Calculadora de Fatiga de Ejes

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una **aplicación en Python para el análisis de ejes mecánicos sometidos a flexión y torsión combinadas**, considerando criterios de falla estática y por fatiga utilizados en el **diseño de elementos mecánicos**.

El programa permite calcular automáticamente distintos parámetros importantes en el diseño de ejes, tales como:

* Factores de concentración de esfuerzos
* Sensibilidad a la muesca
* Factores de fatiga
* Esfuerzos normales y cortantes
* Esfuerzo equivalente de **Von Mises**
* Factores de seguridad mediante los criterios de:

  * Goodman
  * Soderberg
  * Gerber
  * ASME Elíptico

La aplicación cuenta con una **interfaz gráfica desarrollada con Tkinter**, que permite ingresar datos, seleccionar unidades y visualizar los resultados de forma clara.

---

# Tecnologías utilizadas

El programa fue desarrollado en **Python** utilizando **Visual Studio Code** como entorno de desarrollo.

Las librerías utilizadas fueron:

### math

La librería `math` permite realizar operaciones matemáticas necesarias para las ecuaciones de diseño mecánico, como raíces cuadradas y potencias.

```python
import math
```

Estas funciones se utilizan para cálculos como el esfuerzo equivalente de Von Mises:

```python
sigma_a_vm = math.sqrt(sigma_a**2 + 3*tau_a**2)
sigma_m_vm = math.sqrt(sigma_m**2 + 3*tau_m**2)
```

---

### tkinter

La librería `tkinter` permite crear la **interfaz gráfica del programa**, incluyendo ventanas, botones y campos de entrada de datos.

```python
import tkinter as tk
from tkinter import ttk
```

Con esta librería se crea la ventana principal del programa:

```python
root = tk.Tk()
root.title("Calculadora de Fatiga de Ejes")
root.geometry("900x700")
```

---

# Conversión de unidades

El programa incluye funciones que convierten automáticamente las unidades ingresadas por el usuario al **Sistema Internacional (SI)**.

Ejemplo de conversión de longitud:

```python
def conv_long(v,u):
    if u=="m": return v
    if u=="cm": return v/100
    if u=="in": return v*0.0254
```

Esto permite que el usuario pueda ingresar valores en **metros, centímetros o pulgadas**, manteniendo consistencia en los cálculos.

También se implementaron funciones similares para:

* conversión de momentos
* conversión de esfuerzos

---

# Función principal de cálculo

La función principal del programa es `calcular()`, la cual se ejecuta cuando el usuario presiona el botón **CALCULAR** en la interfaz.

```python
def calcular():
```

Esta función realiza los siguientes procesos:

1. Lectura de los datos ingresados por el usuario.
2. Conversión automática de unidades.
3. Cálculo de relaciones geométricas del eje.
4. Determinación de factores de concentración de esfuerzos.
5. Cálculo de sensibilidad a la muesca.
6. Obtención de factores de fatiga.
7. Cálculo de esfuerzos normales y cortantes.
8. Evaluación del esfuerzo equivalente mediante Von Mises.
9. Determinación de factores de seguridad por diferentes criterios de fatiga.

---

# Cálculo de esfuerzos

El programa calcula los esfuerzos normales producidos por flexión mediante la siguiente expresión:

```python
sigma_a = (32*Ma)/(math.pi*d**3)*Kf
sigma_m = (32*Mm)/(math.pi*d**3)*Kf
```

Los esfuerzos cortantes producidos por torsión se calculan mediante:

```python
tau_a = (16*Ta)/(math.pi*d**3)*Kfs
tau_m = (16*Tm)/(math.pi*d**3)*Kfs
```

Estos cálculos consideran los factores de concentración de esfuerzos y los factores de fatiga.

---

# Criterio de Von Mises

El esfuerzo equivalente de Von Mises se calcula mediante:

```python
sigma_a_vm = math.sqrt(sigma_a**2 + 3*tau_a**2)
sigma_m_vm = math.sqrt(sigma_m**2 + 3*tau_m**2)
```

Este criterio permite evaluar el comportamiento del material bajo **esfuerzos combinados de flexión y torsión**.

---

# Criterios de fatiga

El programa calcula factores de seguridad utilizando diferentes criterios de diseño:

### Goodman

```python
inv = (16/(math.pi*d**3))*((A/Se)+(B/Sut))
n_good = 1/inv
```

### Soderberg

```python
inv = (16/(math.pi*d**3))*((A/Se)+(B/Sy))
n_sod = 1/inv
```

### Gerber

```python
inv = (8*A)/(math.pi*d**3*Se)*(1+math.sqrt(1+(2*B*Se/(A*Sut))**2))
n_ger = 1/inv
```

### ASME Elíptico

```python
inv = (16/(math.pi*d**3))*math.sqrt(
    4*(Kf*Ma/Se)**2 +
    3*(Kfs*Ta/Se)**2 +
    4*(Kf*Mm/Sy)**2 +
    3*(Kfs*Tm/Sy)**2)
```

Estos criterios permiten evaluar la **seguridad del diseño frente a cargas fluctuantes**.

---

# Ejecución del programa

Para ejecutar el programa:

1. Descargar o clonar el repositorio.
2. Abrir el archivo en **Visual Studio Code**.
3. Ejecutar el archivo principal.

```bash
python Calculadora.py
```

Se abrirá la interfaz gráfica del programa donde el usuario podrá ingresar los datos y obtener los resultados.

---

# Estructura del repositorio

El repositorio contiene:

* **Calculadora.py** → código principal del programa.
* **README.md** → documentación del proyecto.

---

# Autores

- Arias Jiménez David Eduardo
- Chan Tosca Francisco Javier
- De la Cruz Sastre Emanuel
- Jiménez Velázquez Alejandro
- Lozano Herrera Alexander
- Osorio Hernández José Andrés
- Risso Santos Roberto Carlos

---

# Asignatura

Diseño de Elementos Mecánicos

---

# Institución

Instituto Tecnológico Superior de Comalcalco

---

# Licencia

Este proyecto se distribuye bajo la licencia **MIT**, permitiendo su uso libre con fines educativos y académicos.
