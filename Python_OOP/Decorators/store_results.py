class store_results:
    file_path = "./results.txt"

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open(store_results.file_path, "a") as file:
            file.write(f"Function {self.function.__name__} was called. Result: {self.function(*args, **kwargs)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
