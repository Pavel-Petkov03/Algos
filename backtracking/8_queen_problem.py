QUEEN = "Q"


class BoardChecker:
    def __init__(self, row, col, matrix):
        self.row = row
        self.col = col
        self.matrix = matrix

    def horizontal_checker(self):
        for col in range(len(self.matrix)):
            if self.matrix[self.row][col] == QUEEN:
                return False
        return True

    def vertical_checker(self):
        for row in range(len(self.matrix)):
            if self.matrix[row][self.col] == QUEEN:
                return False
        return True

    def diagonal_checker(self):
        for left_wing in range(1, self.col + 1):
            if self.row - left_wing >= 0 and self.col - left_wing >= 0 and self.matrix[self.row - left_wing][
                self.col - left_wing] == QUEEN:
                return False
            if left_wing + self.row in range(len(self.matrix)) and self.col - left_wing >= 0 and \
                    self.matrix[left_wing + self.row][self.col - left_wing] == QUEEN:
                return False

        for right_wing in range(1, len(self.matrix) - self.col):
            if right_wing + self.row in range(len(self.matrix)) and self.col + right_wing < len(self.matrix) and \
                    self.matrix[self.row + right_wing][self.col + right_wing] == QUEEN:
                return False
            if self.row - right_wing >= 0 and self.col + right_wing < len(self.matrix) and \
                    self.matrix[self.row - right_wing][self.col + right_wing] == QUEEN:
                return False

        return True

    def validate(self):
        return self.diagonal_checker() and self.horizontal_checker() and self.vertical_checker()


class Solver:
    def __init__(self):
        self.matrix = self.__generate_empty_matrix()
        self.count = 0
        self.counter = 0

    @staticmethod
    def __generate_empty_matrix():
        return [["x" for x in range(8)] for _ in range(8)]

    def print_ready_solution(self):
        [print("".join(c)) for c in self.matrix]

    def main(self):
        if self.count == 8:
            self.print_ready_solution()
            print()
            return True
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix)):
                if BoardChecker(row, col, self.matrix).validate():
                    self.matrix[row][col] = QUEEN
                    self.count += 1
                    if self.main():
                        return True
                    self.matrix[row][col] = "x"
                    self.count -= 1
        return False


s = Solver()
s.main()
