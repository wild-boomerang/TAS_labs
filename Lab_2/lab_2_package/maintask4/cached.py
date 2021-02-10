# def my_decorator_example(func_to_decorate):
#     def new_func():
#         print("tugugun")
#         func_to_decorate()
#         print("tugugun again")
#
#     return new_func
#
#
# @my_decorator_example
# def func_for_decoration():
#     print("Hello, world!")


def cached(func):
    def wrapper(*args, **kwargs):
        sorted_kwargs_items = sorted(kwargs.items(), key=lambda item: item[0])  # sorting named attrs
        # print(sorted_kwargs_items)

        if len(sorted_kwargs_items) == 0:
            t = args
        else:
            t = (args, tuple((dict(sorted_kwargs_items).values())))  # keys of saved values dict
        # print(t)

        res = wrapper.res_dict.get(t)

        if res is None:
            wrapper.res_dict[t] = func(*args, **kwargs)
            return wrapper.res_dict[t]
        else:
            print("Printing previously saved value")
            return res

    wrapper.res_dict = {}
    return wrapper


@cached
def test_func(arg1, arg2, named="named arg", g=0):
    return arg1 + arg2


# def main():
#     # func_for_decoration()
#
#     print(test_func(8, 7))
#     print(test_func(0, 0, named="asd"))
#     print(test_func(4, 6, g=8456, named="sdfghkj"))
#     print(test_func(3, 5, named="asd", g=5))
#
#     print()
#     print(test_func(8, 7))
#     print(test_func(0, 0, named="asd"))
#     print(test_func(4, 6))
#     print(test_func(3, 5, g=5, named="asd"))
#
#     return
#
#
# if __name__ == '__main__':
#     main()