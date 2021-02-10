from operator import itemgetter
import random
import copy
import re
import sys
import argparse


def wordcount(text=None):
    if not text:
        text = input('Enter text and program will count words\n')
    text = str_processing(text)
    print("Entered text:\n" + text)

    words = text.split(" ")
    # print(words)
    words_dict = dict.fromkeys(words)
    # print(words_dict)

    text = " " + text + " "
    text = text.replace(" ", "  ")

    for word in words_dict.keys():
        words_dict[word] = text.count(" {} ".format(word), 0)
        # pattern = r" {} ".format(word)
        # words_dict[word] = len(re.findall(pattern, text))

    print("Dict with words:\n{}".format(words_dict))
    print(print_first_n_items(words_dict, 10))


def str_processing(s):
    pattern = r"[,-;!?\"']"
    s = re.sub(pattern, "", s)
    pattern = r"[ ][ ]+"
    s = re.sub(pattern, " ", s)
    return s.strip()


def printing(words):
    for key in dict(words).keys():
        print("{} - {}".format(key, words[key]))
    return


def print_first_n_items(words_dict, n):
    # print(sorted(dictItems, key=lambda num: num[1], reverse=True))
    # print(sorted(dictItems, key=itemgetter(1), reverse=True))
    sorted_dict_items = sorted(words_dict.items(), key=itemgetter(1), reverse=True)
    sorted_dict_keys = list(dict(sorted_dict_items).keys())
    return " ".join(sorted_dict_keys[:n])


# def quick_sort(nums_arr):
#     if len(nums_arr) == 0 or len(nums_arr) == 1:
#         return nums_arr
#
#     supporting_index = len(nums_arr) - 1
#     i = 0
#     while True:
#         if i >= supporting_index:
#             break
#         if nums_arr[i] >= nums_arr[supporting_index]:
#             temp = nums_arr[i]
#             nums_arr[i] = nums_arr[supporting_index - 1]
#             nums_arr[supporting_index - 1] = nums_arr[supporting_index]
#             nums_arr[supporting_index] = temp
#             supporting_index -= 1
#         else:
#             i += 1
#
#     result = quick_sort(nums_arr[:i])
#     result.append(nums_arr[i])
#     result.extend(quick_sort(nums_arr[i + 1:]))
#
#     return result


def quick_sort(nums_arr):
    if len(nums_arr) <= 1:
        return nums_arr

    supporting_index = random.randint(0, len(nums_arr) - 1)
    supporting_el = nums_arr[supporting_index]
    i = 0
    while i < len(nums_arr):
        num = nums_arr[i]
        if num < supporting_el and i > supporting_index:
            nums_arr.pop(i)
            nums_arr.insert(0, num)
            i -= 1
            supporting_index += 1
        elif num >= supporting_el and i < supporting_index:
            nums_arr.pop(i)
            nums_arr.append(num)
            i -= 1
            supporting_index -= 1
        i += 1

    left = quick_sort(nums_arr[:supporting_index])
    right = quick_sort(nums_arr[supporting_index + 1:])
    return left + [supporting_el] + right


# def quick_sort(nums_arr):
#     if len(nums_arr) <= 1:
#         return nums_arr
#
#     supporting = nums_arr.pop(random.randint(0, len(nums_arr) - 1))
#     lower = []
#     equal_and_bigger = []
#     for num in nums_arr:
#         if num < supporting:
#             lower.append(num)
#         else:
#             equal_and_bigger.append(num)
#     return quick_sort(lower) + [supporting] + quick_sort(equal_and_bigger)


def merge_sort(a, flag=False):
    print("arr = {}\nLen = {}".format(a, len(a)))
    if not flag:
        if len(a) > 2:
            arr1 = merge_sort(a[:int(len(a) / 2)])
            print("arr1 = {}".format(arr1))

            arr2 = merge_sort(a[int(len(a) / 2):])
            print("arr2 = {}".format(arr2))

            arr1.extend(arr2)
            arr1 = merge_sort(arr1, True)
            print("arr1 + arr2 = {}".format(arr1))
            return arr1

    b = a[int(len(a) / 2):]
    a = a[:int(len(a) / 2)]
    i = 0
    j = 0
    c = []
    while True:
        if i == len(a):
            while j != len(b):
                c.append(b[j])
                j += 1
            break
        if j == len(b):
            while i != len(a):
                c.append(a[i])
                i += 1
            break

        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    print("return {}".format(c))
    return c


