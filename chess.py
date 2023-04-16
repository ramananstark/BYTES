def calculate_min_moves(coordinates,size_of_board):
    x1,y1,x2,y2=coordinates
    if not(1<=x1<=size_of_board and 1<=y1<=size_of_board and
    1<=x2<=size_of_board and 1<=y2<=size_of_board):
        return -1
    if (x1==x2 and y1==y2):
        return 0
    if abs(x1-x2)%2==1 and abs(y1-y2)%2==1 :
        return 2
    elif abs(x1-x2)%2==0 and abs(y1-y2)%2==0 :
        return 2
    else:
        return 3
        
coordinates=list(map(int,input().split()))       
size_of_board = int(input())


minmoves=calculate_min_moves(coordinates,size_of_board)
print(minmoves)
    
    
#chess