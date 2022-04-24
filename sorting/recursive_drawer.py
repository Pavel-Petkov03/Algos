def recurse_drawer(n):
    if n == 0:
        return
    print(n * "*")
    recurse_drawer(n - 1)
    print(n * "#")


recurse_drawer(7)


def fact(n):
    glob = 1
    for multiply in range(2, n + 1):
        glob *= multiply
    return glob




def generate_n_vectors_0_and_1(n, vector):
    if n >= len(vector):
        print(vector)
        return

    for i in range(9):
        vector[n] = i
        generate_n_vectors_0_and_1(n + 1, vector)