def merge_sort2(nums_arr):
    if len(nums_arr) == 1:
        return nums_arr
    if len(nums_arr) > 1:
        left = merge_sort2(nums_arr[:int(len(nums_arr) / 2)])
        right = merge_sort2(nums_arr[int(len(nums_arr) / 2):])
        return merge_sort_help(left, right)


def merge_sort_help(sorted_arr_1, sorted_arr_2):
    i = j = 0
    c = []
    while i != len(sorted_arr_1) and j != len(sorted_arr_2):
        if sorted_arr_1[i] < sorted_arr_2[j]:
            c.append(sorted_arr_1[i])
            i += 1
        else:
            c.append(sorted_arr_2[j])
            j += 1

    c += sorted_arr_1[i:] + sorted_arr_2[j:]
    return c


def input_list(s):
    b = []
    # for i in range(100):
    #     a.append(random.randint(0, 100))

    s = s.strip()
    a = s.split(" ")
    for i in a:
        b.append(int(i))

    return b


def fibonacci_generator(count):
    prev = 1
    prev_prev = 1
    for i in range(2 if count > 2 else count):
        yield 1
    for i in range(2, count):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
        yield current


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--task_number", type=int, choices=range(1, 6), default=0)
    parser.add_argument("-f", "--file_name", type=argparse.FileType(), default=None)
    parser.add_argument("-ff", "--from_file", action="store_true", default=False)

    namespace = parser.parse_args()

    with open("file.txt", "w") as file:
        file.write("  a, c. x? a cx b d-,. x,. x x a  dfsd, cxv. cxv/ xczv; xcv;; zxc sdf.,/ \"\n")
        file.write("5 1 2 45 3 54 789 21 54621 21 0 156 123 45652\n")
        file.write("20\n")

    if not namespace.from_file and not namespace.file_name:
        if namespace.task_number == 0:
            # task 1, 2
            # wordcount()

            # task 3
            # s = input("Enter numbers\n")
            # a = input_list(s)
            a = []
            for i in range(10):
                a.append(random.randint(0, 50))

            # a = [83, 2, 40, 73, 42, 91, 42, 58, 17, 42]
            print(a)
            print("Quick sort:\n{}".format(quick_sort(a)))

            # task 4
            # print("Merge sort:\n{}".format(merge_sort2(a)))

            # additional task 1
            # for i in fibonacci_generator(int(input("Enter quantity of fibonacci numbers\n"))):
            #     print(i)
        elif namespace.task_number == 1 or namespace.task_number == 2:  # task 1, 2
            wordcount()
        elif namespace.task_number == 3:  # task 3
            a = input_list(input("Enter numbers\n"))
            print(quick_sort(a))
        elif namespace.task_number == 4:  # task 4
            a = input_list(input("Enter numbers\n"))
            print(merge_sort2(a))
        elif namespace.task_number == 5:  # task 5
            for i in fibonacci_generator(int(input("Enter quantity of numbers\n"))):
                print(i)

    else:  # reading data from file
        namespace.file_name = open("file.txt", "r+")
        with namespace.file_name as file:
            lines = file.readlines()

            # task 1, 2
            print("Task 1 and 2\n" + lines[0])
            wordcount(lines[0])

            # task 3
            print("\nTask 3\n" + lines[1])
            a = input_list(lines[1])
            print("Quick sort:\n{}".format(quick_sort(a)))

            # task 4
            print("Merge sort:\n{}".format(merge_sort2(a)))

            # additional task 1
            print("\nAdditional task 1\n" + lines[2])
            # print(fibonacci_generator(int(lines[2])))
            for i in fibonacci_generator(int(lines[2])):
                print(i)
    return 0

    # parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # parser.add_argument('-q', '--quick', type=test)
    # return parser.parse_args()


def create_my_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--task_number", type=int, choices=range(6))
    parser.add_argument("-f", "--file_name", type=argparse.FileType(), default=open("file.txt"))
    # parser.add_argument("")

    namespace = parser.parse_args()
    print(namespace.task_number)
    print(namespace.file_name.read())

    return namespace


if __name__ == '__main__':
    main()
