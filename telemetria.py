#Mostrar o gráfico
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation 
import serial
import time
import sys
import os
from drawnow import *
cont = 0 
vet1=[] #vetor pegando os primeiros valores
vet2=[] #vetor pegando outros valores]

porta = 'COM9'
velocidade = 9600
vet=[]
conexao = serial.Serial(porta,velocidade)
x1=[]

#função para plot em tempo real 
def live():
    plt.subplot(2,1,1)
    plt.title("Estimação de Atitude")
    plt.grid(True)
    plt.ylabel('Angulação (graus)')
    plt.plot(x1, 'ro-', label='Angulação')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.subplot(2,1,2)
    plt.grid(True)
    plt.ylabel('Velocidade(rad/s)')
    plt.plot(x2, 'ro-', label='Velocidade')
    plt.legend(loc='upper left')
    plt.tight_layout()


#função para transformar as variáveis do vetor em float
def hl(numbers):
    y = []
    for x in numbers:
        x = float(x)
        y.append(x)
    return y
vet=[]
    
while True:
    while (conexao.inWaiting()==0):
        pass
    for i in range(0,150):
        leitura_serial = conexao.readline()
        leitura_limpa=leitura_serial.split()
        leitura_limpa1=str(leitura_limpa).strip('[]')
        leitura_limpa2=leitura_limpa1.replace('b','')
        leitura_limpa3=str(leitura_limpa2).strip("''")
        print(leitura_limpa3.split())
        vet.append(leitura_limpa3)
        x=hl(vet)
    #dividindo os vetores. A ideia é que cada valor lido 
    #do arduino representa um sensoriamento de cada linha
    # exemplo: o vetor1 guarda os valores de luminosidade e o vetor2 de distancia
        n=2
        splited = [vet[i::n] for i in range(n)]
        y=[]
        vet1=splited[0]
        vet2=splited[1]
        x1=hl(vet1)
        x2=hl(vet2)
        drawnow(live)
        #plt.pause(.0000001)
    n=2
    splited = [vet[i::n] for i in range(n)]
    y=[]
    vet1=splited[0]
    vet2=splited[1]
    x1=hl(vet1)
    x2=hl(vet2)
    for i in range(0,len(x2)):
            y.append(i)
    cont+=1
    if(cont>50):
       vet1.pop(0)
    break
    
#plt.plot(x1)
plt.plot(x1, label='Angulação')
plt.plot(x2,label='Velocidade Angular')
plt.ylabel('velocidade',size=15)
plt.xlabel('tempo(ms)',size =15)
plt.grid()
#plt.plot(x1,x3)
plt.title('Velocidade(rad/s) x tempo',size=15)
plt.legend()
plt.show()
#jogar os valores para o excel 
d = {'Velocidade Angular': vet1, 'Angulação': vet2}
df = pd.DataFrame(data = d)
df.to_excel('dados_telemetria.xlsx', sheet_name='Planilha1')
