def cambio_de_moneda(dinero):
    denominaciones= [10,5,1]
    resultado= [0,0,0]
    for i, denominacion in enumerate(denominaciones):
        num_monedas= dinero // denominacion
        resultado[i] = num_monedas
        dinero-= num_monedas* denominacion
        
    return resultado,sum(resultado)
#  el uso de monedas ejemplo 
dinero = int(input("ingrese la cantidad de dinero:"))
monedas_necesarias, suma_total= cambio_de_moneda (dinero)
print("monedas necesarias de denominacion 10:",monedas_necesarias[0])
print("monedas necesarias de denominacion 5:",monedas_necesarias[1])
print("monedas necesarias de denominacion 1:",monedas_necesarias[2])
print("suma total de monedas:",suma_total)



      




 




        





