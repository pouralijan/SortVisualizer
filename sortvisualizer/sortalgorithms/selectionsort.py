from sortalgorithms.base import BaseSort
from sortvisualizer.data_class import Data
import time


class SelectedSort(BaseSort):
    _name = "SelectedSort"

    def __init__(self, data: Data) -> None:
        self._data = data

    @property
    def name(self):
        return self._name

    def update(self, check_animation=False):
        if self._data.is_sorted():
            return
        if check_animation:
            if self._data.selected_index > len(self._data):
                return

            if self._data.current_index > len(self._data) - 1:
                self._data[self._data.unsorted_index], self._data[self._data.selected_index] = self._data[
                    self._data.selected_index], self._data[self._data.unsorted_index]
                self._data.unsorted_index += 1
                self._data.selected_index = self._data.unsorted_index
                self._data.current_index = self._data.unsorted_index

            elif self._data[self._data.selected_index] > self._data[self._data.current_index]:
                self._data.selected_index = self._data.current_index

        else:
            self._data.current_index = self._data.unsorted_index
            for checked_index in range(self._data.unsorted_index+1, len(self._data)):
                if self._data[self._data.current_index] > self._data[checked_index]:
                    self._data.current_index = checked_index

            self._data[self._data.unsorted_index], self._data[self._data.current_index] = self._data[
                self._data.current_index], self._data[self._data.unsorted_index]
            self._data.unsorted_index = self._data.unsorted_index + 1

        self._data.current_index += 1
