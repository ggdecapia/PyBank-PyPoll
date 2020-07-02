import os 
import csv 

csv_pathname = os.path.join('Resources', 'budget_data.csv')

#def process_budget(budget_data):
#    print(budget_data)
    

with open(csv_pathname) as csv_filename:
    csv_budget_data = csv.reader(csv_filename, delimiter=',')

    # initialization of numeric values
    total_no_of_mos = 0
    net_total = 0
    change_total = 0
    greatest_decrease = 0
    greatest_increase = 0

    budget_header = next(csv_budget_data)
    
    for row in csv_budget_data:
        #read each row of budget data
        #process_budget(row)

        # computation of number of months
        total_no_of_mos = total_no_of_mos + 1

        # computation of net Profit/Losses
        net_total = net_total + int(row[1])

        if total_no_of_mos == 1:
            # store the Profit/Loss value at row#1
            prev_amount = int(row[1])
        else:
            # store the Profit/Loss value of the current row
            curr_amount = int(row[1])

            change = curr_amount - prev_amount

            # evaluate if current month minus previous month value is an increase or a decrease
            if change < 0:
                if change < greatest_decrease:
                    # stores change amount and month if greater than what's already stored
                    greatest_decrease = change
                    greatest_decrease_month = row[0]
            else:
                if change > greatest_increase:
                    # stores change amount and month if less than what's already stored                    
                    greatest_increase = change
                    greatest_increase_month = row[0]

            # computation of change total
            change_total = change_total + change

            # move amount of current row to previous amount holder for next row evaluation
            prev_amount = curr_amount
                
    # computation of average changes over the entire period
    average_changes = change_total / (total_no_of_mos - 1)

    # print analysis
    print()
    content =  "Financial Analysis" + "\n" 
    content += "----------------------------" + "\n" 
    content += "Total Months : " + str(total_no_of_mos) + "\n" 
    content += "Total : $" + str(net_total) + "\n" 
    content += "Average Change : $" + str(average_changes) + "\n" 
    content += "Greatest Increase in Profits : " + greatest_increase_month + " (" +"$" + str(greatest_increase) + ")" + "\n" 
    content += "Greatest Decrease in Profits : " + greatest_decrease_month + " (" +"$" + str(greatest_decrease) + ")"
    print(content)


    output_pathname = os.path.join('analysis', 'budget_analysis.txt')
    with open(output_pathname, 'w') as budget_filename:
        budget_filename.write(content)