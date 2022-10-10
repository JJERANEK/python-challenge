# Imports
import os
import csv

# Create filepath
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read the csv and convert into lists
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    # Reads the header line in csv and stores it
    csv_header = next(csvreader)

    # Lists to store data
    months = []
    profit_loss = []
    profit_loss_change = []

    # Adds items to lists
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(float(row[1]))

    # Print header, total months, and total amount of "Profit/Losses"
    print("Financial Analysis\n")
    print("-------------------------------\n")
    print("Total Months:", len(months))
    print(f"Total: ${int(sum(profit_loss))}")

    # Tracks changes in "Profit/Losses", then finds the average change, the greateset increase, and the greatest decrease
    for value in range(1,len(profit_loss)):
        profit_loss_change.append(profit_loss[value] - profit_loss[value-1])
        avg_profit_loss = round(sum(profit_loss_change)/len(profit_loss_change), 2)
        max_profit = max(profit_loss_change)
        min_profit = min(profit_loss_change)
        max_profit_date = str(months[profit_loss_change.index(max(profit_loss_change))+1])
        min_profit_date = str(months[profit_loss_change.index(min(profit_loss_change))+1])
        

    # Prints the average change and the dates and amounts of greatest increase and decrease
    print(f"Average Change: ${avg_profit_loss}")
    print(f"Greatest Increase in Profits: {max_profit_date} (${int(max_profit)})")
    print(f"Greatest Decrease in Profits: {min_profit_date} (${int(min_profit)})")
    print("\n")

    # Exports a text file
    with open(os.path.join("Analysis","budget_data_analysis.txt"), "w+") as analysis_text:
        analysis_text.write("Financial Analysis\n")
        analysis_text.write("-------------------------------\n")
        analysis_text.write(f"Total Months: {len(months)}")
        analysis_text.write("\n")
        analysis_text.write(f"Total: ${int(sum(profit_loss))}")
        analysis_text.write("\n")
        analysis_text.write(f"Average Change: ${avg_profit_loss}")
        analysis_text.write("\n")
        analysis_text.write(f"Greatest Increase in Profits: {max_profit_date} (${int(max_profit)})")
        analysis_text.write("\n")
        analysis_text.write(f"Greatest Decrease in Profits: {min_profit_date} (${int(min_profit)})")
        analysis_text.write("\n")










