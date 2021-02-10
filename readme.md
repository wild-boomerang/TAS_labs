Laboratory works on **Tools and software**, the main purpose of which is to study basics of python.  

# Lab 1 - Fundamentals of Python
### Main tasks:
1. The _word count_ task. The input is text data. It is necessary to calculate and display statistics on how many times each word is repeated in the received text. When deciding to use the `dict()` container or its analogs.
1. Based on the last paragraph: compose and display a sentence of the 10 most frequently repeated words in the received text. When deciding to use the built-in
operations on strings.
1. Quick sorting. The input receives a string containing numbers separated by spaces. It is necessary to implement a quick sort algorithm and use it to sort the data. The output will be sorted in ascending order
numbers.
1. Sort by merges. Similar to the previous point, only you need to implement and use merge sort. When deciding to use the slicing mechanism (slices).

### Additional tasks:
1. Write a generator that sequentially returns Fibonacci numbers starting from the first. (1 point)
1. Read the input data for each of the tasks described above from a file with a fixed name. (1 point)
1. When working with a file, use the with context statement. (1 point)
1. Use command line arguments to get the name of the file from which to read the input. (1 point)
1. Combine all the tasks described above into one program and determine which subroutine to run using command line arguments. Use the argparse module. (4 points)

# Lab 2 - Basic elements of the Python language

### Themes:
1. Data types.
1. Strings and formatting.
1. Input output.
1. Modules.
1. Handling errors.
1. Classes and metaclasses.
1. Generators and iterators.
1. Decorators.
1. Descriptors.


### Requirements:
- Each task is a separate module that can be called as a file or imported and used as a library.
- Where necessary, create your own exception classes to signal specific errors or use existing ones. Handle the errors of the libraries being called.
- In tasks, you cannot simply use built-in analogs of the requested elements from the language or libraries, you must implement yourself. Example: You cannot use the built-in `json` module in a json converter.

### Main tasks:
1. Merge sort in external memory.
The input is a file with numbers in an arbitrary format. The file size must be large enough to run out of RAM for regular merge sort. The output is a file with these numbers in ascending order. Store intermediate results in temporary files (the `tempfile` module is recommended). Temporary files are deleted after use.  
You can create a large file with numbers with this script:  
    ```python
    import random
    with open ('numbers.txt', 'w') as f:
        f.writelines ('{} \ n'.format (random.randint (-1000000, 1000000)) for _ in range (500000000))
    ```
1. Your converter to JSON. Implement the `to_json(obj)` function, which receives a python object as input, and outputs a JSON string.
1. Class `n dimensional vector`. This class must have all the natural operations for a vector - addition, subtraction, multiplication by a constant and dot product, comparison by equality. In addition, there must be operations for calculating the length, getting an element by index, and also a string representation.
1. The `@cached` decorator, which stores the function value on each call. If the function is called again with the same arguments, the stored value is returned and the function is not evaluated.
1. Unit tests. Use any testing framework (`unittest`, `nose`, `pytest`). Use the `coverage` module to assess code coverage by tests. For each main task, write 2+ tests (correct work,
incorrect work).

### Additional tasks:
1. Custom converter from JSON. Implement a function `from_json(text)` that returns a python object corresponding to a json string. Don't use standard JSON tools. (4 points)
1. Singleton. Implement the Singleton design pattern that can be applied to an arbitrary class. Develop yourself how this tool will be applied to the target class (for example, modify the original class or change the way a constructor is called). (2 points)
1. Implement your installable (`setup.py`) package with all the tasks of this lab, divided into modules. Describe the dependencies, specify scripts for starting tasks from each item. (2 points)