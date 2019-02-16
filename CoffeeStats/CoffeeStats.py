from openpyxl import load_workbook
from SalesCalculator import SalesCalculator
import matplotlib.pyplot as plt

def main():
    # Open an Excel Workbook -> An array of sheets
    wb = load_workbook(filename = 'data.xlsx')

    # Sales sheet has data about cups sold
    salesSheet = wb['Sales']

    # Parse The Weeks Column
    sc = SalesCalculator()
    weekColumn = 'A'
    cupsColumn = 'B'
    hoursColumn = 'C'
    row = 2
    while (salesSheet[weekColumn + str(row)].value is not None):
        sc.addWeek(salesSheet[weekColumn + str(row)].value,
            salesSheet[cupsColumn + str(row)].value,
            salesSheet[hoursColumn + str(row)].value)
        row += 1

    # Plot Cup Sales Per Hour
    print('Plotting cups per hour')
    rates = sc.getSalesRates()
    
    for i, rate in enumerate(rates):
        plt.plot([i + 1], [rate], 'ro')
        plt.annotate(str(rate), (i + 1, rate))

    projectedValue = rates[len(rates) - 1] + sc.projectSales()
    plt.plot([len(rates) + 1], [projectedValue], 'bo')
    plt.annotate("Projected: " + str(projectedValue), (len(rates), projectedValue))

    plt.xlabel('Week')
    plt.ylabel('Cups Per Hours')
    plt.show()

    projectedHours = eval(input("How many hours will the cafe be open next week? "))
    print("Projected Cup Sales", sc.projectSalesGivenRate(projectedValue, projectedHours))


main()