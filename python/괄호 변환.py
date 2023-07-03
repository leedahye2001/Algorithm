# import sys
# input = sys.stdin.readline
#
# p = input()


def solution(p):
    stack = []
    answer = True

    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if stack == '[]':
                answer = False
                break
            else:











