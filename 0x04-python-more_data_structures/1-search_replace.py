#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    count = 0
    if my_list is None:
        return ()
    for i in new:
        if i == search:
            new[count] = replace
        count = count + 1
    return (new)
