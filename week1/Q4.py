dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

def merge_dict(dict_first, dict_second):
    for key, value in dict_second.items():
        if key in dict_first:
            dict_first[key] += value
        else:
            dict_first[key] = value
    print(dict_first)

merge_dict(dict_first, dict_second)