import random


class Data:
    def __init__(self, start: int = 1, end: int = 101, size: int = None) -> None:
        self._start: int = start
        self._end: int = size + 1 if size else end
        self._size: int = self._end - self._start

        self._data: list = list(range(self._start, self._end))

        self._selected_index :int = 0
        self._checked_index :int = 0
        self._unsorted_index :int = 0

    def is_sorted(self) -> bool:
        if self._data == sorted(self._data):
            self._selected_index = -1
            self._checked_index = -1
            self._unsorted_index = -1
            return True
        return False

    @property
    def size(self) -> int:
        raise DeprecationWarning("Using len()")

    @property
    def data(self) -> list:
        return self._data

    def shuffle(self) -> None:
        self.selected_index: int = 0
        self.current_index: int = 0
        self.unsorted_index: int = 0
        random.shuffle(self._data)

    @property
    def unsorted_index(self) -> int:
        return self._unsorted_index

    @unsorted_index.setter
    def unsorted_index(self, value:int) -> None:
        self._unsorted_index = value

    @property
    def selected_index(self) -> int:
        return self._selected_index

    @selected_index.setter
    def selected_index(self, value:int) -> None:
        self._selected_index = value

    @property
    def current_index(self) -> int:
        return self._checked_index

    @current_index.setter
    def current_index(self, value:int) -> None:
        self._checked_index = value

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]
    
    def __setitem__(self, key, value):
        self._data[key] = value