print("*****Olá eu sou o seu App de Consumo de Água diário*****\n")

nome = input("Por favor nos informe seu nome: ")

validacaoWapp = False
while validacaoWapp == False:
    numero = input("Por favor nos informe seu numero do Whatsapp: ")
    if numero.isdigit() and len(numero) >= 9:
        validacaoWapp = True
    else:
        print("Por favor digite um número correto!")


while True:
    try: 
        peso = float(input("Por favor nos informe seu peso: ").replace(",", "."))
        break
    except:
        print("Por favor digite um peso válido!")

while True:
    try: 
        altura = float(input("Por favor nos informe sua altura: ").replace(",", "."))
        break
    except:
        print("Por favor digite uma altura válida!")
        
imc = peso/(altura*altura)
if imc < 18.5:
    resultadoIMC = "Abaixo do peso"
if imc > 18.5 and imc < 24.9: 
    resultadoIMC = "Peso normal"
if imc > 24.9 and imc < 29.9:
    resultadoIMC = "Sobrepeso"
if imc > 29.9 and imc < 34.9: 
    resultadoIMC = "Obesidade grau 1 (leve)"
if imc > 34.9 and imc < 39.9:
    resultadoIMC = "Obesidade grau 2 (moderada)"
if imc > 39.9: 
    resultadoIMC = "Obesidada grau 3 (mórbida)"
    
totalDeAguaDiario = peso*0.035

print("\n----Resultados----\nNome: " + nome + "\nWhatsapp: " + numero + f'\nPeso: {peso}\nAltura: {altura}\nConsumo de água: {totalDeAguaDiario:.2f} litros'
      f'\nIMC: {imc:.2f}\nCondição: {resultadoIMC}' )
    