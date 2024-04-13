def cambio_de_monedas_total(monto_dar):
#calcular numero minimo de monedas 
    monedas = [1, 5, 10]
    result=[]
    total_monedas =0 # el total de monedas
    for m in reversed(monedas): #rodemamos las monedas de mayor a menor  denominacion
        cant_monedas=monto_dar // m # mientras el moto a cambiar sea mayor o igual a la moneda actual
        result.append((m, cant_monedas))# resultado de moneda
        total_monedas+= cant_monedas 
        monto_dar %= m #el valor de la moneda al monto al cambiar
#ver el resultado
    print("numero minimo de monedas:") 
    print(total_monedas)
    print("detalle de monedas")
    for moneda, cantidad in result:
        print(f"{cantidad} moneda(s) de {moneda}")
    print("suma total de monedas utilizadas:")
    print(sum(cantidad for_, cantidad in result))
    # solicitar el monto al usuario
monto_dar=int(input("ingrese el monto a cambiar:"))
#  llamar la funcion para cvalcular el cambio
cambio_de_monedas_total(monto_dar)
         



        





