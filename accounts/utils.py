def percentage_counter(int1, int2):
    c = (int1 - int2) / int2 * 100
    c = round(c, 1)
    if c == 0:
        return f"{c}"
    return f'{c}%'
