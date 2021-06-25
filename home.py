import numpy as plt
import pandas as pd   
import matplotlib.pyplot as plt 

dados = pd.read_csv('C:\\Users\\Rodrigues\\Desktop\\BRANCH-TESTE\\athlete_events.csv')

masculinos = dados.loc[dados['Sex']=='M']

altura = masculinos['Height']
peso = masculinos['Weight']

plt.title('Reção Altura/Peso')
plt.ylabel('Altura')
plt.xlabel('Peso')
plt.scatter(altura, peso)
plt.savefig('grafico_linha.png', format='png')
plt.show()