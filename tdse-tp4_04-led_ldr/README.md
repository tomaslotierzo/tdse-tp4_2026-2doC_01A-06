# tdse-tp4_04-led_ldr

## Materiales 
- NUCLEO-F103RB
- LED blanco
- Resistor 100 ohm
- LDR
- Potenciómetro o trim pot 10 Kohm

## Procedimiento
1) Medir la resistencia del LDR cuando está iluminado y en la oscuridad. Tomar nota de los valores.
> max (oscuro) = 1M, min (con luz) = 100

2) Ajustar el potenciómetro a un valor de resistencia similar al mayor valor medido anteriormente.
3) Conectar el potenciómetro y el LDR en serie y alimentar la malla con 3,3V.
4) Conectar el punto medio de la malla a la entrada PA0 (ADC1_PIN0).
5) Conectar el LED blanco en serie con la R de 100 ohm.
6) Conectar el LED blanco al GPIO PA6 (TIM3_CH1), verificando la polaridad y la R a GND
7) Enfrentar el LED al LDR, procurando disminuir otra fuente de luz.
8) Debugear el firmware: F11 (Debug) -> F8 
9) Para cada nueva muestra leida por el ADC (LDR) se levanta una variable booleana.
 Al detectarla, el PWM cambia el duty cycle. Como resultado, como LDR y LED están enfrentados,
  la medición del LDR varia según el brillo.
10) Revisar la consola, ahí se imprime una lista de dos columnas con ambas magnitudes.
 Copiar la lista en una hoja de cálculo y dibujar ambas curvas.

Nota: Los resultados deberán registrarse en el archivo led_ldr.txt, en el root de la carpeta app de su
 repositorio. 

