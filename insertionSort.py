import time

import psutil

arq = open('100milNum.csv', 'r')
final = open('100MilNumEstatisInsertionSort.txt', 'w')

linhas = arq.read()
linhas = linhas.split(';')

lista = []
for i in linhas:
    i = i.replace("\n", "")
    if(i != ''):
        lista.append(int(i))

tamanhoLista = len(lista)


def insertionSort(lista):
    tam = len(lista)
    qtdComparacoes = 0
    qtdTrocas = 0
    for i in range(1, tam):
        eleito = lista[i]
        j = i-1
        while (j >= 0) and (lista[j] > eleito):
            lista[j+1] = lista[j]
            j = j-1
            qtdComparacoes += 1
            qtdTrocas+=1
        lista[j+1] = eleito
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()
    return usoCpu, usoRam, qtdComparacoes, qtdTrocas


resultados=()
inicio = time.time()
resultados = insertionSort(lista)
fim = time.time()
tempExe = fim - inicio

final.write("Quantidade de comparações: "+str(resultados[2])+"\nQuantidade de trocas: "+str(resultados[3])+"\nTempo de execução: "+str(tempExe)+"\nUso da CPU: "+str(resultados[0])+"\nUso de RAM: "+str(resultados[1]))
final.close()
