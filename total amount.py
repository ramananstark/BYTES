def calculate_total_amount(count_50, count_1, count_2, count_5):
    total_amount = count_50 * 0.5 + count_1 + count_2 * 2 + count_5 * 5
    return total_amount 
    
count_50 = int(input())
count_1 = int(input())
count_2 = int(input())
count_5 = int(input())

total_amount = calculate_total_amount(count_50, count_1, count_2, count_5)

print(total_amount)


#total amount