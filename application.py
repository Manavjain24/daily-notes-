class diet(func):
    // have to write 3 custom decorators
    print("this is a diet decorator")
    return func 

class excercise(func):
    print("this is an excercise decorator")
    return func

class sleep(func):
    print("this is a  sleep decorator")
    return func

@diet
@excercise
@sleep
class health:
    def __init__(self):
        print("This is a health class")