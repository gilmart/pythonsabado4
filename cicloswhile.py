observador=100

print("**MENU**")
print("0.SALIR")
print("1.Saludar")
print("2.Despedir")

while(observador != 0):
    observador=int(input('digite una opcion: '))
    if(observador==0):
        print('programa terminado')
        break        
    elif(observador == 1):
        print('hola')
    elif(observador == 2):
        print('chao')
    else:
        print('digite una opcion valida')
else:
    print('termine')



