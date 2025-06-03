from functools import wraps

def twice(func):

    print("3333")

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper

def run_n_times(n: (int,int)):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            returns = []
            for i in range(n):
                r = func(*args, **kwargs)
                returns.append(r)
            return returns
        return wrapper
    return decorator

@run_n_times(10)
def print_hoi():
    "print hoi"
    print("hoi")
    return 54


help(print_hoi)