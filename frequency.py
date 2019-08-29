'''
Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form(minfreqlist, maxfreqlist) where

minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order

maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending

frequency([13,12,11,13,14,13,7,11,13,14,12])
([7], [13])

frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
([7], [13, 14])

frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
([7, 11, 12], [13, 14])
'''


def frequency(l):
    freq_table = {}
    min_v, max_v = 0, 0
    (minfreqlist, maxfreqlist) = ([], [])
    l.sort()
    value_freq_list = []

    for i in l:
        if i in freq_table:
            freq_table[i] += 1
        else:
            freq_table[i] = 1

    for k, v in freq_table.items():
        value_freq_list.append(int(v))

    min_v = min(value_freq_list)
    max_v = max(value_freq_list)
    for k, v in freq_table.items():
        if min_v is v and max_v is v:
            minfreqlist.append(k)
            maxfreqlist.append(k)
        elif min_v is v:
            minfreqlist.append(k)
        elif max_v is v:
            maxfreqlist.append(k)

    return(minfreqlist, maxfreqlist)
