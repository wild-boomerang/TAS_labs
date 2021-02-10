import random
import tempfile


# def ext_merge_sort(file_name):
#     file = open(file_name, "r+")
#     temp_1 = open("temp_1", "w+")
#     temp_2 = open("temp_2", "w+")
#
#     while True:
#         file.seek(0)
#         print("file:\n\n" + file.read())
#         file.seek(0)
#
#         prev_num = 0
#         isFirst = True
#         prev_file = temp_1
#
#         for line in file:
#             if isFirst:
#                 prev_file = temp_1
#                 prev_file.write(line)
#                 isFirst = False
#                 prev_num = int(line)
#             elif int(line) >= prev_num:
#                 prev_file.write(line)
#                 prev_num = int(line)
#             else:
#                 prev_file.write("\'\n")  # the end of the series
#                 prev_file = temp_2 if prev_file == temp_1 else temp_1
#                 prev_file.write(line)
#                 prev_num = int(line)
#
#         # merger
#         # com_file = open("common_temp", "w")
#         # file.seek(0)
#         file.close()
#         file = open(file_name, "w+")
#         temp_1.seek(0)
#         print("temp_1:\n\n" + temp_1.read())
#         temp_1.seek(0)
#         temp_2.seek(0)
#         print("temp_2:\n\n" + temp_2.read())
#         temp_2.seek(0)
#
#         series_quantity = temp_1.read().count("\'\n") + 1
#         if series_quantity == 1:
#             break
#         temp_1.seek(0)
#         temp_2.seek(0)
#
#         for i in range(series_quantity):
#             buf_1 = []
#             buf_2 = []
#             for line in temp_1:
#                 if line != "\'\n" and line != "\n":
#                     buf_1.append(int(line))
#                 else:
#                     break
#
#             for line in temp_2:
#                 if line != "\'\n" and line != "\n":
#                     buf_2.append(int(line))
#                 else:
#                     break
#
#             file.write(merge_sort_help(buf_1, buf_2))
#             # print(merge_sort_help(buf_1, buf_2))
#
#         file.seek(0)
#         print("file:\n\n" + file.read())
#         file.seek(0)
#         # temp_1.seek(0)
#         # temp_2.seek(0)
#         temp_1.close()
#         temp_1 = open(file_name, "w+")
#         temp_2.close()
#         temp_2 = open(file_name, "w+")
#
#     temp_files.append(open("temp_{}.txt".format(temp_quantity), "w+"))  # todo temp/temp_{}.txt
#
#     file.close()
#     temp_1.close()
#     temp_2.close()


def merge_sort(nums_arr):
    if len(nums_arr) == 1:
        return nums_arr
    if len(nums_arr) > 1:
        left = merge_sort(nums_arr[:int(len(nums_arr) / 2)])
        right = merge_sort(nums_arr[int(len(nums_arr) / 2):])
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


def ext_merge_sort(file_name, size=100):
    with open(file_name, "r") as file:
        # sorting each file
        temp_quantity = 0
        temp_files = []
        while True:
            nums = []
            for _ in range(size):
                num = file.readline()
                if num != "":
                    nums.append(int(num))
                else:
                    break
            if len(nums) == 0:
                break

            nums = merge_sort(nums)

            temp_files.append(tempfile.NamedTemporaryFile(mode="w+"))
            temp_files[temp_quantity].writelines("{}\n".format(i) for i in nums)

            print(temp_quantity)
            temp_quantity += 1

    # file.close()

    # print(temp_quantity)

    # nums = []
    # for i in range(temp_quantity):
    #     # nums.append(open("temp_{}.txt".format(i), "r+").readline())
    #     i_temp = open("temp_{}.txt".format(i), "r+")
    #     for _ in range(int(size / (temp_quantity + 1))):
    #         num = i_temp.readline()
    #         if num != "":
    #             nums.append(int(num))
    #         else:
    #             break
    #
    # print(len(nums))

    nums = []
    i = 0
    for temp in temp_files:
        temp.seek(0)
        nums.append((int(temp.readline()), i))
        i += 1

    # print(nums)
    with open("sorted_nums2.txt", "w") as answer_file:
        to_stop = 0
        while to_stop != temp_quantity:
            min_number = min(nums)
            nums.remove(min_number)
            answer_file.writelines("{}\n".format(min_number[0]))
            num = temp_files[min_number[1]].readline()
            if num != "":
                nums.append((int(num), min_number[1]))
            else:
                to_stop += 1

        for temp in temp_files:
            temp.close()


def main():
    with open("test_nums.txt", "w") as file:
        file.writelines("{}\n".format(_) for _ in range(953, -1, -1))
        file.writelines("{}\n".format(random.randint(-1000000, 1000000)) for _ in range(900))

    ext_merge_sort("test_nums.txt", 100)


if __name__ == "__main__":
    main()
