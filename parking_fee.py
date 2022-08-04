# 2022 KAKAO BLIND RECRUITMENT
import math

def solution(fees, records):
    answer = []
    cars = {}
    cars_t = {}
    cars_fee = {}
    for i in records:
        t,n,io = i.split()
        if io == 'IN':
            try:
                cars[n].append(t)
            except KeyError:
                cars[n] = [t]
                cars_fee[n] = 0
                cars_t[n] = 0
        else:
            in_t = cars[n].pop()
            in_t = int(in_t[:2])*60 + int(in_t[3:])
            t = int(t[:2])*60 + int(t[3:])
            charge_t = t - in_t
            cars_t[n] += charge_t
    for i,j in cars.items():
        if j:
            in_t = j.pop()
            in_t = int(in_t[:2])*60 + int(in_t[3:])
            t = 23*60 + 59
            charge_t = t - in_t
            cars_t[i] += charge_t
    for i,j in cars_t.items():
        if j > fees[0]:
            cars_fee[i] += fees[1]
            j -= fees[0]
            cars_fee[i] += math.ceil(j/fees[2])*fees[3]
        else:
            cars_fee[i] += fees[1]
    rslt = list(cars_fee.items())
    rslt.sort(key = lambda x: int(x[0]))
    for i,j in rslt:
        answer.append(j)
    return answer