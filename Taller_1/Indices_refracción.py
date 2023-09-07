import yaml as ym
import matplotlib.pyplot as plt
import numpy as np

def abrir (archivo):
    lista=[]
    with open(archivo, "r") as f:
        data=ym.safe_load(f)
        i=0
        for i in data["DATA"]:
            c=0
            y= i['data'].split("\n")
            
            z=len(y)
            for g in y:
                tupla = []
                for f in g.split():
                    tupla.append(float(f))
                   
                lista.append(tuple(tupla))

    return lista


def grafindicevslong(r):
    x=[]
    y=[]
    i=0
    t=len(r)-2
    while i<=t:
        if r[i]==():
            i+=1
            break
        else:
            x.append(r[i][1])
            y.append(r[i][0])
            i+=1
    x1=[]
    y1=[]
    if i<t:
        while i<=t:
             x1.append(r[i][1])
             y1.append(r[i][0])
             i+=1
        
    if len(x1)==0:
        plt.plot(x,y)
        plt.xlabel("longitud de onda")
        plt.ylabel("índice de refracción")
        plt.title("tabulado en n")
        plt.show()
    
    else:
        fig,axs=plt.subplots(1,2)
        axs[0].plot(x,y)
        axs[1].plot(x1,y1)
        axs[0].set_xlabel("longitud de onda")
        axs[0].set_ylabel("índice de refracción")
        axs[0].set_title("tabulado en n")
        axs[1].set_xlabel("longitud de onda")
        axs[1].set_ylabel("índice de refracción")
        axs[1].set_title("tabulado en k")
        plt.show()


def mixto(t,camino):
    lista=[]
    print(t)
    with open(t,"r") as f:
        data=ym.safe_load(f)
        i=0
        for i in data["DATA"]:
            c=0
            y= i['data'].split("\n")
            
            z=len(y)
            for g in y:
                tupla = []
                for f in g.split():
                    tupla.append(float(f))
                   
                lista.append(tuple(tupla))
    x=[]
    y=[]
    i=0
    t=len(lista)-2
    while i<=t:
        if lista[i]==():
            i+=1
            break
        else:
            x.append(lista[i][1])
            y.append(lista[i][0])
            i+=1
    x1=[]
    y1=[]
    if i<t:
        while i<=t:
             x1.append(lista[i][1])
             y1.append(lista[i][0])
             i+=1
        
    if len(x1)==0:
        plt.plot(x,y)
        plt.xlabel("longitud de onda")
        plt.ylabel("índice de refracción")
        plt.title("tabulado en n")
        plt.savefig(camino)
        
    else:
        fig,axs=plt.subplots(1,2)
        axs[0].plot(x,y)
        axs[1].plot(x1,y1)
        axs[0].set_xlabel("longitud de onda")
        axs[0].set_ylabel("índice de refracción")
        axs[0].set_title("tabulado en n")
        axs[1].set_xlabel("longitud de onda")
        axs[1].set_ylabel("índice de refracción")
        axs[1].set_title("tabulado en k")
        plt.savefig(camino)
    

mixto("Taller_1\idrio\BK10.yml","Taller_1\idrio/Gráfica_BK10")




    










