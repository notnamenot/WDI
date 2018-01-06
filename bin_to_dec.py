b=input("Podaj liczbę w sysytemie binarnym:\n")
 
def bin_to_dec(b):
  d=0
  for i in range(len(b)):
    d=d+2**(len(b)-i-1)*int(b[i])
  return d

print("Ta liczba w systemie dziesiętnym to", bin_to_dec(b))  
