"""Métodos para concatenar"""
word = "Ada Lovelace"

# Se puede concatenar se muchas formas

# 1°
# Usando el operador de adición
print("La primera programadora fue " + word )

# 2°
# La llaves indican que allí se va a reemplazar un valor específico, usando también el método format
print("La primera programadora fue {}".format(word))


# 3°
# Usando f-string
print(f"La primera programadora fue {word}")