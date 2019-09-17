#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if idx < 0:
        return (new)
    elif idx >= len(my_list):
        return (new)
    else:
        for i in range(len(new)):
            if i == idx:
                del new[i]
                new.insert(idx, element)
                return (new)
        return (None)
