from abc import ABC, abstractmethod


class Laptop(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass


class Netbook(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass


class EBook(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass


class Smartphone(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass


class TechFactory(ABC):
    @abstractmethod
    def create_laptop(self) -> Laptop:
        pass

    @abstractmethod
    def create_netbook(self) -> Netbook:
        pass

    @abstractmethod
    def create_ebook(self) -> EBook:
        pass

    @abstractmethod
    def create_smartphone(self) -> Smartphone:
        pass


class IProneLaptop(Laptop):
    def get_info(self) -> str:
        return "IProne MacBook Pro: M3 chip, 16GB RAM, 512GB SSD"


class IProneNetbook(Netbook):
    def get_info(self) -> str:
        return "IProne MacBook Air: M2 chip, 8GB RAM, 256GB SSD"


class IProneEBook(EBook):
    def get_info(self) -> str:
        return "IProne iRead Pro: 10.9\" Retina, 64GB"


class IProneSmartphone(Smartphone):
    def get_info(self) -> str:
        return "IProne iPhone 16: A18 chip, 256GB, 48MP camera"


class IProneFactory(TechFactory):
    def create_laptop(self) -> Laptop:
        return IProneLaptop()

    def create_netbook(self) -> Netbook:
        return IProneNetbook()

    def create_ebook(self) -> EBook:
        return IProneEBook()

    def create_smartphone(self) -> Smartphone:
        return IProneSmartphone()


class KiaomiLaptop(Laptop):
    def get_info(self) -> str:
        return "Kiaomi Mi Laptop Pro: Intel i7, 16GB RAM, 1TB SSD"


class KiaomiNetbook(Netbook):
    def get_info(self) -> str:
        return "Kiaomi Mi Netbook: Intel i5, 8GB RAM, 512GB SSD"


class KiaomiEBook(EBook):
    def get_info(self) -> str:
        return "Kiaomi Mi EBook: 7.8\" E-Ink, 32GB"


class KiaomiSmartphone(Smartphone):
    def get_info(self) -> str:
        return "Kiaomi Mi 14: Snapdragon 8 Gen 3, 512GB, 50MP camera"


class KiaomiFactory(TechFactory):
    def create_laptop(self) -> Laptop:
        return KiaomiLaptop()

    def create_netbook(self) -> Netbook:
        return KiaomiNetbook()

    def create_ebook(self) -> EBook:
        return KiaomiEBook()

    def create_smartphone(self) -> Smartphone:
        return KiaomiSmartphone()


class BalaxyLaptop(Laptop):
    def get_info(self) -> str:
        return "Balaxy Galaxy Book4 Pro: Intel i9, 32GB RAM, 1TB SSD"


class BalaxyNetbook(Netbook):
    def get_info(self) -> str:
        return "Balaxy Galaxy Book4 Go: Snapdragon X, 8GB RAM, 256GB SSD"


class BalaxyEBook(EBook):
    def get_info(self) -> str:
        return "Balaxy Galaxy Tab S9 FE: 10.9\" AMOLED, 128GB"


class BalaxySmartphone(Smartphone):
    def get_info(self) -> str:
        return "Balaxy Galaxy S25 Ultra: Snapdragon 8 Elite, 512GB, 200MP camera"


class BalaxyFactory(TechFactory):
    def create_laptop(self) -> Laptop:
        return BalaxyLaptop()

    def create_netbook(self) -> Netbook:
        return BalaxyNetbook()

    def create_ebook(self) -> EBook:
        return BalaxyEBook()

    def create_smartphone(self) -> Smartphone:
        return BalaxySmartphone()


def demo_factory(factory: TechFactory):
    print(f"  Ноутбук:  {factory.create_laptop().get_info()}")
    print(f"  Нетбук:   {factory.create_netbook().get_info()}")
    print(f"  Електронна книга: {factory.create_ebook().get_info()}")
    print(f"  Смартфон: {factory.create_smartphone().get_info()}")


if __name__ == "__main__":
    print("Завдання 2")

    factories = {
        "IProne": IProneFactory(),
        "Kiaomi": KiaomiFactory(),
        "Balaxy": BalaxyFactory(),
    }

    for brand, factory in factories.items():
        print(f"\nБренд: {brand}")
        demo_factory(factory)
