#!/usr/bin/python3
''' algorithm that finds a single peak in a list of integers'''


def find_peak(list_of_integers):
    '''find peak in list of ints'''
    list_size = len(list_of_integers)
    if list_size == 0:
        return None
    _list = list_of_integers
    for i in range(list_size):
        '''peak at the beginning'''
        if i == 1 and _list[i] < _list[0]:
            return _list[0]
        elif i == list_size - 1:
            '''peak at the end'''
            if i > 0 and _list[i] > _list[i - 1]:
                return _list[i]
            elif _list[i - 1] == _list[i]:
                '''plateau'''
                return _list[i]
        else:
            '''peak in the middle'''
            if i > 0 and _list[i] > _list[i - 1] and _list[i] > _list[i + 1]:
                return _list[i]
