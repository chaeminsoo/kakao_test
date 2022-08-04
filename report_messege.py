def solution(id_list, report, k):
    answer = [0]*len(id_list)
    id_reported = {id:0 for id in id_list}
    id_report_ppl = {id:list() for id in id_list}
    for i in report:
        er, ee = i.split()
        if ee in id_report_ppl[er]:
            pass
        else:
            id_report_ppl[er].append(ee)
            id_reported[ee] += 1
    for i,j in enumerate(id_list):
        for l in id_report_ppl[j]:
            if id_reported[l] >= k:
                answer[i] += 1
    return answer