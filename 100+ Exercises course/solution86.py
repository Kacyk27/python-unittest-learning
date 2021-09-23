def filter_ge_four_char(words):
    x = []
    for i in words:
        if len(i) >= 4:
            x.append(i)

    return x