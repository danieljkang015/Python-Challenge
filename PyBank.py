import os
import csv
import numpy as np

budget_data_csv = os.path.join('..', 'PyBank', 'budget_data.csv')

total_months = 0
total_revenue = 0
prev_revenue = 0
change_in_profit = []
greatest_decr = ['', 0]
greatest_incr = ['', 0]

with open(budget_data_csv,newline="") as budget_data:
    reader = csv.reader(budget_data)

    header = next(reader)
    total_months += 1
    first_month = next(reader)
    total_revenue += prev_revenue
    prev_revenue = int(first_month[1])

    for row in reader:
        total_months += 1
        total_revenue += int(row[1])
        rev_change = int(row[1])- prev_revenue
        prev_revenue = int(row[1])
        change_in_profit += [rev_change]

        if rev_change>greatest_incr[1]:
            greatest_incr[1]=rev_change
            greatest_incr[0]=row[0]
        if rev_change<greatest_decr[1]:
            greatest_decr[1]=rev_change
            greatest_decr[0]=row[0]


avg_change = round(sum(change_in_profit)/len(change_in_profit), 2)

print(f'Financial Analysis')
print(f'---------------------------')
print(f'Total Months: {str(total_months)}')
print(f'Total: $ {str(total_revenue)}')
print(f'Average Change: $ {str(avg_change)}')
print(f'Greatest Increase in Profits: {str(greatest_incr)}')
print(f'Greatest Decrease in Profits: {str(greatest_decr)}')