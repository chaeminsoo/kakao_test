# 2022 kakao tech internship

from collections import deque

def solution(q1, q2):
    s1 = sum(q1)
    s2 = sum(q2)
    l = len(q1)
    
    q1 = deque(q1)
    q2 = deque(q2)
    for i in range(4*l):
        if s1 == s2:
            return i
        elif s1 > s2:
            ref = q1.popleft()
            q2.append(ref)
            s1 -= ref
            s2+=ref
        else:
            ref = q2.popleft()
            q1.append(ref)
            s2 -= ref
            s1+=ref
    return -1