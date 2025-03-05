"""
Calculadora Simples

O usuário deve poder fazer operções
básicas, como adição, subtração, 
divisão e multiplicação.
"""


def tenta_mudar_para_float(valor):
    try:
        return float(valor)
       
    except ValueError:
        return None


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


while True:
    primeiro_numero = input("Digite o primeiro número: ")
    numero_um_float = tenta_mudar_para_float(primeiro_numero)
        
    if numero_um_float is None:
            continue
        
    break
    
while True:
    segundo_numero = input("Digite o segundo número: ")
    numero_dois_float = tenta_mudar_para_float(segundo_numero)
        
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
        resultado = numero_um_float + numero_dois_float
        print(f"Resultado: {resultado:.2f}")
        break
            
    elif operador == "2":
        # Subtração
        resultado = numero_um_float - numero_dois_float
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
