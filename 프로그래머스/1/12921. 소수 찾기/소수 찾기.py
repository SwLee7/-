def solution(n):
    answer = 0
    isPrime = [True] * (n+1)
    for i in range(2, n+1):              
        if isPrime[i] == True:           
            for j in range(i+i,n+1,i):    
                isPrime[j] = False
    
    for i in range(2,n+1):
        if(isPrime[i] == True):         
            answer +=1
    return answer