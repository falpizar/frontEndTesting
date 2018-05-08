# Backend should be able 
# to implement most of these functionalities
# as it has full access to data and its structure.
# This class may be entirely replaced by backend calls.
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
        return 50
    def getAllAccountsTotalBalance(self):
        return 100
    def getCreditCardTotalBalance(self):
        return -50
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