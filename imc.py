def numero_quadrado(numero):
  quadrado = numero * numero
  return quadrado

def imc(peso, altura):
  altura_quadrada = altura ** 2
  meu_imc = peso / altura_quadrada
  print(f'O meu imc é {meu_imc:.2f}')
  return meu_imc

meu_imc = imc(103 , 1.80)