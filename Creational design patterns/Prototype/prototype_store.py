import sys
from enum import Enum
from prototype import Prototype, PrototypeFacebook, PrototypeGoogle


class StoreEnum(Enum):
    Google = 1,
    Facebook = 2,
    Amazon = 3


class PrototypeStore:

    _prototypes = {}

    def add(self, store: StoreEnum, prototype: Prototype) -> None:
        self._prototypes[store] = prototype

    def get(self, store: StoreEnum) -> Prototype:
        return self._prototypes[store].clone()


if __name__ == '__main__':
    google_p = PrototypeGoogle(
        id=1001,
        name="Google",
        phone="0911222333",
        search_engine="Awesome"
    )

    facebook_p = PrototypeFacebook(
        id=2001,
        name="Facebook",
        phone="0922333444",
        ads="Many"
    )

    # Initialize PrototypeStore
    prototypeStore = PrototypeStore()
    prototypeStore.add(StoreEnum.Google, google_p)
    prototypeStore.add(StoreEnum.Facebook, facebook_p)

    # region Clone Google
    new_google = prototypeStore.get(StoreEnum.Google)
    print(str(new_google))

    # region Clone Facebook
    new_facebook = prototypeStore.get(StoreEnum.Facebook)
    print(str(new_facebook))

    sys.exit(0)
