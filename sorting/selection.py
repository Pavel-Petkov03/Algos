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
        if len(self) > 1:
            middle_index = len(self) // 2
            left = self[:middle_index]
            right = self[middle_index:]

            Sort.merge_sort(left)
            Sort.merge_sort(right)

            left_merge_index = 0
            right_merge_index = 0
            global_index = 0

            while left_merge_index < len(left) and right_merge_index < len(right):
                if left[left_merge_index] <= right[right_merge_index]:
                    self[global_index] = left[left_merge_index]
                    left_merge_index += 1
                else:
                    self[global_index] = right[right_merge_index]
                    right_merge_index += 1
                global_index += 1

            while left_merge_index < len(left):
                self[global_index] = left[left_merge_index]
                left_merge_index += 1
                global_index += 1

            while right_merge_index < len(right):
                self[global_index] = right[right_merge_index]
                global_index += 1
                right_merge_index += 1

        return self

    def quick_sort(self, pointer):
        pass

    def __swap(self, first_index, second_index):
        self[first_index], self[second_index] = self[second_index], self[first_index]


ls = Sort([12, 1, 33, 5, -12, 22, 654364, 12, 13, -1,124421,-421421])
print(ls.bubble_sort())
