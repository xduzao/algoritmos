# Exercicio 1
def mult(x, y):
    if x == 1:
        return y
    else:
        return y + mult(x - 1, y)


print(mult(3, 4))


# Exercicio 2

def div(x, y):
    if x < y:
        return 0
    else:
        return 1 + div(x - y, y)


print(div(13, 4))


# Exercicio 3

def resto(x, y):
    if x < y:
        return x
    else:
        return resto(x - y, y)


print(resto(13, 4))


# Exercicio 4

def elevado(x, y):
    if y == 1:
        return x
    else:
        return x * elevado(x, y - 1)


print(elevado(4, 5))
