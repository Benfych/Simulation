from abc import ABC, abstractmethod

class ObjectCreator(ABC):

    @abstractmethod
    def create_object(self):
        pass




