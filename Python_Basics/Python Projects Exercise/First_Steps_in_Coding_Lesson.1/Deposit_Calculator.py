deposit = float(input())
months = int(input())
ann_perc = float(input())
ann_interest = ann_perc / 100
acc_interest = deposit * ann_interest
month_interest = acc_interest / 12
total_sum = deposit + (months * month_interest)
print(total_sum)
