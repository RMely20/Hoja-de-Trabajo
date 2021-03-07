#Melanie R. Morataya
#Ejercicio 1
print('¡Hola a ‘” todas “’ y “’ todos!’”’')
print()

#Ejercicio 2
username=input('Ingrese su nombre: ')
print('! Hola ',username,'!')
print()

#Ejercicio 3
a=1
b=0
q1=b|b
q2=b|a
q3=a|b
q4=a|a 
print("A B Q")
print(b, b, q1)
print(b, a ,q2)
print(a, b ,q3)
print(a, a ,q4)
print()

#Ejercicio 4
hrs=int(input('Ingrese el número de horas estudiadas para el curso de Programación III: '))
prom=int(input('Ingrese el tiempo promedio usado por día: '))
suma=hrs+prom
print('La sumatoria de horas es de: '+str(suma))
print()

#Ejercicio 5
m=int(input('Ingrese un número entero: '))
suma=m*(m+1)/2
print('La suma de todos los enteros de 1 a '+str(m)+' es '+str(suma))
print()

#Ejercicio 6
peso=input('Ingrese su peso en libras: ')
estatura=input('Ingrese su estatura en metros: ')
imc=round(float(peso)/float(estatura)**2,2)
print("Su índice de masa corporal es: " + str(imc))
print()

#Ejercicio 7
a=input('Ingrese un numero decimal: ')
b=input('Ingrese otro numero decimal: ')
c=round(float(a)//float(b),2)
d=round(float(a)%float(b),2)
print(a + ' entre ' +  b + ' da un cociente ' + str(c) + ' y un resto ' + str(d))
print()

#Ejercicio 8
monto=float(input('Ingrese el monto a invertir: '))
interes=float(input('Ingrese el interes anual: '))
años=int(input('Ingrese la cantidad de años: '))
capital=round(monto * (interes / 100 + 1) ** años, 2)
print('Capital obtenido en la inversión: '+str(capital))
print()

#Ejercicio 9
peso_1=112
peso_2=75
barrenos=int(input('Ingrese el número de barrenos a enviar: '))
sierras=int(input('Ingrese el número de sierras a enviar: '))
total=peso_1*barrenos+peso_2*sierras
print('El peso total del paquete es de: '+str(total)+' kg')
print()

#Ejercicio 10
precio=20.00
descuento=0.6
memoria=int(input('Ingrese el número de memorias RAM vendidas que no son nuevas: '))
total=memoria*precio*(1-descuento)
print('El precio del una memoria RAM nueva es de: US $'+str(precio))
print('El descuento que se le hace a una memoria RAM por no ser nueva es de: '+str(descuento*100)+'%')
print('El costo total es de: US $'+str(round(total, 2)))
print()