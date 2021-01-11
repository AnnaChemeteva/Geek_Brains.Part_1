from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def sewing(self):
        pass


class CoatAndSuit(Clothes):
    def __init__(self, size, height):
        self.__size = size
        self.__height = height

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def sewing(self):
        return f'Для изготовления изделий необходимо {str(round((self.__size / 6.5 + 0.5) + (2 * self.__height + 0.3)))}' \
               f' метра ткани'


coat_suit_1 = CoatAndSuit(44, 160)
print(coat_suit_1.sewing())
