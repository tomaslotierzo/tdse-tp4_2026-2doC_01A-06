import matplotlib.pyplot as plt

curva1 = []
curva2 = []

with open('datos.txt', 'r') as archivo:
    for linea in archivo:
        if linea.strip(): 
            valores = linea.split(',')
            curva1.append(float(valores[0]))
            curva2.append(float(valores[1]))

# --- Crear y guardar el gráfico de la Curva 1 ---
plt.figure(figsize=(8, 5)) 
plt.plot(curva1, label='Curva 1', marker='o', linestyle='-', color='b')
plt.title('Gráfico de la Curva 1')
plt.xlabel('Índice (Número de muestra)')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()
plt.savefig('grafico_curva1.png', dpi=300) 
plt.close() 

plt.figure(figsize=(8, 5))
plt.plot(curva2, label='Curva 2', marker='s', linestyle='-', color='r')
plt.title('Gráfico de la Curva 2')
plt.xlabel('Índice (Número de muestra)')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()
plt.savefig('grafico_curva2.png', dpi=300)
plt.close()

print("Gráficos guardados exitosamente como 'grafico_curva1.png' y 'grafico_curva2.png'.")