class BMW:
    car = "BMW"
    def __init__(self) -> None:
        pass

class Toyota:
    car = "Toyota"
    def __init__(self) -> None:
        pass

class Car:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create_car(c):
        if c == "BMW":
            return BMW()
        elif c == "Toyota":
            return Toyota()
        else: return None


print("Creating BMW:", Car.create_car("BMW").car)
print("Creating Toyota:", Car.create_car("Toyota").car)