from abc import ABC, abstractmethod
from typing import List


class Character:
    def __init__(self):
        self.name: str = ""
        self.height: float = 0.0
        self.build: str = ""
        self.hair_color: str = ""
        self.eye_color: str = ""
        self.outfit: str = ""
        self.inventory: List[str] = []
        self.good_deeds: List[str] = []
        self.evil_deeds: List[str] = []
        self.special_ability: str = ""

    def __str__(self):
        lines = [
            f"Ім'я: {self.name}",
            f"Зріст: {self.height} см",
            f"Статура: {self.build}",
            f"Колір волосся: {self.hair_color}",
            f"Колір очей: {self.eye_color}",
            f"Одяг: {self.outfit}",
            f"Інвентар: {', '.join(self.inventory) if self.inventory else 'порожньо'}",
        ]
        if self.good_deeds:
            lines.append(f"Добрі справи: {', '.join(self.good_deeds)}")
        if self.evil_deeds:
            lines.append(f"Злі справи: {', '.join(self.evil_deeds)}")
        if self.special_ability:
            lines.append(f"Особлива здібність: {self.special_ability}")
        return "\n".join(lines)


class CharacterBuilder(ABC):
    def __init__(self):
        self._character = Character()

    @abstractmethod
    def set_name(self, name: str) -> "CharacterBuilder":
        pass

    @abstractmethod
    def set_height(self, height: float) -> "CharacterBuilder":
        pass

    @abstractmethod
    def set_build(self, build: str) -> "CharacterBuilder":
        pass

    @abstractmethod
    def set_hair_color(self, color: str) -> "CharacterBuilder":
        pass

    @abstractmethod
    def set_eye_color(self, color: str) -> "CharacterBuilder":
        pass

    @abstractmethod
    def set_outfit(self, outfit: str) -> "CharacterBuilder":
        pass

    @abstractmethod
    def add_inventory_item(self, item: str) -> "CharacterBuilder":
        pass

    @abstractmethod
    def set_special_ability(self, ability: str) -> "CharacterBuilder":
        pass

    def build(self) -> Character:
        return self._character


class HeroBuilder(CharacterBuilder):
    def set_name(self, name: str) -> "HeroBuilder":
        self._character.name = name
        return self

    def set_height(self, height: float) -> "HeroBuilder":
        self._character.height = height
        return self

    def set_build(self, build: str) -> "HeroBuilder":
        self._character.build = build
        return self

    def set_hair_color(self, color: str) -> "HeroBuilder":
        self._character.hair_color = color
        return self

    def set_eye_color(self, color: str) -> "HeroBuilder":
        self._character.eye_color = color
        return self

    def set_outfit(self, outfit: str) -> "HeroBuilder":
        self._character.outfit = outfit
        return self

    def add_inventory_item(self, item: str) -> "HeroBuilder":
        self._character.inventory.append(item)
        return self

    def set_special_ability(self, ability: str) -> "HeroBuilder":
        self._character.special_ability = ability
        return self

    def do_good_deed(self, deed: str) -> "HeroBuilder":
        self._character.good_deeds.append(deed)
        return self


class EnemyBuilder(CharacterBuilder):
    def set_name(self, name: str) -> "EnemyBuilder":
        self._character.name = name
        return self

    def set_height(self, height: float) -> "EnemyBuilder":
        self._character.height = height
        return self

    def set_build(self, build: str) -> "EnemyBuilder":
        self._character.build = build
        return self

    def set_hair_color(self, color: str) -> "EnemyBuilder":
        self._character.hair_color = color
        return self

    def set_eye_color(self, color: str) -> "EnemyBuilder":
        self._character.eye_color = color
        return self

    def set_outfit(self, outfit: str) -> "EnemyBuilder":
        self._character.outfit = outfit
        return self

    def add_inventory_item(self, item: str) -> "EnemyBuilder":
        self._character.inventory.append(item)
        return self

    def set_special_ability(self, ability: str) -> "EnemyBuilder":
        self._character.special_ability = ability
        return self

    def do_evil_deed(self, deed: str) -> "EnemyBuilder":
        self._character.evil_deeds.append(deed)
        return self


class Director:
    def build_dream_hero(self, builder: HeroBuilder) -> Character:
        return (
            builder
            .set_name("Арія Зоряна")
            .set_height(172)
            .set_build("Струнка, спортивна")
            .set_hair_color("Золотисто-руде")
            .set_eye_color("Смарагдово-зелений")
            .set_outfit("Срібна броня з рунами, плащ із зоряної тканини")
            .add_inventory_item("Меч Світанку")
            .add_inventory_item("Щит Надії")
            .add_inventory_item("Зілля зцілення x5")
            .set_special_ability("Зоряний вибух — звільняє хвилю світла, що очищає темряву")
            .do_good_deed("Врятувала місто від дракона")
            .do_good_deed("Відновила мир між двома королівствами")
            .build()
        )

    def build_arch_enemy(self, builder: EnemyBuilder) -> Character:
        return (
            builder
            .set_name("Малакар Темний")
            .set_height(195)
            .set_build("Масивна, загрозлива")
            .set_hair_color("Чорне як смола")
            .set_eye_color("Криваво-червоний")
            .set_outfit("Чорна мантія з черепами, обладунок із темного заліза")
            .add_inventory_item("Посох Загибелі")
            .add_inventory_item("Книга Темних Заклинань")
            .add_inventory_item("Амулет безсмертя")
            .set_special_ability("Темний вихор — поглинає душі ворогів")
            .do_evil_deed("Знищив три міста")
            .do_evil_deed("Відкрив портал у пекло")
            .build()
        )


if __name__ == "__main__":
    print("Завдання 5")

    director = Director()

    hero_builder = HeroBuilder()
    hero = director.build_dream_hero(hero_builder)
    print("\nГерой мрії")
    print(hero)

    enemy_builder = EnemyBuilder()
    enemy = director.build_arch_enemy(enemy_builder)
    print("\nНайзапекліший ворог")
    print(enemy)

    print("\nВласноруч створений персонаж")
    custom = (
        HeroBuilder()
        .set_name("Іван Хоробрий")
        .set_height(180)
        .set_build("Атлетична")
        .set_hair_color("Темно-русяве")
        .set_eye_color("Блакитний")
        .set_outfit("Козацька кольчуга")
        .add_inventory_item("Шабля")
        .add_inventory_item("Лук і стріли")
        .set_special_ability("Козацький дух — невразливість до страху")
        .do_good_deed("Захистив рідне село")
        .build()
    )
    print(custom)
