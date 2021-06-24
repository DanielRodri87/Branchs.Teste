import numpy as plt
import pandas as pd   
import matplotlib.pyplot as plt 

dados = pd.read_csv('/home/daniel/Downloads/athlete_events.csv')

masculinos = dados.loc[dados['Sex']=='M']

altura = masculinos['Height']
peso = masculinos['Weight']

plt.scatter(altura, peso)
plt.savefig('grafico_linha.png', format='png')
plt.show()