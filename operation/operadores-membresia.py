a = "casa"
valor = 's' in "casa" # esta dentro de
print(valor)

b = "hombre"
valor1 = "s" not in "hombre" # no esta dentro de
print(valor1)

# Operadores de Identidad ( is, is not )
# Verifican si dos variables apuntan al mismo objeto en memoria.
x = [1, 2]
y = x
z = [1, 2]
print(x is y)
print(x is z)
