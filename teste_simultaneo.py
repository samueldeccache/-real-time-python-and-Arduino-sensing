# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 01:02:51 2020

@author: Samsung
"""
#usar ani = FuncAnimation(plt.gcf(), atualizar, interval=200)
#cid = plt.gcf().canvas.mpl_connect("key_press_event", close)
#Mostrar o gráfico
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation 
import serial
import time
import sys
import os
vet1=[] #vetor pegando os primeiros valores
vet2=[] #vetor pegando outros valores
porta = 'COM9'
velocidade = 9600
vet=[]
conexao = serial.Serial(porta,velocidade)

def hl(numbers):
    y = []
    for x in numbers:
        x = float(x)
        y.append(x)
    return y
def leitura_serial(leitura_serial):
    vet=[]
    for i in range(0,10):
        leitura_serial = conexao.readline()
        leitura_limpa=leitura_serial.split()
        leitura_limpa1=str(leitura_limpa).strip('[]')
        leitura_limpa2=leitura_limpa1.replace('b','')
        leitura_limpa3=str(leitura_limpa2).strip("''")
        vet.append(leitura_limpa3)
    return vet 
vet=[]
    
while True:
    for i in range(0,10):
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
    t= input('deseja continuar?')
    if t == 'sim':
        for i in range(0,len(x2)):
            y.append(i)
        plt.plot(y,x1)
        plt.plot(y,x2)
        plt.title('Distancia x tempo')
        plt.show()
    else:
        for i in range(0,len(x2)):
            y.append(i)
        plt.plot(y, x1)
        plt.plot(y,x2)
        plt.title('Distancia x tempo')
        plt.show()
        break
#jogar os valores para o excel 
d = {'valores 1': vet1, 'valores 2': vet2}
df = pd.DataFrame(data = d)
df.to_excel('sensores2.xlsx', sheet_name='Planilha1')


            
        
    
            
    
    
    
    
        
    
        

    