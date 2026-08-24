from threading import Lock


class Singleton:
    _instance = None
    _lock = Lock()

    def __init__(self):
        print("Singleton Constructor Called!")

    @classmethod
    def getInstance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
        return cls._instance


# Main
s1 = Singleton.getInstance()
s2 = Singleton.getInstance()

print(s1 is s2)