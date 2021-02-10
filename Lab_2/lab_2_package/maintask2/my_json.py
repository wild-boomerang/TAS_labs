import argparse
import json
import requests
import re
import copy


def dict_transform(obj):
    obj = dict(obj)

    new_obj = dict()
    for key in obj.keys():
        new_obj[str(key)] = obj[key]

    return new_obj


def list_transform(obj):
    for i in range(len(obj)):
        if isinstance(obj[i], dict):
            obj[i] = dict_transform(obj[i])
        if isinstance(obj[i], list):
            obj[i] = list_transform(obj[i])

    return obj


def to_json(obj_for_json):
    obj = copy.deepcopy(obj_for_json)  # in order not to modify the object

    if isinstance(obj, list):
        list_transform(obj)

    if isinstance(obj, dict):
        obj = dict_transform(obj)

    s = str(obj)

    patterns = [r"True", r"False", r"None", r"\(", r"\)", r"\'"]
    replacements = [r"true", r"false", r"null", r"[", r"]", "\""]

    i = 0
    while i < len(patterns):
        s = re.sub(patterns[i], replacements[i], s)
        i += 1

    if isinstance(obj, str):
        return "\"" + s + "\""
    else:
        return s


def get_elem(text):
    if "." in text:
        return float(text)
    elif text == "null":
        return None
    elif text == "true":
        return True
    elif text == "false":
        return False
    elif text.isdigit():
        return int(text)
    else:
        text = text.replace("\"", "")
        return str(text)


# def nested_cycle(text):  # doesn't work with nested 3 and higher
#     obj = []
#     smth = text.split(", ")
#     i = 0
#     while i < len(smth):
#         print(smth[i])
#         if "[" in smth[i]:
#             smth[i] = smth[i][1:]
#             tempList = [get_elem(smth[i])]
#             j = i + 1
#             while "]" not in smth[j]:
#                 tempList.append(get_elem(smth[j]))
#                 j += 1
#             smth[j] = smth[j][:len(smth[j]) - 1]
#             tempList.append(get_elem(smth[j]))
#             obj.append(tempList)
#             i = j
#         else:
#             obj.append(get_elem(smth[i]))
#         i += 1
#
#     return obj


def func(text):
    obj = []
    smth = text.split(", ")
    i = 0
    while i < len(smth):
        print(smth[i])
        if "[" in smth[i]:
            smth[i] = smth[i][1:]
            tempList = [get_elem(smth[i])]
            j = i + 1
            while "]" not in smth[j]:
                tempList.append(get_elem(smth[j]))
                j += 1
            smth[j] = smth[j][:len(smth[j]) - 1]
            tempList.append(get_elem(smth[j]))
            obj.append(tempList)
            i = j
        else:
            obj.append(get_elem(smth[i]))
        i += 1

    return obj


def from_json(text):
    if text[0] == "[":
        obj = []
        text = text[1:len(text) - 1]

        # print(text.split(", "))

        # for elem in text.split(", "):
        #     obj.append(get_elem(elem))
        obj = func(text)
        return obj
    elif text[0] == "{":
        obj = {}

        return obj
    else:
        return get_elem(text)


def main():
    # serialization
    # var = "("  # todo (, True, False, None, ' in strings doesn't work
    # var = {"asd": 34, 234: [23, 4530.456, "dsdf"], False: True, None: ("sdf", 0, 324, "sdf")}
    # var = [{"asd": 34, 234: [23, 4530.456, "dsdf"], False: True, None: ("sdf", 0, 324, "sdf")}, 234, "sdf",
    #        {456: 234.01265, "sdf": "sdf"}]
    # var = ["asdf", 234, 342.432, (34, 43)]
    # var = [{34: 43}, {"34": 324}, [{23: 43}, [{23: 3}]]]
    var = [23, "werr", [None, True, False], 45.12, ["asdf", ["sdfa", 456], True]]
    # var = None

    # print("str version: " + str(var))
    s1 = json.dumps(var)
    print(s1 + "\n")
    # print("As must be:  " + s1)
    # s2 = to_json(var)
    # print("As I have:   " + s2)
    # print(s1 == s2)

    # deserialization
    obj1 = json.loads(s1)
    print(obj1)
    print(type(obj1))

    obj2 = from_json(s1)
    print(obj2)
    print(type(obj2))

    print(obj1 == obj2)

    # print(to_json.__class__)
    # test = Test(5)
    # print(test.tygydyn())
    # smth = 5
    # print(to_json({2: 1}))
    # print(to_json(test.tygydyn()))
    # print(smth.__class__.__name__)

    # responce = requests.get("https://jsonplaceholder.typicode.com/todos")
    # jsonStr = json.loads(responce.text)
    # print(jsonStr[0])

    # smth = {5.45: 5123.123, "kjhg": "jhg"}
    # print(smth)
    # jsonStr = json.dumps(smth)
    # print(jsonStr)
    # print(to_json(smth))


if __name__ == "__main__":
    main()
