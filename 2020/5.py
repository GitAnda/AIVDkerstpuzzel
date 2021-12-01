_1 = {2, 3, 5, 7}
_1 = {2, 5}
_7 = {1, 4, 9}

print("1:", _1)
print("7:", _7)

print("\n5^8=67")
_5, _8, _6 = set(), set(), set()
for e in range(10):
    for h in range(10):
        x = pow(e, h)
        if 9 < x < 100 and x%10 in _7:
            if e is not h and e is not x//10 and e is not x%10 and h is not x//10 and h is not x%10 and x//10 is not x%10:
                print("{}^{} = {}".format(e, h, x))
                _5.add(e)
                _8.add(h)
                _6.add(x//10)

print("\n5:", _5)
print("6:", _6)
print("8:", _8)

print("\n2*6=84")
_2, _4 = set(), set()
for b in range(10):
    for d in range(10):
        for _f in _6:
            x = b*_f
            if 9 < x < 100 and x // 10 in _8 and x % 10 == d:
                if b is not _f and b is not x//10 and b is not x%10 and _f is not x//10 and _f is not x%10 and x//10 is not x%10:
                    print("{}*{} = {}".format(b, _f, x))
                    _2.add(b)
                    _4.add(d)

print("\n2:", _2)
print("4:", _4)

print("\n97-50=11")
_0, _9 = set(), set()
for i in range(10):
    for j in range(10):
        for _g in _7:
            for _e in _5:
                x1 = i * 10 + _g
                x2 = _e * 10 + j
                x = x1 - x2
                if 9 < x < 100 and x//10 == x%10 and x%10 in _1:
                    # print("{}-{} = {}".format(x1, x2, x))
                    if i is not _g and i is not _e and i is not j and i is not x%10 and _g is not _e and _g is not j and _g is not x%10 and _e is not j and _e is not x%10 and j is not x%10:
                        print("{}-{} = {}".format(x1, x2, x))
                        _0.add(j)
                        _9.add(i)

print("\n0:", _0)
print("9:", _9)

for a in _1:
    for b in _2:
        for d in _4:
            for e in _5:
                for f in _6:
                    for g in _7:
                        for h in _8:
                            for i in _9:
                                for j in _0:
                                    c = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.difference({a, b, d, e, f, g, h, i, j})
                                    if len(c) == 1:
                                        c = c.pop()

                                        if pow(e, h) == f*10+g:
                                            if b*f == h*10+d:
                                                if i*10+g - (e*10+j) == 11*a:
                                                    print(a, b, c, d, e, f, g, h, i, j)
                                                    print(b*11*a*(b*1000+j*100+a*10+c))