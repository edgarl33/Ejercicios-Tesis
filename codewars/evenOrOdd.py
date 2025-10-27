#Crear una función que determine si un número es par o impar

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#Intercambiar los valores de dos variables. 
x = 'A'
y = 'B'

print(x,y)

temp = y
print(temp)

y=x
x=temp
print(x,y )

