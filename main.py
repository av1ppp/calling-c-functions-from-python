import ctypes

cdll = ctypes.CDLL("./lib.so")
    
def square(i: int) -> int:
    return cdll.square(i)

def say_hello(name: str) -> None:
    cdll.say_hello(name.encode())

print(square(20))
say_hello("Avi")
