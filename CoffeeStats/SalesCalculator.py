class SalesCalculator(object):
    """
    A Class for analyzing sales of an entity in a business relative to its hours
    of operation.
    """

    def __init__(self):
        self.sales = {}
        self.price = 4.75

    def addWeek(self, week: int, cupsSold: int, hoursOpen: int):
        self.sales['Week ' + str(week)] = {
            'cups' : cupsSold,
            'hours': hoursOpen
        }

    def getSalesRates(self) -> list:
        cupsPerHours = []
        for week in self.sales:
            cupsPerHours.append(self.sales[week]['cups'] / (self.sales[week]['hours'] * 1.0))
        return cupsPerHours

    def projectSales(self) -> float:
        cupsPerHours = self.getSalesRates()
        weeklyGrowth = []
        
        while (len(cupsPerHours) > 1):
            latest = cupsPerHours.pop()
            weeklyGrowth.append(latest - cupsPerHours[len(cupsPerHours) - 1])

        avg = 0
        for i in weeklyGrowth:
            avg += i

        return avg / (len(weeklyGrowth) * 1.0)

    @staticmethod
    def projectSalesGivenRate(cupsPerHours: float, hours: int):
        return cupsPerHours * hours






