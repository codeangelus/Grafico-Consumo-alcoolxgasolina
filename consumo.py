import matplotlib.pyplot as plt
import numpy as np

# Preços (R$/L)
p_gasolina = 6.09
p_alcool = 4.74

# Consumo (km/L)
c_gasolina = 12
c_alcool = 10

# Função custo por km (M = preço / consumo)
def m(preco, consumo):
    return preco / consumo

# Equações da reta: y = Mx
def gasolina(x):
    return m(p_gasolina, c_gasolina) * x

def alcool(x):
    return m(p_alcool, c_alcool) * x

# Distância percorrida (km)
x_values = np.linspace(0, 200, 400)  # de 0 a 200 km

# Gera os valores de custo total
y_gasolina = gasolina(x_values)
y_alcool = alcool(x_values)

# Cria o gráfico
plt.figure(figsize=(8, 6))

# Plot das linhas
plt.plot(x_values, y_gasolina, label='Gasolina', color='red')
plt.plot(x_values, y_alcool, label='Álcool', color='blue')

# Rótulos e título
plt.xlabel('Distância percorrida (km)')
plt.ylabel('Custo total (R$)')
plt.title('Comparativo de custo - Gasolina x Álcool')
plt.grid(True)
plt.legend()

# Mostra o gráfico
plt.show()
