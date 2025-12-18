_Este proyecto ha sido creado como parte del currículo de 42 por hgarcia2._

**Get_next_line**
# Descripción
El objetivo de este proyecto consiste en crear una función capaz de leer una línea desde un file descriptor. El objetivo principal es implementar una función que, llamada en un bucle, permita leer el contenido de un archivo línea por línea hasta el final manejando la memoria correctamente. La función debe ser capaz de leer y retornar cada línea terminada en '\n', (excepto la última si no termina en salto de línea), hasta que no quede nada más por leer.
Instrucciones 
Este proyecto es sencillo de compilar. Basta con compilar los .c necesarios para generar el programa.
# Compilación básica con BUFFER_SIZE de 42
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c
# Ejemplos con diferentes BUFFER_SIZE
cc -Wall -Wextra -Werror -D BUFFER_SIZE=1 get_next_line.c get_next_line_utils.c
cc -Wall -Wextra -Werror -D BUFFER_SIZE=1000 get_next_line.c get_next_line_utils.c
Para probarlo basta con ejecutar el ./a.out junto al archivo de texto necesario.
Recursos 
Principalmente se ha utilizado la documentación oficial relacionada con read y open, además de la documentación de las variables estáticas o del manejo de valgrind para detectar leaks. La IA se ha empleado para identificar posibles casos que no hubiesen sido contemplados en un inicio además de ser usada para comprender conceptos con los que no había trabajado antes.