from abc import ABC, abstractmethod


class Subscription(ABC):
    @property
    @abstractmethod
    def monthly_fee(self) -> float:
        pass

    @property
    @abstractmethod
    def min_period(self) -> int:
        pass

    @property
    @abstractmethod
    def channels(self) -> list:
        pass

    @property
    @abstractmethod
    def features(self) -> list:
        pass

    def __str__(self):
        return (
            f"{self.__class__.__name__}:\n"
            f"  Щомісячна плата: {self.monthly_fee} грн\n"
            f"  Мінімальний період: {self.min_period} міс.\n"
            f"  Канали: {', '.join(self.channels)}\n"
            f"  Можливості: {', '.join(self.features)}"
        )


class DomesticSubscription(Subscription):
    @property
    def monthly_fee(self) -> float:
        return 99.0

    @property
    def min_period(self) -> int:
        return 1

    @property
    def channels(self) -> list:
        return ["1+1", "Україна", "ICTV", "СТБ"]

    @property
    def features(self) -> list:
        return ["HD якість", "Перегляд на 1 пристрої"]


class EducationalSubscription(Subscription):
    @property
    def monthly_fee(self) -> float:
        return 149.0

    @property
    def min_period(self) -> int:
        return 3

    @property
    def channels(self) -> list:
        return ["National Geographic", "Discovery", "BBC Earth", "History"]

    @property
    def features(self) -> list:
        return ["HD якість", "Доступ до навчальних матеріалів", "Перегляд на 2 пристроях"]


class PremiumSubscription(Subscription):
    @property
    def monthly_fee(self) -> float:
        return 299.0

    @property
    def min_period(self) -> int:
        return 6

    @property
    def channels(self) -> list:
        return ["1+1", "Україна", "ICTV", "СТБ", "National Geographic",
                "Discovery", "BBC Earth", "HBO", "Netflix Originals"]

    @property
    def features(self) -> list:
        return ["4K якість", "Перегляд на 5 пристроях", "Завантаження для офлайн перегляду",
                "Пріоритетна підтримка"]


class SubscriptionCreator(ABC):
    @abstractmethod
    def create_domestic(self) -> DomesticSubscription:
        pass

    @abstractmethod
    def create_educational(self) -> EducationalSubscription:
        pass

    @abstractmethod
    def create_premium(self) -> PremiumSubscription:
        pass

    def buy_subscription(self, sub_type: str) -> Subscription:
        if sub_type == "domestic":
            sub = self.create_domestic()
        elif sub_type == "educational":
            sub = self.create_educational()
        elif sub_type == "premium":
            sub = self.create_premium()
        else:
            raise ValueError(f"Невідомий тип підписки: {sub_type}")
        print(f"[{self.__class__.__name__}] Оформлено підписку: {sub.__class__.__name__}")
        return sub


class WebSite(SubscriptionCreator):
    def create_domestic(self) -> DomesticSubscription:
        print("  Веб-сайт: застосовано онлайн-знижку 5%")
        sub = DomesticSubscription()
        return sub

    def create_educational(self) -> EducationalSubscription:
        print("  Веб-сайт: застосовано студентську знижку 10%")
        return EducationalSubscription()

    def create_premium(self) -> PremiumSubscription:
        print("  Веб-сайт: додано бонус — 1 місяць безкоштовно")
        return PremiumSubscription()


class MobileApp(SubscriptionCreator):
    def create_domestic(self) -> DomesticSubscription:
        print("  Мобільний додаток: надіслано push-сповіщення про активацію")
        return DomesticSubscription()

    def create_educational(self) -> EducationalSubscription:
        print("  Мобільний додаток: надіслано push-сповіщення про активацію")
        return EducationalSubscription()

    def create_premium(self) -> PremiumSubscription:
        print("  Мобільний додаток: надіслано push-сповіщення + подарунок")
        return PremiumSubscription()


class ManagerCall(SubscriptionCreator):
    def create_domestic(self) -> DomesticSubscription:
        print("  Менеджер: підписку оформлено по телефону, відправлено договір")
        return DomesticSubscription()

    def create_educational(self) -> EducationalSubscription:
        print("  Менеджер: підписку оформлено по телефону, відправлено договір")
        return EducationalSubscription()

    def create_premium(self) -> PremiumSubscription:
        print("  Менеджер: VIP-підписку оформлено, призначено персонального менеджера")
        return PremiumSubscription()


if __name__ == "__main__":
    print("Завдання 1")

    creators = [WebSite(), MobileApp(), ManagerCall()]

    for creator in creators:
        print(f"\n{creator.__class__.__name__}")
        sub = creator.buy_subscription("domestic")
        print(sub)
        print()
        sub = creator.buy_subscription("educational")
        print(sub)
        print()
        sub = creator.buy_subscription("premium")
        print(sub)
