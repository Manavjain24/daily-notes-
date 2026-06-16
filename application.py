def diet(func):
    def wrapper(*args, **kwargs):
        print("this is a diet decorator")
        return func(*args, **kwargs)
    return wrapper


def excercise(func):
    def wrapper(*args, **kwargs):
        print("this is an excercise decorator")
        return func(*args, **kwargs)
    return wrapper


def sleep(func):
    def wrapper(*args, **kwargs):
        print("this is a sleep decorator")
        return func(*args, **kwargs)
    return wrapper


@diet
@excercise
@sleep
class health:
    def __init__(self):
        print("This is a health class")