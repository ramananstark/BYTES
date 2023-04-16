def pair_sum(arr,target_sum):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]+arr[j] == target_sum):
                return arr[i],arr[j]
    return -1
    
    
arr=list(map(int,input().split()))
target_sum = int(input())

pair = pair_sum(arr,target_sum)

if pair == -1:
    print(-1)
else:
    print(pair[0])
    print(pair[1])
    
    
#sum n