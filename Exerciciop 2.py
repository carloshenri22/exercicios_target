def contar_a(string):
    return string.lower().count('a')

# String a ser analisada
texto = input("Informe uma string: ")
quantidade_a = contar_a(texto)
print(f"A letra 'a' aparece {quantidade_a} vez(es) na string.")