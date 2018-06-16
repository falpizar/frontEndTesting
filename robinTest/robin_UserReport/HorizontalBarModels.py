from django.db import models
import datetime
from .DataModels import Request_Spending, Request_BudgetRegularSpending, SpendingDataColumn,SpendingDataRow

class HorizontalBarItem(models.Model):
    def getHref(self):
        return ""
    def getName(self):
        return ""
    def getSelectedByDefault(self):
        return "" # only one of the options will be selected by default
    def getTextSelectedByDefault(self):
        return "" # only one displayed by default
    def getText(self):
        return ""

class HorizontalBarItem_UserProfile(HorizontalBarItem):
    def getHref(self):
        return "userProfile"
    def getName(self):
        return "Profile"
    def getText(self):
        return "To display user profile. Section details TBD."

class HorizontalBarItem_Goals(HorizontalBarItem):
    def getHref(self):
        return "userGoals"
    def getName(self):
        return "Goals"
    def getText(self):
        return "To display user defined goals. Section details TBD."

class BudgetRowData():
    dataByColumn = []
    def getColumnCount(self):
        return 0
    def getData(self):
        return self.dataByColumn

class BudgetDataTable():
    columnNames = []
    rows = []
    def getTitle(self):
        return ""
    def getColumnNames(self):
        return columnNames
    def getRows(self):
        allRows = [""]

class HorizontalBarItem_Budget(HorizontalBarItem):
    def getHref(self):
        return "userBudget"
    def getName(self):
        return "Budget"
    def getText(self):
        return self.getMonthSelector() + self.getRegularSpendingData() + self.getOcasionalSpendingData() + self.getSavingsData()
    def getMonthSelector(self):
        monthName = self.getMonthName()
        return monthName
    def getTextSelectedByDefault(self):
        return "in " + self.getSelectedByDefault()
    def getSelectedByDefault(self):
        return "active"
    def getMonthName(self):
        mydate = datetime.datetime.now()
        return mydate.strftime("%B")
    def getOcasionalSpendingDataId(self):
        return "userBudgetOcasionalSpendingTable"
    def getOcasionalSpendingData(self):
        return "<h2>Ocasional Spending</h2>" + self.getDataTable(self.getOcasionalSpendingDataId(),1)
    def getRegularSpendingDataId(self):
        return "userBudgetRegularSpendingTable"
    def getRegularSpendingData(self):
        return "<h2>Regular Spending</h2>" + self.getDataTable(self.getRegularSpendingDataId(),2)
    def getSavingsDataId(self):
        return "userBudgetSavingsTable"
    def getSavingsData(self):
        return "<h2>Savings for future</h2>" + self.getDataTable(self.getSavingsDataId(),3)

    def getDataTable(self, tableId, tableDataId):
        tableData = self.getBudgetBaseTableHeader(tableId)
        for eachRow in Request_BudgetRegularSpending().getRows(tableDataId):
            tableData += "<tr>"
            for eachIndex in eachRow.getAllData():
                tableData += "<th>{}</th>".format(eachIndex)
            tableData += "</tr>"
        tableData += "</table>"
        return tableData
    def getBudgetBaseTableHeader(self, tableId):
        tableHeader = """
        <table id=\"""" + tableId + """\" class=\"table table-bordered table-responsive-md table-striped text-center\">
        <tr>"""
        for eachCategory in Request_BudgetRegularSpending().getCategories():
            tableHeader += """
            <th class=\"text-center col-sm-{size}\">{name}</th>
            """.format(size=eachCategory.size, name=eachCategory.name)
        tableHeader += "</tr>"
        return tableHeader
class HorizontalBarItem_Tools(HorizontalBarItem):
    def getHref(self):
        return "userTools"
    def getName(self):
        return "Tools"
    def getText(self):
        return "To display various tools. Section details TBD."