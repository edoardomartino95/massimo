myarr = [2,1,5,7,9,0,3] #creo un array di numeri 

def maxmassimo(arr): #creo la funzione maxmassimo
    massimo = arr[0] #massimo è il primo elemento dell'array
    for i in range(len(arr)): #ciclo for per scorrere l'array -> [len(arr) volte]
        if massimo < arr[i]: #se il massimo è minore del valore corrente
            massimo = arr[i] #massimo diventa il valore corrente
    return massimo #ritorno il massimo

print("l'array conta questi numeri: ", myarr) #stampo l'array
print("il massimo è: ", maxmassimo(myarr)) #stampo il massimo
