word = input()
while word != "End":
    if word == "SoftUni":
        word = input()
    print("".join([f"{c}{c}" for c in word]))
    word = input()


