# 2022 KAKAO BLIND RECRUITMENT

def ten_to_n(num, n):
    word=""
    while num:
        word = str(num%n)+word
        num=num//n
    return word

def check_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    rslt = ten_to_n(n,k)
    for i in rslt.split('0'):
        if i:
            if check_prime(int(i)):
                answer += 1
    return answer