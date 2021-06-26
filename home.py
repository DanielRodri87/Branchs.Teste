#Importação das bibliotcas necessáiras 
import pandas as pd   
import matplotlib.pyplot as plt 

#Arquivo com dados de atletas olímpicos usando no programa
dados = pd.read_csv('C:\\Users\\Rodrigues\\Desktop\\BRANCH-TESTE\\athlete_events.csv')

#seleção de gênero
masculinos = dados.loc[dados['Sex']=='M']
femininos = dados.loc[dados['Sex']=='F']

#Seleção de tópicos masculinos abordados
alturaM = masculinos['Height']
idadeM = masculinos['Age']

#Seleção de tópicos femininos abordados
alturaF = femininos['Height']
idadeF = femininos['Age']

#Criação e amarzenamengo do gráfico
plt.title('Tamanho Feminino e Masculino em relação a Idade')
plt.ylabel('Idade')
plt.xlabel('Tamanho')
plt.scatter(alturaF, idadeF, color="pink") #Mulheres simbolizadas por rosa
plt.scatter(alturaM, idadeM, color="blue") #homens simbolizados por azul
plt.savefig('atletas.png', format='png')
plt.show()