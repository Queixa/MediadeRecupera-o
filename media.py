# Solicita as duas notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média aritmética
media = (nota1 + nota2) / 2

# Exibe a média final
print(f"\nMédia final: {media:.1f}")

# Verifica a situação do aluno
if media >= 7.0:
    print("Situação: APROVADO")
elif 5.0 <= media <= 6.9:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")