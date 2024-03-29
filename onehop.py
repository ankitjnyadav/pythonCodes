def onehop(lst):
    data = lst
    # Sorting all tuples in ascending order via first element
    data.sort(key=lambda tup: tup[0])
    ans = []                   # Creating a blank List
    for ele in lst:            # Looping through all elements
        x, y = ele             # Storing Tuple value in x and y
        for ele1 in lst:       # For finding next hop for all destinations
            if ele != ele1:    # To check if it's not the same element in loop
                xx, yy = ele1  # Storing another tuple's value in xx, yy
                # checking conditions for adding to ans.
                if y == xx and x != yy and (x, yy) not in ans:
                    # y == xx to check if second element of first tuple is equal to first element of second tuple.
                    # Only then Next Hop is possible
                    # x != y, so that we don't get tuples like (2,2), (3,3) etc.
                    # (x,yy) not in ans, is to ensure that one next hope isn't repeated twice.
                    # Adding tuple to ans if all conditions satisfied.
                    ans.append((x, yy))
    # Sorting all tuples in ascending order via first element and second element.
    ans = sorted(ans, key=lambda tup: (tup[0], tup[1]))
    #ans.sort(key=lambda tup: tup[0])
    return ans


print(onehop([(2, 3), (1, 2), (3, 1), (1, 3), (3, 2), (2, 4), (4, 1)]))
