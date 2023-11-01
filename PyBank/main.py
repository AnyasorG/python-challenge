import os
import csv

# Define the relative file path using os.path.join
csvpath = os.path.join("..", "anyas", "Desktop", "python-challenge", "PyBank", "Resources", "budget_data.csv")

# Initialize variables
total_months = 0
total_profit_losses = 0
profit_loss_changes = []
dates = []

# Open and read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(csvreader)

    previous_profit_loss = None

    # Calculate the total number of months and net total amount of Profit/Losses
    for row in csvreader:
        total_months = total_months + 1
        profit_loss = int(row[1])
        total_profit_losses = total_profit_losses + profit_loss
        dates.append(row[0])  # Collect dates for later use

        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)

        previous_profit_loss = profit_loss

# Calculate the average change
total_changes = sum(profit_loss_changes)
average_change = total_changes / len(profit_loss_changes)

# Calculate the greatest increase and decrease
greatest_increase = max(profit_loss_changes)
greatest_increase_date = dates[profit_loss_changes.index(greatest_increase) + 1]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease) + 1]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the results to a text file
output_path = os.path.join("..", "anyas", "Desktop", "python-challenge", "PyBank", "analysis","financial_analysis.txt")
with open(output_path, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Net Total Amount of Profit/Losses: ${total_profit_losses}\n")
    text_file.write(f"Average Change: ${round(average_change, 2)}\n")  # Use round to format average_change
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print("Results have been exported to 'financial_analysis.txt'.")