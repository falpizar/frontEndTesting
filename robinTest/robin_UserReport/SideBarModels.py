from django.db import models
from .DataModels import Request_Spending
from .Helpers import getClassColorForValue

#### side bar objects ####
#### Main interface implemented by all different
#### functionalites to allow uniform html syntax
class SideBarItem(models.Model):
    # Standalone object
    # displayed in the user's main page
    def id(self):
        return ""
    def idText(self):
        return ""
    def getAjaxUrl(self):
        return "invalidUrl"
    def getUserData(self):
        raise Exception('Invalid class. Use of base class not allowed.')
    def getText(self):
        raise Exception('Invalid class. Use of base class not allowed.')
    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return "sideBarItem"

class SideBarItem_Spending(SideBarItem):
    def id(self):
        return "spendingSideBarItemMock"
    def idText(self):
        return "spendingSideBarItemTextMock"
    def getAjaxUrl(self):
        return "spendingAjaxSidebar"
    def getUserData(self):
        userData = Request_Spending()

        availableCash = userData.getAvailableCash()
        accBalance = userData.getAllAccountsTotalBalance()
        creditCardsBalance = userData.getCreditCardTotalBalance()

        exchangeSymbol = userData.getExchangeSymbol()
        # todo: might try this with js?
        # in the end, its py or js code, just should not be here
        cashColor = getClassColorForValue(availableCash, 0, userData.getPositiveCashTrendThreshold())
        accsColor = getClassColorForValue(accBalance, 0, 0) # good or bad
        creditColor = getClassColorForValue(creditCardsBalance, 0, userData.getCreditLimit()) # may have capacity for credit

        resultMessage =  "Cash: <a class=\"" + cashColor + "\">"  + exchangeSymbol + str(availableCash) + "</a>\n"
        resultMessage += "Acc: <a class=\"" + accsColor + "\">"  + exchangeSymbol + str(accBalance) + "</a>\n"
        resultMessage += "Credit Cards: <a class=\"" + creditColor + "\">"  + exchangeSymbol + str(creditCardsBalance) + "</a>\n"

        return resultMessage 
    def getText(self):
        return "Spending"
    

class SideBarItem_Savings(SideBarItem):
    def id(self):
        return "savingsSideBarItemMock"
    def idText(self):
        return "savingsSideBarItemTextMock"
    def getAjaxUrl(self):
        return "savingsAjaxSidebar"
    def getUserData(self):
        return "Mock savings data 456"
    def getText(self):
        return "Savings"

class SideBarItem_Retirement(SideBarItem):
    def id(self):
        return "retirementSideBarItemMock"
    def idText(self):
        return "retirementSideBarItemTextMock"
    def getAjaxUrl(self):
        return "retirementAjaxSidebar"
    def getUserData(self):
        return "Mock retirement data 234 along with other stuff"
    def getText(self):
        return "Retirement"

class SideBarItem_Investing(SideBarItem):
    def id(self):
        return "investingSideBarItemMock"
    def idText(self):
        return "investingSideBarItemTextMock"
    def getAjaxUrl(self):
        return "investingAjaxSidebar"
    def getUserData(self):
        return "Mock investing data 0987. Less stuff here."
    def getText(self):
        return "Investing"

class SideBarItem_PropertyAndDebt(SideBarItem):
    def id(self):
        return "propertyDebtsSideBarItemMock"
    def idText(self):
        return "propertyDebtsSideBarItemTextMock"
    def getAjaxUrl(self):
        return "propertyAjaxSidebar"
    def getUserData(self):
        return "Mock property data. No number displayed."
    def getText(self):
        return "Property & Debt"