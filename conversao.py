n = int(input())
horas = n/3600
r = n%3600
minutos = r/60
segundos = r%60
print("%i:%i:%i"%(horas,minutos,segundos))
