*Este proyecto ha sido creado como parte del currículo de 42 por hgarcia2.*

**ft_printf** es una reimplementación de la función `printf()` de la librería estándar de C. El objetivo principal es comprender en profundidad cómo funciona el formateo de cadenas y la gestión de argumentos variables en C, implementando un subconjunto de las conversiones soportadas por la función original.

La función `ft_printf` replica el comportamiento de `printf` para las siguientes conversiones:
- `%c` - Imprime un solo carácter
- `%s` - Imprime una cadena de caracteres
- `%p` - Imprime un puntero en formato hexadecimal
- `%d` / `%i` - Imprime un número entero con signo en base decimal
- `%u` - Imprime un número entero sin signo en base decimal
- `%x` - Imprime un número en hexadecimal (minúsculas)
- `%X` - Imprime un número en hexadecimal (mayúsculas)
- `%%` - Imprime un signo de porcentaje

# Instrucciones

## Compilación

Para compilar la librería, ejecuta:
```bash
make
```

Esto generará el archivo `libftprintf.a` que contiene todas las funciones necesarias.

## Comandos adicionales

- `make clean` - Elimina los archivos objeto (.o)
- `make fclean` - Elimina los archivos objeto y la librería
- `make re` - Recompila el proyecto desde cero

## Uso en tu código

1. Incluye el header en tu archivo:
```c
#include "ft_printf.h"
```

2. Compila tu programa enlazando la librería:
```bash
cc ft_printf.c libftprintf.a -o ft_printf
```

# Estructura del Proyecto
```
ft_printf/
├── ft_printf.c          # Función principal y parseo de formato
├── ft_printf.h          # Header con prototipos y definiciones
├── ft_putchar.c      # Conversión %c
├── ft_putstr.c    # Conversión %s
├── ft_voidptr.c   # Conversión %p
├── ft_putnbr.c    # Conversiones %d, %i
├── ft_putunbr.c  # Conversión %u
├── ft_hexnbr.c       # Conversiones %x, %X
├── Makefile
└── README.md
```

# Algoritmo y Estructura de Datos

## Algoritmo

1. **Parseo secuencial**: La función principal recorre la cadena de formato carácter por carácter
2. **Detección de especificadores**: Al encontrar un `%`, se identifica el tipo de conversión
3. **Conversiones**: Se delega la conversión a la función especializada correspondiente
4. **Acumulación de longitud**: Cada función retorna el número de caracteres escritos

## Estructura de Datos

La implementación utiliza principalmente:

- **`va_list`**: Para acceder a los argumentos variables de forma secuencial
- **Arrays estáticos de caracteres**: Para las bases de conversión hexadecimal
- **Variables de contador**: Para acumular la longitud total escrita

**Decisiones técnicas clave**:

1. **Sin buffer intermedio grande**: Cada conversión escribe directamente con `write()`, evitando memoria extra y simplificando el manejo de errores

2. **Separación de casos hexadecimales**: Aunque `%x` y `%X` son similares, se implementan con lógica compartida pero arrays de caracteres diferentes para mantener la claridad

3. **Manejo de casos especiales**:
- Punteros nulos: Se imprime `(nil)` o `0x0` según el sistema
- Cadenas nulas: Se imprime `(null)`
- Número cero: Se maneja explícitamente para evitar salida vacía

# Uso de IA

**Herramientas utilizadas**: Perplexity / Claude

**Tareas realizadas con asistencia de IA**:

1. Consultas conceptuales (va_list) y optimización del código.

2. Ayuda para el Readme.
