# Calendario en Python / Calendar in Python

- Calendario interactivo en modo consola, implementado en Python **sin utilizar librerías para el cálculo de fechas**. 

- Interactive console calendar written in Python **without using any date/time libraries**


## Características / Features

- Cálculo manual del día de la semana (Congruencia de Zeller)
- Detección de años bisiestos
- Cálculo de los días por mes
- Alineación correcta comenzando lunes
- Interacción por teclado (mes y año)


## Lógica utilizada / Core Logic

| Función / Function          | Descripción / Description |
|-----------------------------|---------------------------|
| `isLeap(year)`              | Determina si un año es bisiesto / Determines leap years |
| `calculateDaysPerMonth()`   | Devuelve los días del mes / Returns number of days in month |
| `calculateDayOfWeek()`      | Calcula el día de la semana mediante la congruencia de Zeller / Computes weekday using Zeller's congruence |
| `showMonthCalendar()`       | Imprime el calendario / Prints the formatted calendar |

---
