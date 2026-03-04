import threading


class Authenticator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._logged_in_user = None
        print("Authenticator: екземпляр створено")

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        raise TypeError("Клас Authenticator не може бути успадкований")

    def login(self, username: str, password: str) -> bool:
        users = {"admin": "admin123", "user": "pass456"}
        if users.get(username) == password:
            self._logged_in_user = username
            print(f"Authenticator: користувач '{username}' увійшов у систему")
            return True
        print(f"Authenticator: невірні дані для '{username}'")
        return False

    def logout(self):
        print(f"Authenticator: користувач '{self._logged_in_user}' вийшов із системи")
        self._logged_in_user = None

    def get_current_user(self) -> str:
        return self._logged_in_user


if __name__ == "__main__":
    print("Завдання 3")

    auth1 = Authenticator()
    auth2 = Authenticator()

    print(f"\nauth1 is auth2: {auth1 is auth2}")
    print(f"id(auth1) == id(auth2): {id(auth1) == id(auth2)}")

    auth1.login("admin", "admin123")
    print(f"Поточний користувач (через auth2): {auth2.get_current_user()}")
    auth2.logout()

    print("\nПеревірка в багатопотоковому середовищі:")
    instances = []

    def create_instance():
        instances.append(Authenticator())

    threads = [threading.Thread(target=create_instance) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    all_same = all(inst is instances[0] for inst in instances)
    print(f"Всі 5 екземплярів однакові: {all_same}")

    print("\nПеревірка захисту від успадкування:")
    try:
        class SubAuth(Authenticator):
            pass
    except TypeError as e:
        print(f"Помилка успадкування: {e}")
