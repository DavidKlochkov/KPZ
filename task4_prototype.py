import copy


class Virus:
    def __init__(self, name: str, species: str, weight: float, age: int):
        self.name = name
        self.species = species
        self.weight = weight
        self.age = age
        self.children: list["Virus"] = []

    def add_child(self, child: "Virus") -> "Virus":
        self.children.append(child)
        return self

    def clone(self) -> "Virus":
        return copy.deepcopy(self)

    def __str__(self, level: int = 0) -> str:
        indent = "  " * level
        result = (
            f"{indent}Вірус: {self.name} (вид: {self.species}), "
            f"вага: {self.weight}мкг, вік: {self.age} год."
        )
        for child in self.children:
            result += "\n" + child.__str__(level + 1)
        return result


if __name__ == "__main__":
    print("Завдання 4")

    #Перше покоління
    ancestor = Virus("Альфа", "CoronaVirus", 0.5, 100)

    #Друге покоління
    child1 = Virus("Бета", "CoronaVirus", 0.3, 50)
    child2 = Virus("Гамма", "CoronaVirus", 0.4, 60)

    #Третє покоління
    grandchild1 = Virus("Дельта", "CoronaVirus", 0.2, 20)
    grandchild2 = Virus("Омікрон", "CoronaVirus", 0.15, 15)
    grandchild3 = Virus("Лямбда", "CoronaVirus", 0.25, 25)

    child1.add_child(grandchild1).add_child(grandchild2)
    child2.add_child(grandchild3)
    ancestor.add_child(child1).add_child(child2)

    print("\nОригінальне сімейство вірусів:")
    print(ancestor)

    #Клонування
    cloned = ancestor.clone()
    cloned.name = "Альфа-Клон"
    cloned.children[0].name = "Бета-Клон"
    cloned.children[0].children[0].name = "Дельта-Клон"

    print("\nКлонований вірус (після зміни імен клона):")
    print(cloned)

    print("\nОригінал (не змінився після клонування):")
    print(ancestor)

    print("\nПеревірка незалежності клона:")
    print(f"  ancestor.name == cloned.name: {ancestor.name == cloned.name}")
    print(f"  ancestor.children[0].name == cloned.children[0].name: "
          f"{ancestor.children[0].name == cloned.children[0].name}")
    print(f"  Клон є глибокою копією: {ancestor is not cloned}")
    print(f"  Діти клона незалежні: {ancestor.children[0] is not cloned.children[0]}")
