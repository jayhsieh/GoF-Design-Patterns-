from __future__ import annotations
from abc import ABC, abstractmethod
import copy


class Prototype(ABC):

    @abstractmethod
    def clone(self) -> Prototype:
        pass


class BaseStore:
    def __init__(self, id: int, name: str, phone: str) -> None:
        self.id = id
        self.name = name
        self.phone = phone

    def __str__(self) -> str:
        return str(self.__dict__)

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__


class PrototypeFacebook(BaseStore, Prototype):
    def __init__(self, id: int, name: str, phone: str, ads: str) -> None:
        super().__init__(id, name, phone)
        self.ads = ads

    def clone(self) -> Prototype:
        print("Cloning PrototypeFacebook")
        # 需要 copy() 是為了避免使用同一個 reference
        return copy.deepcopy(self)


class PrototypeGoogle(BaseStore, Prototype):
    def __init__(self, id: int, name: str, phone: str, search_engine: str) -> None:
        super().__init__(id, name, phone)
        self.searchEngine = search_engine

    def clone(self) -> Prototype:
        print("Cloning PrototypeGoogle")
        # 需要 copy() 是為了避免使用同一個 reference
        return copy.deepcopy(self)
