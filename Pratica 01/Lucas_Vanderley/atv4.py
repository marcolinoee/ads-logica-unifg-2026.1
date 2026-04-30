idade = int(input("Digite sua idade: "))
experiencia = int(input("Digite sua experiência: "))

acesso = idade >= 18 and experiencia >= 2

print("=" * 30)
print(f"Seu acesso foi {acesso}...")
print("=" * 30)