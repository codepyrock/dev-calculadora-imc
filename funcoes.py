import re

# calcular IMC
def calcular_imc(peso, altura):
    peso = float(peso)
    altura = float(altura)
    imc = round(peso / (altura**2), ndigits=2)
    return imc

# estabelecer parâmetros do IMC
cores_imc = {
    "Muito abaixo do peso": "#0000FF",   # Azul
    "Abaixo do peso": "#00BFFF",         # Azul claro
    "Peso normal": "#00FF00",            # Verde
    "Acima do peso": "#FFFF00",          # Amarelo
    "Obesidade I": "#FFA07A",            # Laranja claro
    "Obesidade II (severa)": "#FFA500",  # Laranja
    "Obesidade III (mórbida)": "#FF0000" # Vermelho
}

# estabelecer a categoria
def categoria_imc(imc):
    if imc > 40:
        return "Obesidade III (mórbida)"
    elif imc  >= 35 and imc <= 39.9:
        return "Obesidade II (severa)"
    elif imc  >= 30 and imc <= 34.9:
        return "Obesidade I"
    elif imc  >= 25 and imc <= 29.9:
        return "Acima do peso"
    elif imc  >= 18.5 and imc <= 24.9:
        return "Peso normal"
    elif imc  >= 17 and imc <= 18.5:
        return "Abaixo do peso"
    else:
        return "Muito abaixo do peso"

# definindo a cor
def definir_cor(valor):
    if valor in cores_imc:
        return cores_imc[valor]

# validar peso e altura
def validar_valor(peso):
    valor_validado = re.match(r'\d', peso)    
    if valor_validado:
        return "Valor validado"
    else:
        return "Digite apenas números"
  

# formatar peso e altura
def formatar_valor(valor_user):
    valor_user = valor_user.strip()
    if ',' in valor_user:
        valor_user = re.sub(r',', '.', valor_user)
    valor_formatado = f'{round(float(valor_user), 2):.2f}'
    return valor_formatado

