empty = "_"
wall = "*"


class Solve:
    """
        * means a wall
        _ means not visited path
        x means  visited path
        e means exit
    """

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.matrix = self.initial_matrix()
        self.dir_tracer = []

    def initial_matrix(self):
        ls = []
        for row in range(self.row):
            ls.append([])
            line = input()
            for col in line:
                ls[row].append(col)
        return ls

    def main(self, row=0, col=0, direction="L"):
        if not (0 <= row < self.row and 0 <= col < self.col):
            return
        self.dir_tracer.append(direction)
        if self.is_exit(row, col):
            print("".join(self.dir_tracer[1:]))
        elif self.is_not_visited(row, col) and self.is_passable(row, col):
            self.mark(row, col)
            self.main(row, col + 1, "R")
            self.main(row + 1, col, "D")
            self.main(row - 1, col, "U")
            self.main(row, col - 1, "L")
            self.unmark(row, col)
        self.dir_tracer.pop()

    def print_solution(self):
        [print("".join(m)) for m in self.matrix]

    def is_exit(self, row, col):
        return self.matrix[row][col] == "e"

    def is_not_visited(self, row, col):
        return self.matrix[row][col] != "x"

    def is_passable(self, row, col):
        return self.matrix[row][col] != "*"

    def mark(self, row, col):
        self.matrix[row][col] = "x"

    def unmark(self, row, col):
        self.matrix[row][col] = "_"


row = int(input())
col = int(input())
Solve(row, col).main()
