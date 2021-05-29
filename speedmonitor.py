# Programa para medir a velocidade de Download e Upload
# ultima atualizacao: 29/05/2021

import speedtest as spdt
import time
from datetime import datetime
import pandas as pd
import sys
import matplotlib.pyplot as plt

# Variaveis
lista_down = []
lista_up = []
tempo = []
nTestes = int(input('Digite o numero de testes '))

# funcao para pegar a hora atual
def pegar_tempo():
	now = datetime.now()
	return now.strftime("%H:%M:%S")

# funcao para download
def dnld():
	return round(st.download() / 10 ** 6, 2)

def upld():
	return round(st.upload() / 10 ** 6, 2)

def coef_var(valor):
	import pandas as pd
	df = pd.DataFrame(valor)
	return round((df.std()/df.mean() * 100),2).values

def ard(valor):
	return round(valor,2)

#==============================================================================
# Testar a conexao com a internet
try:
	st = spdt.Speedtest()
except:
	print('Erro de Conexão!!!\nEncerrando programa')
	sys.exit()
    
print('Conectado!')

# =============================================================================
inicio = round(time.time())

loop = 0

while loop < nTestes:
	hora = pegar_tempo()										# chama a funcao pegar tempo
	download = dnld()											# chama a funcao download
	upload   = upld()											# chama a funcao upload
	tempo.append(hora)											# adiciona a hora na lista
	lista_down.append(download)									# adiciona o valor do download na lista
	lista_up.append(upload)										# adiciona o valor do upload na lista
    
	print(f'Hora: {hora} | Download: {download} | Upload: {upload}')
	loop += 1

tempo_total = round(((time.time()) - inicio) / 60, 2)			# tempo total de execucao

# Construindo o Dataframe
df = pd.DataFrame({'Tempo': tempo,
				   'Download': lista_down,
				   'Upload': lista_up})

# dividir o print em horas ou minutos
tempo_execucao = (tempo_total/60) if tempo_total > 60 else tempo_total
metrica_tempo = 'Horas' if tempo_total > 60 else 'Minutos'
print(f'Tempo de execucao: {tempo_execucao} {metrica_tempo}')

# metricas
media  = [df['Download'].mean(), df['Upload'].mean()]
cv     = [coef_var(df['Download']), coef_var(df['Upload'])]
minimo = [df['Download'].min(), df['Upload'].min()]
maximo = [df['Download'].max(), df['Upload'].max()]

print(f'Media: Download: {ard(media[0])} | Upload: {ard(media[1])}\n'
	  f'CV: Download: {cv[0]} | Upload: {cv[1]}\n'
	  f'Mínimo: Download: {ard(minimo[0])} | Upload: {ard(minimo[1])}\n'
	  f'Maxino: Download: {ard(maximo[0])} | Upload: {ard(maximo[1])}\n'
	  f'FIM DO PROGRAMA')

# visualizacao grafica
# linhas
fig, ax = plt.subplots()

line1, = ax.plot(tempo, lista_down, label='Download')
line1.set_dashes([2, 2, 10, 2])

line2, = ax.plot(tempo, lista_up, dashes=[6, 2], label='Upload')

ax.legend()
#fig.savefig('Grafico_DN_x_UP') # linha para exportar a imagem 
plt.show()

# exportando CSV
#df.to_csv('DF_DN_x_UP.csv')    # linha para exportar o DF como CSV







