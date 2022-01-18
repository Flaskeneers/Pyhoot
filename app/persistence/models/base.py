from abc import ABC

from pymongo.collection import Collection


class Document(dict, ABC):
    collection: Collection = None

    def __init__(self, data):
        super().__init__()
        if "_id" not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self) -> str:
        attributes = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"

    def __str__(self) -> str:
        attributes = "\n".join(f"\t{k}: {v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}:\n{attributes}"

    def save(self) -> None:
        if not self._id:
            del self.__dict__["_id"]
            self.collection.insert_one(self.__dict__)
        else:
            self.update_with(self.__dict__)

    def update_with(self, new_values: dict) -> None:
        self.__dict__.update(new_values)
        self.collection.replace_one({"_id": self._id}, self.__dict__)

    def delete(self) -> None:
        self.collection.delete_one({"_id": self._id})

    def delete_field(self, field: str) -> None:
        self.collection.update_one({"_id": self._id}, {"$unset": {field: ""}})

    @property
    def id(self) -> str:
        return str(self._id)
