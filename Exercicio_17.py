peso = float(print("Diga o seu peso "))
altura = float(print("Diga a sua altura "))
imc = peso / (altura * altura)

print(f"Seu IMC é: {imc}")

if(imc > 25):
    print("Acima do peso ideal.")
else:
    print("Peso ok.")