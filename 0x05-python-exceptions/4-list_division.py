#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            num = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            num = 0
            print('division by 0')
        except TypeError:
            num = 0
            print('wrong type')
        except IndexError:
            num = 0
            print('out of range')
        finally:
            new.append(num)
    return new
