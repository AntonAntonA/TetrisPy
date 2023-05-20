from Brick import Brick

class GameField:
    _field_width: float = None
    _field_height: float = None

    def __init__(self, field_width: float, field_height: float):
        self._set_width(field_width)
        self._set_height(field_height)

    def _set_width(self, val):
        if val <= 0.:
            raise ValueError
        else:
            self._field_width = val
        return

    def _set_height(self, val):
        if val <= 0.:
            raise ValueError
        else:
            self._field_height = val
        return

    def get_dimensions(self):
        '''
        Возвращает размеры игрового поля в юнитах
        :return: список из двух значений (ширина поля, высота поля)
        '''
        return [self._field_width, self._field_height]