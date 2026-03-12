a,b,c = map(float,input().split())

d = (a*c)/2
d2 = 3.14159 * c**2
d3 = ((a+b)*c)/2
d4 = b**2
d5 = a*b 

print("TRIANGULO: %.3f" %d)
print("CIRCULO: %.3f" %d2)
print("TRAPEZIO: %.3f" %d3)
print("QUADRADO: %.3f" %d4)
print("RETANGULO: %.3f" %d5)