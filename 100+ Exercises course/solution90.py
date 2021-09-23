def is_distinct(items):
    x=[]
    for i in items:
        if i not in x:
            x.append(i)
    if len(items) == len(x):
        return True
    else:
        return False