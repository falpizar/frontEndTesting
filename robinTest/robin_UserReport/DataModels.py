# Backend should be able 
# to implement most of these functionalities
# as it has full access to data and its structure.
# This class may be entirely replaced by backend calls.

# for now, let's generate some random numbers!!
import random

class Request_Spending():
    # Stores user's data
    # with the required calculations
    # This class will:
    # 1) query the required data
    # 2) internally save calculations
    # 3) return saved calculations

    # using hard-coded values for now.
    # will eventually replace with data
    # coming from service requests.
    def getAvailableCash(self):
        return random.randint(0, 200)
    def getAllAccountsTotalBalance(self):
        return random.randint(-40, 300)
    def getCreditCardTotalBalance(self):
        return random.randint(-300, 0)
    def getPositiveCashTrendThreshold(self):
        # should calculate based on historical data
        # the value where we want to let the user
        # know that he is doing "right"
        return 70
    # some users want the value in a different format
    # will do calculation if required.
    # for now let's assume everything is rolled up in $
    def getExchangeSymbol(self):
        return "$"
    def getCreditLimit(self):
        # the user has some capacity for credit, based on overall balance
        return 20

class SpendingDataRow():
    name = ""
    assigned = 0.0
    budgetActual = 0.0
    available = 0.0
    def getAllData(self):
        return [self.name,'{}'.format(self.assigned), '{}'.format(self.budgetActual), '{}'.format(self.available)]
class SpendingDataColumn():
    name = ""
    size = "0"
class Request_BudgetRegularSpending():
    def getCategories(self):
        spendingCategory = SpendingDataColumn()
        spendingCategory.name="Spending category"
        spendingCategory.size="6"

        budgetCategory = SpendingDataColumn()
        budgetCategory.name="Budget"
        budgetCategory.size="2"

        actualCategory = SpendingDataColumn()
        actualCategory.name="Actual"
        actualCategory.size="2"

        availableCategory = SpendingDataColumn()
        availableCategory.name="Available"
        availableCategory.size="2"

        return [spendingCategory,budgetCategory,actualCategory,availableCategory]
    def getRows(self, tableId):
        # tableId represents the section in the budget being queried
        # i.e. it will have a value to represent ocasional\regular spending, savings for the future
        # or any other table that might be added in the future
        outputRows = []
        for x in range(0,2+tableId,1):
            someRandomData = SpendingDataRow()
            someRandomData.name = "InputCategory{}".format(x)
            someRandomData.assigned = x*1.4
            someRandomData.budgetActual = x*1.1
            someRandomData.available = x*2
            outputRows.append(someRandomData)
        return outputRows
