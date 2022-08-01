from __future__ import annotations
import sys
from abc import ABC, abstractmethod


class Logistics(ABC):

    # 初始化透過factory method創建product
    def __init__(self) -> None:
        self.product = self.factory_method()

    # 抽象的product創建方法
    # 子類可以修改工廠方法返回的對象類型
    @abstractmethod
    def factory_method(self) -> Transport:
        pass

    # 卡車和船共通的送貨邏輯
    def run_delivery(self) -> None:
        print("Running some complex operations")
        self.product.deliver()


# 陸路運輸公司
class RoadLogistics(Logistics):

    # 重寫工廠方法
    def factory_method(self) -> Transport:
        return Truck()


# 海路運輸公司
class SeaLogistics(Logistics):

    # 重寫工廠方法
    def factory_method(self) -> Transport:
        return Ship()


# 廣義的運輸工具
class Transport(ABC):

    # 會運輸
    @abstractmethod
    def deliver(self) -> None:
        pass


# 貨車
class Truck(Transport):

    # 會走陸路運輸
    def deliver(self) -> None:
        print("truck delivering stuff")


# 船
class Ship(Transport):

    # 會走海路運輸
    def deliver(self) -> None:
        print("ship delivering stuff")


def client_code(creator: Logistics) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.run_delivery()}", end="")


if __name__ == "__main__":
    # 假設陸路運輸公司那邊要製造貨車來送貨
    logistics = RoadLogistics()
    logistics.run_delivery()

    print("\nApp: Launched with the ConcreteCreator1.")
    client_code(RoadLogistics())

    print("\nApp: Launched with the ConcreteCreator2.")
    client_code(SeaLogistics())

    sys.exit(0)
