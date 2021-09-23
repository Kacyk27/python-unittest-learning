def map_longest(words):
    if words == []:
        return 0
    else:
        x=[]
        for i in words:
            x.append(len(i))
        return max(x)