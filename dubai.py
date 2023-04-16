








"""
def runways_required(arrival_time, departure_time, no_of_planes):
    arrival_time.sort()
    departure_time.sort()
    
    i = j = count = max_count = 0
    
    while i < no_of_planes and j < no_of_planes:
        if arrival_time[i] < departure_time[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        
        max_count = max(max_count, count)
    
    return max_count
    
    
arrival_time = list(map(int,input().split()))
departure_time = list(map(int,input().split()))
no_of_planes = int(input())

runway = runways_required(arrival_time,departure_time,no_of_planes)
print(runway)
"""













def runways_required(arrival_time, departure_time, no_of_planes):
    times=[(arrival_time[i],departure_time[i]) for i in range(no_of_planes)]
    times.sort()
    
    runways = 0
    
    current_plane=[]
    
    for time in times:
        current_plane = [plane for plane in current_plane if plane>time[0]]
        current_plane.append(time[1])
        
        runways = max(runways,len(current_plane))
    return runways
    
    
arrival_time = list(map(int,input().split()))
departure_time = list(map(int,input().split()))
no_of_planes = int(input())

runway = runways_required(arrival_time,departure_time,no_of_planes)
print(runway)