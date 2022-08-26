# SRP
import sys
from abc import ABC, abstractmethod


# 汽車
class Car:
    def __init__(self) -> None:
        self.parts = "A car with "

    def add(self, part: str) -> None:
        self.parts += (part + " ")


# 機車
class Motorcycle:
    def __init__(self) -> None:
        self.parts = "A motorcycle with "

    def add(self, part: str) -> None:
        self.parts += (part + " ")


# 抽象的builder會 (0)回傳product (1)安裝車體 (2)安裝引擎 (3)安裝擾流板
class Builder(ABC):

    @abstractmethod
    def get_product(self):
        pass

    @abstractmethod
    def install_body(self) -> None:
        pass

    @abstractmethod
    def install_engine(self) -> None:
        pass

    @abstractmethod
    def install_spoiler(self) -> None:
        pass


# 汽車builder會 (0)回傳product (1)安裝車體 (2)安裝引擎 (3)安裝擾流板
class CarBuilder(Builder):

    # 初始化：產生空的汽車供安裝各種部件
    def __init__(self) -> None:
        self.__product = None
        self.reset()

    # 產生空的汽車供安裝各種部件
    def reset(self) -> None:
        self.__product = Car()

    # [細節] 通常每個builder要負責提供方法獲取他製造的東西，因為不同builder可能回傳完全不同class的object
    # 比如說CarBuilder製造Car，而MotorcycleBuilder製造Motorcycle
    # 通常builder回傳製造的東西以後要重設，準備下一輪的安裝，所以通常會呼叫reset()
    def get_product(self) -> Car:
        product = self.__product
        self.reset()
        return product

    def install_body(self) -> None:
        self.__product.add("car_body")

    def install_engine(self) -> None:
        self.__product.add("car_engine")

    def install_spoiler(self) -> None:
        self.__product.add("car_spoiler")


# 機車builder會 (0)回傳product (1)安裝車體 (2)安裝引擎 (3)安裝擾流板
class MotorcycleBuilder(Builder):

    # 初始化：產生空的汽車供安裝各種部件
    def __init__(self) -> None:
        self.__product = None
        self.reset()

    # 產生空的機車供安裝各種部件
    def reset(self) -> None:
        self.__product = Motorcycle()

    def get_product(self) -> Motorcycle:
        product = self.__product
        self.reset()
        return product

    def install_body(self) -> None:
        self.__product.add("motorcycle_body")

    def install_engine(self) -> None:
        self.__product.add("motorcycle_engine")

    def install_spoiler(self) -> None:
        self.__product.add("motorcycle_spoiler")


# Director負責記得製造哪種車需要哪些零件，然後會呼叫builder負責安裝每個零件
class Director:

    def __init__(self) -> None:
        self.builder = None

    # 用來存取builder，因為我們要負責指派builder給director
    def builder(self) -> Builder:
        return self.builder

    # 普通車款要安裝車體、安裝引擎
    def build_basic_entity(self) -> None:
        self.builder.install_body()
        self.builder.install_engine()

    # 運動型車款要安裝車體、安裝引擎、安裝擾流板
    def build_sports_entity(self) -> None:
        self.builder.install_body()
        self.builder.install_engine()
        self.builder.install_spoiler()


if __name__ == "__main__":
    # 假設現在要製造轎車跟跑車(兩種汽車)
    director = Director()
    car_builder = CarBuilder()
    director.builder = car_builder

    print("Constructing basic car")
    director.build_basic_entity()
    print("product completed:", car_builder.get_product().parts)

    print("\n")

    print("Constructing sports car")
    director.build_sports_entity()
    print("product completed:", car_builder.get_product().parts)

    print("\n")

    # [細節] 如果要客製化某台很特別的車(只有車體跟擾流板的展示用車)
    # 其實我們也可以不用director直接呼叫car_builder內部的安裝功能
    print("Constructing custom car (without director)")
    car_builder.install_body()
    car_builder.install_spoiler()
    print("product completed:", car_builder.get_product().parts)

    print("\n")

    # [細節] director記得運動型車款的零件菜單：如果交給他CarBuilder會做出四輪跑車
    # 如果交給他MotorcycleBuilder會做出兩輪跑車
    motorcycle_builder = MotorcycleBuilder()
    director.builder = motorcycle_builder
    print("Constructing sports motorcycle")
    director.build_sports_entity()
    print("product completed:", motorcycle_builder.get_product().parts)

    sys.exit(0)
