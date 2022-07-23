def wav(l, w):
    num = 0
    ct = len(l)
    if w == 1:
        for i in range(ct):
            num += l[i]
    else:
        for i in range(ct):
            num += l[i] * w[i]
    return num/ct

def similar(l, c):
    a = []
    b = []
    for i in range(len(l)):
        for j in range(len(i)):
            a.append(l[j[i]])
        b.append(wav(a, 0))
        a.clear()
    ret = wav(b, 0)
    if c <= ret:
        ret -= c
        return ret
    else:
        c -= ret
        return c

def compare(iris, seg, ids, c):
    a = []
    newc = wav(c, 0)
    pseg = 0
    for i in seg:
        a.append(similar(iris[pseg:i], newc))
        pseg = i
    m = min(a)
    ret = []
    d = []
    for i in range(len(a)):
        if a[i] == min(a):
            ret.append[i]
    for i in range(len(ret)):
        d.append(ids[i])
    print('this flower is most likely to be' + d)
