class Solve:
    """
    find all solutions of equation with horner function
    """

    def __init__(self, *args):
        self.equation = list(args)

    def main(self):
        first = self.equation[0]
        last = self.equation[-1]
        all_combinations = self.generate_all_combinations(first, last)
        for probable_x in all_combinations:
            new_equation = self.generate_probable_solution(probable_x)
            if new_equation[-1] == 0:
                print(f"{probable_x} is solution")
                self.equation.pop()

    def generate_probable_solution(self, probable_x):
        new_equation = [self.equation[0]]
        start_point = self.equation[0]
        for index in range(1, len(self.equation)):
            start_point = probable_x * start_point + self.equation[index]
            new_equation.append(start_point)
        return new_equation

    @staticmethod
    def generate_all_valid_combinations(n) -> set:
        """
        accepts first and last argument and finds all delimiters
        :param n:
        :return: list[tuple]
        """
        result = set()
        for index in range(1, n + 1):
            if n % index == 0:
                result.add(index)
        return result

    def generate_all_combinations(self, first, last):
        """
        this function takes the highest powered and lowest powered x and returns all valid x
        :param first: int
        :param last: int
        :return: set
        """

        first_comb = self.generate_all_valid_combinations(first)
        last_comb = self.generate_all_valid_combinations(last)

        res = first_comb.union(last_comb)
        for last_num in last_comb:
            for first_num in first_comb:
                res.add(last_num / first_num)
        return res


r = Solve(1, -2, -5, 6)
r.main()
# х3 - 2х2 - 5х + 6
