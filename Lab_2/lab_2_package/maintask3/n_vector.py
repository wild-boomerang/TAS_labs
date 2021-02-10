class NVector:
    def __init__(self, other_list=None):
        if other_list is None:
            other_list = []
        self.elements = other_list
        self._idx = 0

    def append(self, n):
        self.elements.append(n)

    def __add__(self, other):
        self.__len_check(other)

        i = 0
        res = NVector()
        while i < len(self):
            res.append(self.elements[i] + other[i])
            i += 1
        return res

    def __sub__(self, other):
        self.__len_check(other)

        i = 0
        res = NVector()
        while i < len(self):
            res.append(self.elements[i] - other[i])
            i += 1
        return res

    def __mul__(self, other):
        i = 0
        res = NVector()

        if isinstance(other, int) or isinstance(other, float):
            while i < len(self):
                res.append(self.elements[i] * other)
                i += 1
        else:
            self.__len_check(other)
            while i < len(self):
                res.append(self.elements[i] * other[i])
                i += 1
        return res

    def __eq__(self, other):
        if len(other) != len(self):
            return False

        i = 0
        while i < len(self):
            if self[i] != other[i]:
                return False
            i += 1
        return True

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, key, value):
        self.elements[key] = value

    def __delitem__(self, key):
        return self.elements.pop(key)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_value = self.elements[self._idx]
            self._idx += 1
            return next_value
        except IndexError:
            self._idx = 0
            raise StopIteration

    def __contains__(self, item):
        for elem in self.elements:
            if elem == item:
                return True
        return False

    def __str__(self):
        return str(self.elements)

    def __len_check(self, other):
        if len(other) != len(self):
            raise ValueError("Vector lengths do not match")


# def main():
#     vector = NVector()
#     vector.append(5)
#     vector.append(2)
#     print(vector)
#
#     print(vector)
#     vector[0] = 5
#     print(vector)
#
#     if 5 in vector:
#         print("Yes")
#     else:
#         print("No")
#
#     # vector.__delitem__(1)
#     # print(vector)
#
#     for elem in vector:
#         print(elem)
#
#     for elem in vector:
#         print(elem)
#
#     result = vector + [1, 1]
#     print(result)
#
#     vector2 = NVector([2, 2])
#     vector += vector2
#     print(vector)
#
#     vector -= vector2
#     print(vector)
#
#     vector *= vector2
#     print(vector)
#
#     vector *= 0
#     print(vector)
#
#     vector += (3, 5)
#     print(vector)
#
#     print(vector == NVector((3, 5)))
#     # print(len(vector))
#     print(str(vector))
#
#
# if __name__ == "__main__":
#     main()
