#функция update_dictionary(d, key, value), которая принимает на вход словарь d d d и два числа: key key key и value value value.

#Если ключ key key key есть в словаре d d d, то добавляется значение value  в список, который хранится по этому ключу.
#Если ключа key  нет в словаре, то он добавляется  в список по ключу 2∗key . Если и ключа  2∗key нет, то добавляется ключ 2∗key  в словарь и ему сопоставляется список из переданного элемента [value].


def update_dictionary(d, key, value):
    if key in d:
        d[key]+=[value]
    if key not in d:
        d.setdefault(2*key, []).append(value)
    if key*2 not in d and key not in d:
        d[2*key]=[value]
    return() 
