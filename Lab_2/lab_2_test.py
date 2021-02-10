import unittest
from cached import test_func, cached
import n_vector
import my_json
import json
from external_merge_sort import ext_merge_sort


class CachedTests(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_cached(self):
        saved_res_dict = {}

        self.assertEqual(test_func(1, 2), test_func(1, 2))
        saved_res_dict[(1, 2)] = 3
        self.assertEqual(test_func.res_dict, saved_res_dict)

        # self.assertEqual(test_func(8, arg2=7, named="asd"), test_func(8, 7, named="asd")) # todo when arg2=2
        # saved_res_dict[((8, 7), ('asd',))] = 15
        # self.assertEqual(test_func.res_dict, saved_res_dict)
        #
        # self.assertEqual(test_func(4, 6, named_2=8456, named="named"), test_func(4, 6, named_2=8456, named="named"))
        # saved_res_dict[((4, 6), ('named', 8456))] = 10
        # self.assertEqual(test_func.res_dict, saved_res_dict)
        #
        # self.assertEqual(test_func(3, 5, named="asd", named_2=5), test_func(3, 5, named_2=5, named="asd"))
        # saved_res_dict[((3, 5), ('asd', 5))] = 8
        # self.assertEqual(test_func.res_dict, saved_res_dict)

    def tearDown(self) -> None:
        pass


class NVectorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vector = n_vector.NVector([3, 5])

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def test_append(self):
        self.vector.append(5)
        self.vector.append(2)
        self.assertEqual(str(self.vector), "[3, 5, 5, 2]")

    def test_sum(self):
        result = self.vector + [1, 1]
        self.assertEqual(str(result), "[4, 6]")

    def test_add(self):
        vector2 = n_vector.NVector([2, 2])
        self.vector += vector2
        self.assertEqual(str(self.vector), "[5, 7]")

    def test_sub(self):
        vector2 = n_vector.NVector([2, 2])
        self.vector -= vector2
        self.assertEqual(str(self.vector), "[1, 3]")

    def test_mul(self):
        vector2 = n_vector.NVector([2, 2])
        self.vector *= vector2
        self.assertEqual(str(self.vector), "[6, 10]")

    def test_zero_mul(self):
        self.vector *= 0
        self.assertEqual(str(self.vector), "[0, 0]")

    def test_tuple_sum(self):
        self.vector += (5, 3)
        self.assertEqual(str(self.vector), "[8, 8]")

    def test_comparison(self):
        self.assertTrue(self.vector == n_vector.NVector((3, 5)))
        self.assertFalse(self.vector == n_vector.NVector((3, 5, 5)))
        self.assertFalse(self.vector == n_vector.NVector((5, 8)))

    def test_len(self):
        self.assertEqual(len(self.vector), 2)

    def test_contains(self):
        self.assertTrue(5 in self.vector)
        self.assertFalse(99 in self.vector)

    def test_setitem(self):
        self.vector[0] = 5
        self.assertEqual(self.vector[0], 5)

    def test_delitem(self):
        self.vector.__delitem__(1)
        self.assertEqual(self.vector, [3])

    def test_iteration(self):
        for v in self.vector:
            pass

    @unittest.expectedFailure
    def test_if_def_lengths(self):
        self.vector + [3, 5, 7, 6]


class MyJsonTests(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_dict(self):
        var = {"asd": 34, 234: 45.123}
        self.assertEqual(my_json.to_json(var), json.dumps(var))

    def test_string(self):
        var = "Just some string"
        self.assertEqual(my_json.to_json(var), json.dumps(var))

    def test_tuple(self):
        var = (234, "fds", 234.045)
        self.assertEqual(json.dumps(var), my_json.to_json(var))

    def test_nested_lists(self):
        var = [{34: 43}, {"34": 324}, [{23.123: 43}, [{23: 3.56}]]]
        self.assertEqual(json.dumps(var), my_json.to_json(var))

    def test_true_false_none(self):
        var = (None, True, False)
        self.assertEqual(json.dumps(var), my_json.to_json(var))

    def test_complex(self):
        var = [{"asd": 34, 234: [23, 4530.456, "dsdf"], False: True, None: ("sdf", 0, 324, "sdf")}, 234, "sdf",
               [{234: 453, False: True}, {None: True, 2342: 654.012}, [{324: 43}]], {456: 234.01265, "sdf": "sdf"}]
        self.assertEqual(json.dumps(var), my_json.to_json(var))

    def tearDown(self) -> None:
        pass


class ExtMergeSortTests(unittest.TestCase):
    def test_sort(self):
        with open("test_nums.txt", "w") as file:
            file.writelines("{}\n".format(_) for _ in range(457, -1, -1))
            file.writelines("{}\n".format(_) for _ in range(512))
        ext_merge_sort("test_nums.txt", 100)

        with open("sorted_nums2.txt", "r") as file:
            while True:
                num_1 = file.readline()
                if num_1 != "":
                    num_1 = int(num_1)
                else:
                    break
                num_2 = int(file.readline())

                self.assertTrue(num_2 >= num_1)


if __name__ == "__main__":
    unittest.main()
