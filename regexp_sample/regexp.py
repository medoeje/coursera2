def calculate(data, findall):
    matches = findall(r"([abc])([\+-])?(=)([abc]?)([\+-]?\d*)")  # Если придумать хорошую регулярку, будет просто
    for v1, r, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        # data[v1] = data.get(v2, 0) + int(n or 0)
        right_part = data.get(v2, 0) + int(n or 0)
        if r:
            if r=='+':
                data[v1] = data.get(v1, 0) + right_part
            elif r=='-':
                data[v1] = data.get(v1, 0) - right_part
        else:
            data[v1] = right_part
    return data
