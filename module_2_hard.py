def code_(n):
    pair = []
    pairs = []
    for i in range(1, n):
        for j in range(i+1, n):
            ij=i+j
            if n % ij == 0 and i != j:
                pair = []
                pair.append(i)
                pair.append(j)
                spair = sorted(pair)
                pairs.append(spair)
    return(n, pairs)

input_ = int(input("введите число от 3 до 20: "))
z, pairs1 = code_(input_)
print(z, ''.join(map(lambda b: ''.join(map(str, b)), pairs1)))