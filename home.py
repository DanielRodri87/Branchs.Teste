import numpy as plt
import pandas as pd   
import matplotlib.pyplot as plt 

dados = pd.read_csv('C:\\Users\\Rodrigues\\Desktop\\BRANCH-TESTE\\athlete_events.csv')

masculinos = dados.loc[dados['Sex']=='M']
femininos = dados.loc[dados['Sex']=='F']

alturaM = masculinos['Height']
pesoM = masculinos['Weight']

alturaF = femininos['Height']
pesoF = femininos['Weight']

plt.title('Reção Altura/Peso')
plt.ylabel('Altura')
plt.xlabel('Peso')
plt.scatter(alturaF, pesoF, color="pink")
plt.scatter(alturaM, pesoM, color="blue")
plt.savefig('grafico_linha.png', format='png')
plt.show()