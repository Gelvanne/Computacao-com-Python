n=int(input('Digite o valor se n:',))
c=n
f=1
print('Calculando{}!='.format(n), end='')
while c>0:
  print('{}'.format(c), end='')
  print('x' if c>1 else'=', end='')
  f=f*c
  c= c-1
print('{}'.format(f))