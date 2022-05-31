def comb(array, n, k, index=0):
    if index == k:
        print(" ".join([str(c) for c in array]))
        return
    for i in range(1, n + 1):
        array[index] = i
        comb(array, i, k, index + 1)


n = int(input())
k = int(input())

comb([None] * k, n, k)
