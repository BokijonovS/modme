def percentage_counter(int1, int2):
    a = int2 - int1
    b = int2 / 100
    c = a / b
    c = round(c, 1)
    if c == 0:
        return f"{c}"
    return f'{-c}%'
