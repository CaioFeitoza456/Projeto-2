"""
Calculadora Simples

O usuário deve poder fazer operções
básicas, como adição, subtração, 
divisão e multiplicação.
"""


def tenta_mudar_tipo(valor):
    try:
        # Tenta transformar o índice digitado
        # pelo usuário em um número inteiro
        return float(valor)
       
    except ValueError:
        # Se der erro de valor(o usuário passar
        # uma string, por exemplo) ele cai aqui
        # na exceção
        print("Digite apenas números.")


def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


while True:
    primeiro_numero = input("Digite o primeiro número: ")
    numero_um_float = tenta_mudar_tipo(primeiro_numero)
        
    if numero_um_float is None:
            continue
        
    break
    
while True:
    segundo_numero = input("Digite o segundo número: ")
    numero_dois_float = tenta_mudar_tipo(segundo_numero)
        
    if numero_dois_float is None:
        continue
        
    break


while True:
    
    print("""
      ◇◇MENU DE OPÇÕES◇◇
      1. Adição (+)
      2. Subtração (-)
      3. Multiplicação (*)
      4. Divisão(/)
    """)
    
    operador = input("Digite aqui: ")
    
    if operador == "1":
        # Soma
        resultado = sum(numero_um_float, numero_dois_float)
        print(f"Resultado: {resultado:.2f}")
        break
            
    elif operador == "2":
        # Subtração
        resultado = subtracao(numero_um_float, numero_dois_float)
        print(f"Resultado: {resultado:.2f}")
        break
            
    elif operador == "3":
        # Multiplicacao
        resultado = multiplicacao(numero_um_float, numero_dois_float)
        print(f"Resultado: {resultado:.2f}")
        break
            
    elif operador == "4":
        # Divisão
        resultado = divisao(numero_um_float, numero_dois_float)
        print(f"Resultado: {resultado}")
        break
        
    else:
        print("Você não digitou uma opção do menu.")
        continue
