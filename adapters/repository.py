from abc import ABC, abstractmethod
from domain.charla import Charla


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, element):
        raise NotImplementedError




    @abstractmethod
    def get(self, reference) -> Charla:
        raise NotImplementedError
