# Dependencies
import csv
import os

# Files to load and output 

# Track various financial parameters
total_months = 0
preview_revenue = 0
month_of_change = []
Revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_Revenue = 0
total_net = 0
net_change_list = 0

# Read the csv and convert it into a list of dictionaries
with open('C:/Users/pks/Desktop/NUCHI201908DATA2/Homework1/Prework_PKS/Submitted/03-python-challenge/PyBank/budget_data.csv') as csv_file:
    reader = csv.reader(csv_file)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Track the net change
        Revenue_change = int(row[1]) - preview_revenue
        prev_Revenue = int(row[1])
        Revenue_change_list = net_change_list + Revenue_change
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if (Revenue_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = Revenue_change

        # Calculate the greatest decrease
        if Revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = Revenue_change

# Calculate the Average Net Change
Revenue_monthly_avg = Revenue_change_list / total_months
# Generate Output Summary
output = (
    "\nProfit/Losses Analysis\n"
    "----------------------------\n"
    "Total Months:" +str(total_months)+"\n"
    "Total Revenue:" +str(total_net)+"\n"
    "Average  Change:"+str(Revenue_monthly_avg)+"\n"
    "Greatest Increase in Profits:"+ ''.join(str(s) for s in greatest_increase)+"\n"
    "Greatest Decrease in Profits:"+ ''.join(str(s) for s in greatest_decrease)+"\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open('C:/Users/pks/Desktop/NUCHI201908DATA2/Homework1/Prework_PKS/Submitted/03-python-challenge/PyBank/budget_analysis_1.txt', "w") as txt_file:
    txt_file.write(output)
