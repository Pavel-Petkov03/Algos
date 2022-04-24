empty = "_"
wall = "*"


class Solve:
    """
        * means a wall
        _ means not visited path
        x means  visited path
        e means exit
    """

    def __init__(self, matrix):
        self.matrix = matrix

    def main(self, row=0, col=0):

        if not (0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[row])):
            return
        if self.is_exit(row, col):
            print("Path found")
            print()
            self.print_solution()
            print()
        elif self.is_not_visited(row, col) and self.is_passable(row, col):
            self.mark(row, col)
            self.main(row + 1, col)
            self.main(row - 1, col)
            self.main(row, col - 1)
            self.main(row, col + 1)
            self.unmark(row, col)

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


m = [
    [empty, empty, empty, wall, empty, empty, empty, ],
    [wall, wall, empty, wall, empty, wall, empty],
    [empty for _ in range(7)],
    [empty, *[wall for _ in range(5)], empty],
    [*[empty for _ in range(6)], "e"],

]
s = Solve(m)
s.main()
