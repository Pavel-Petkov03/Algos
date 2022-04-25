from collections import deque


class Sort(list):

    def selection_sort(self):
        for left_most_index in range(len(self)):
            min_number = self[left_most_index]
            swappable_index = left_most_index
            for finder_index in range(left_most_index + 1, len(self)):
                if self[finder_index] < min_number:
                    min_number = self[finder_index]
                    swappable_index = finder_index
            self.__swap(swappable_index, left_most_index)
        return self

    def bubble_sort(self):
        for left_most_index in range(len(self)):
            for finder_index in range(left_most_index + 1, len(self)):
                if self[finder_index] < self[left_most_index]:
                    self.__swap(finder_index, left_most_index)
        return self

    def insertion_sort(self):
        for left_most_index in range(1, len(self)):
            key = self[left_most_index]
            finding_index = left_most_index - 1
            while finding_index >= 0 and key < self[finding_index]:
                self[finding_index + 1] = self[finding_index]
                finding_index -= 1
            self[finding_index + 1] = key
        return self

    def merge_sort(self):
        if len(self) == 1:
            return
        middle_index = len(self) // 2
        left_part = self[:middle_index]
        right_part = self[middle_index:]

        Sort.merge_sort(left_part)
        Sort.merge_sort(right_part)

        left_index = 0
        right_index = 0
        global_index = 0

        while left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index] < right_part[right_index]:
                self[global_index] = left_part[left_index]
                left_index += 1
            else:
                self[global_index] = right_part[right_index]
                right_index += 1
            global_index += 1

        while left_index < len(left_part):
            self[global_index] = left_part[left_index]
            left_index += 1
            global_index += 1
        while right_index < len(right_part):
            self[global_index] = right_part[right_index]
            global_index += 1
            right_index += 1
        return self

    def quick_sort(self, pointer):
        pass

    def __swap(self, first_index, second_index):
        self[first_index], self[second_index] = self[second_index], self[first_index]


ls = Sort([12, 1, 33, 5, -12, 22, 654364, 12, 13, -1, 124421, -421421])
print(ls.merge_sort())


