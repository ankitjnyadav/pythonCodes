'''
Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched:
that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it.
Your function should ignore all other symbols that appear in s.
Your function should return True if s has matched brackets and False if it does not
matched("zb%78")
matched("(7)(a")
'''
open_list = ["("]
close_list = [")"]


def matched(s):
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
      return False
