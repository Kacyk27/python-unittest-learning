def count_string(items):
    x=[]
    for i in items:
        if type(i) == str:
            x.append(i)
    return len(x)