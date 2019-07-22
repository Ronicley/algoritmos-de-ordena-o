import time

import psutil

arq = open('100milNum.csv', 'r')
final = open('100milNumEstatisBubbleSortMelhoria1.txt', 'w')

linhas = arq.read()
linhas = linhas.split(';')

lista = []
for i in linhas:
    i = i.replace("\n", "")
    if(i != ''):
        lista.append(int(i))

tamanhoLista = len(lista)


def bubbleSort(lista):
    qtdComparacoes = 0
    qtdTrocas = 0
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            qtdComparacoes += 1
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                
                qtdTrocas+=1
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()
    return usoCpu, usoRam, qtdComparacoes, qtdTrocas


def bubbleSortMelhoria1(lista):
    qtdComparacoes = 0
    qtdTrocas = 0
    for j in range(len(lista)):
        for i in range(len(lista)-1, j, -1):
            qtdComparacoes += 1
            if lista[i] < lista[i-1]:
                aux = lista[i]
                lista[i] = lista[i-1]
                lista[i-1] = aux
                
                qtdTrocas+=1
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()
    return usoCpu, usoRam, qtdComparacoes, qtdTrocas


def bubbleSortMelhoria2(lista):
    j=1
    troca=True
    tam = len(lista)-1
    qtdComparacoes = 0
    qtdTrocas = 0
    while (j<=tam) and troca:
        troca = False
        for i in range(tam, j-1, -1):
            qtdComparacoes += 1
            if lista[i]<lista[i-1]:
                troca=True
                aux = lista[i]
                lista[i] = lista[i-1]
                lista[i-1] = aux
               
                qtdTrocas+=1
        j+=1
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()
    return usoCpu, usoRam, qtdComparacoes, qtdTrocas

resultados=()
inicio = time.time()
resultados = bubbleSortMelhoria1(lista)
fim = time.time()
tempExe = fim - inicio

final.write("\tBubble Sort\n\nQuantidade de comparações: "+str(resultados[2])+"\nQuantidade de trocas: "+str(resultados[3])+"\nTempo de execução: "+str(tempExe)+"\nUso da CPU: "+str(resultados[0])+"\nUso de RAM: "+str(resultados[1]))
final.close()
