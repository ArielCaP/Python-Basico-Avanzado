# Conversor de Temperaturas 🌡️

Programa que convierte una temperatura entre grados Celsius y Fahrenheit, manejando errores si el usuario ingresa datos inválidos.

## 🎯 ¿Qué hace?

1. Pide una temperatura y en qué unidad está (C o F)
2. Convierte al otro sistema usando las fórmulas correspondientes
3. Si el usuario escribe una unidad distinta a C o F, avisa que no es válida
4. Si el usuario escribe texto en vez de un número, evita que el programa se rompa

## 🧮 Fórmulas usadas

- Celsius a Fahrenheit: `F = (C * 9/5) + 32`
- Fahrenheit a Celsius: `C = (F - 32) * 5/9`

## 📚 Lo que aprendí

- `try / except` para manejar errores sin que el programa se rompa
- Diferencia entre un `except` genérico y uno específico (`except ValueError`)
- Distintos tipos de errores en Python: `ValueError`, `ZeroDivisionError`, `TypeError`, `IndexError`, `KeyError`, `FileNotFoundError`, `NameError`, `AttributeError`
- `.upper()` para normalizar texto ingresado por el usuario
- Diferencia entre un error real de Python (manejado con `try/except`) y una validación de lógica propia (manejada con `if/else`)
- Comentarios de varias líneas con `"""` o `'''`

## 🚀 Cómo ejecutarlo

```
python Conversor de temperaturas.py
```
