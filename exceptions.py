from dataclasses import dataclass


class LinkedListExeption(Exception):
    @property
    def message(self):
        return 'Ошибка связного списка'

@dataclass
class EmptyList(Exception):
    @property
    def message(self):
        return 'Список пуст'     
    
@dataclass
class  IndexOutOfRange(Exception):
    index: int
    @property
    def message(self):
        return f'Индекс {self.index} выходит за границы'   

@dataclass
class MissingIndex(Exception):
    @property
    def message(self):
        return 'Не указан индекс' 
    
@dataclass
class IndexIsNegative(Exception):
    @property
    def message(self):
        return 'Индекс не может быть отрицательным числом'
    
@dataclass
class UnexpectedArgument(Exception):
    @property
    def message(self):
        return 'Неожиданный аргумент'