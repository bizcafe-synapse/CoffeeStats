from openpyxl import load_workbook
from SalesCalculator import SalesCalculator
import matplotlib.pyplot as plt

def main():
    sc = SalesCalculator(4.75)
    
    # Open an Excel Workbook -> Sales sheet has data about cups sold
    wb = load_workbook(filename = 'data.xlsx')
    salesSheet = wb['Sales']
    weekColumn = 'A'  # Column A in Excel
    cupsColumn = 'B'  # Column B in Excel
    hoursColumn = 'C' # Column C in Excel

    # Parse salesSheet into SalesCalculator
    row = 2 # row 1 contains headers, don't parse those
    while (salesSheet[weekColumn + str(row)].value is not None):
        sc.addWeek(salesSheet[weekColumn + str(row)].value,
            salesSheet[cupsColumn + str(row)].value,
            salesSheet[hoursColumn + str(row)].value)
        row += 1

    # Plot Projected Cup Sales
    plt.xlabel('Week')
    plt.ylabel('Cups Per Hours')
    plt.title("Hourly Sales Projection")

    rates = sc.getSalesRates()
    
    for i, rate in enumerate(rates): # Add plot points for each week's sales
        plt.plot([i + 1], [rate], 'ro')
        plt.annotate(str(rate), (i + 1, rate))

    projectedValue = rates[len(rates) - 1] + sc.projectSales() # projection for next week's sale
    plt.plot([len(rates) + 1], [projectedValue], 'bo')
    plt.annotate("Projected: {:.2f}".format(projectedValue), (len(rates), projectedValue))

    plt.show()

    # Project num cups sold for upcoming week
    projectedHours = eval(input("How many hours will the cafe be open next week? "))
    print("Projected Cup Sales: {:.2f}".format(sc.projectSalesGivenRate(projectedValue, projectedHours)))

main()
