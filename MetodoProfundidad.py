lista=['a','b','c','d','e','f','g','h']
grafo={
    'a':['b','c','g'],
    'b':['a','d'],
    'c':['a','d','e'],
    'd':['b','c','f'],
    'e':['c','f','g'],
    'f':['d','e','h'],
    'g':['a','e'],   
    'h':['f'],
}

def profundidad(v,listaBusqueda,iteraciones):
    retroceso=True
    retrocesoValor=1

    while len(listaBusqueda)!=len(v) :
        for nodoSiguiente in v:
            if nodoSiguiente in grafo[listaBusqueda[-retrocesoValor]]  and nodoSiguiente not in listaBusqueda:
                print(listaBusqueda[-retrocesoValor],nodoSiguiente)
                iteraciones.append((listaBusqueda[-retrocesoValor],nodoSiguiente))
                retroceso=False
                retrocesoValor=1
                listaBusqueda.append(nodoSiguiente)
                break
        if retroceso:
            retrocesoValor+=1
        retroceso=True
    print(v,"\niteraciones",iteraciones,"\ncamino",listaBusqueda)

raiz=input("digite la posicion inicial: ")
profundidad(lista,[raiz],[])