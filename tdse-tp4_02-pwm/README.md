# tdse-tp4-pwm

1. Forkear el repositorio y abrir el proyecto en STM32CubeIDE
2. Analizar en el IOC las configuraciones del TIM3 y del RCC, sin modificarlas
3. En PA6 colocar un cable Dupont hembra macho y dejarlo al aire. En GND colocar un cable Dupont macho macho y dejarlo al aire.
4. Enchufar la placa NUCLEO-F103RB

## Test 1
5. Volver al código y configurar el primer test, verificando el `#define TEST_NUMBER` (línea 18 de app.c), es decir que diga `#define TEST_NUMBER TEST_1`
6. Compilar y debuggear.
7. Colocar la punta del osciloscopio entre PA6 y GND y analizar la forma de onda mostrada. ¿Cuál es el período de la señal? ¿Se modifica?
 ¿Cómo se define duty cycle? Se modifica?
8. Colocar un led entre PA6 y GND (no olvidar R de polarización) y observar la intensidad del brillo.


> Aparece una señal periodica de tension pico 3.3V, el periodo es de 1 ms y no se modifica, se modifica el ancho de los pulsos y por lo tanto el duty cycle.
> El led varia la intensidad del brillo suavemente.


## Test 2
9. Volver al código y configurar el segundo test, mediante la directiva `#define TEST_NUMBER TEST_2`
10. Compilar y debuggear.
11. Colocar la punta del osciloscopio entre PA6 y GND y analizar la forma de onda mostrada. ¿Qué ocurre con el período de la señal?
 ¿Qué ocurre con el duty cycle?
12. Colocar un led entre PA6 y GND (no olvidar R de polarización) y observar la intensidad del brillo.
13. Comparar resultados


> En la señal del osciloscopio el periodo varia rapidamente. A ojo mantiene un duty cycle de 50%, solo se modifica el periodo
> La intensidad del brillo del led no varia.


*Nota:* Los comentarios deberán registrarse en los archivo pwm.txt, test_1.txt y test_2.txt, en el root de la carpeta app de su repositorio.
 Asimismo, en esa misma ubicación se debe incorporar todo material de soporte o argumentación, tal como capturas de pantalla de computadora,
  capturas de pantalla de osciloscopio, fotografías, etcétera.