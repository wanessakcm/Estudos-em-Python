minha_string = "qualquer texto"
               #01234567891111
               #          0123

print(f"concatenar {minha_string} em string")


print(minha_string.upper())

print(minha_string.lower())

print(minha_string.capitalize())

print(minha_string.isupper())

print(minha_string.islower())

print(minha_string.replace("qualquer", "meu"))

print(minha_string.replace("u", "U",1))

print(len(minha_string))

print(minha_string[2:5])

print(minha_string[-4:-1])

print(minha_string.index("texto"))

x = "texto" in minha_string
print(x)

y = "linha 1, \nlinha 2,\nlinha 3"
print(y)