#!/usr/bin/python

PI= 3.14155926535897931159979634685441852
def aproximacion_PI(n):
  if(n!=0):
    
    suma = 0.0
    for i in range(1,n+1):
      x_i=(i-0.5)/float(n)
      fx_i=4/(1+x_i*x_i)
      b=i/float(n)
      a = b-(1 / float(n))
      suma=suma+fx_i

      PI_i=suma/float(n)

  return PI_i
n = int(raw_input('Introduzca el valor de intervalos: '))
m= int(raw_input('Introduzca el numero de veces que se repetira la funcion: '))
print aproximacion_PI(n)
n=0
l=[]
for j in range(1,m+1):
 aproximacion_PI(j*m)
 l=l+[PI]
    
print l


  