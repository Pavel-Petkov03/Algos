taken_pos = "x"


class Solve:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.matrix = self.init_matrix()
        self.result = []

    def init_matrix(self):
        return [input().split(" ") for _ in range(self.row)]

    def main(self, row=0, col=0):
        if row == self.row or col == self.col or self.matrix[row][col] == taken_pos:
            return
        self.result.append(self.matrix[row][col])
        self.matrix[row][col] = taken_pos

        self.main(row, col + 1)
        self.main(row + 1, col)
        self.main(row, col - 1)
        self.main(row - 1, col)


r = int(input())
c = int(input())

res_instance = Solve(r, c)
res_instance.main()
print(" ".join(res_instance.result))
