import time

class Single:

    instance = None
    time_created = None

    def __new__(self) -> None:
        if not self.instance:
            instance = super(Single, self).__new__(self)
            instance.time_created = time.time()
            self.instance = instance
            return instance
        else:
            print("Instance already exists:: ")
            return self.instance


s1 = Single()
s2 = Single()
print(s1.time_created, s2.time_created)