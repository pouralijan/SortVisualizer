from sortvisualizer import Data


class BaseSort:
    _name = "BaseSort"
    def __init__(self, data:Data) -> None:
        self._data = data

    @property
    def name(self):
        return self._name

    def reset(self):
        self._data.shuffle()
        
    def update(self, check_animation=False):
        if self._data.is_sorted():
            return
        self._data.data.sort()
