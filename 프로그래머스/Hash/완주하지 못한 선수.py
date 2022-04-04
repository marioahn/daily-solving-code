def solution(participant, completion):
    answer = ''
    hash = {}
    for ele in participant:
        if not ele in hash:
            hash[ele] = 1
        else:
            hash[ele] += 1

    hash2 = {}
    for ele in completion:
        if not ele in hash2:
            hash2[ele] = 1
        else:
            hash2[ele] += 1

    for key in hash.keys():
        if not key in hash2.keys():
            answer = key
        elif hash[key] - hash2[key] == 1:
            answer = key
        
    return answer