#-*- coding: utf-8 -*-
"""Base class for output plugins"""


class baseplugin(object):
    def run(self):
        pass

    def translate(self, to_translate):
        """receive tuple and try to translate"""
        dictionary = dict([
            ("квартира", "flat"),
            ("комната", "room"),
            ("Тип недвижимости", "type_realty"),
            ("Площадь", "full_square")])

        # Простейший перводчик с русс на англ. Если слова нету - не мняем.
        # Получаем кортеж из двух элементов - возвращаем так же
        if to_translate[0] in dictionary:
            l = dictionary[to_translate[0]]
        else:
            l = to_translate[0]

        if to_translate[1] in dictionary:
            r = dictionary[to_translate[1]]
        else:
            r = to_translate[1]

        return l, r
