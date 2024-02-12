def solution(n, arr1, arr2):
    answer = []
    
    for a,b in zip(arr1, arr2):
        result = bin(a|b)[2:]
        
        if len(result) < n:
            result = "0" * (n-len(result)) + result
        result = result.replace("0", " ").replace("1", "#")
        answer.append(result)
    return answer