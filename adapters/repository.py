from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, element):
        raise NotImplementedError




    @abstractmethod
    def get(self, reference):
        raise NotImplementedError
