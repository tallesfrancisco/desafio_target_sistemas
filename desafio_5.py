def inverter_string(texto : str):
    return texto[::-1]

# Exemplo de uso da função

string : str = "Estágio Ribeirão Preto - 2024"
string_inversa : str = inverter_string(string)

print(f"String original :\n{string}")
print(f"String invertida :\n{string_inversa}")