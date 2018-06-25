from django.db import models
import datetime
from .DataModels import Request_Spending, Request_BudgetRegularSpending, SpendingDataColumn,SpendingDataRow
from .Helpers import getClassColorForValue, getFormatColumn, getPlusButton

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
        return self.columnNames
    def getRows(self):
        return self.rows

class HorizontalBarItem_Budget(HorizontalBarItem):
    def getHref(self):
        return "userBudget"
    def getName(self):
        return "Budget"
    def getText(self):
        return self.getTopBar() + self.getRegularSpendingTable() + self.getOcasionalSpendingTable() + self.getSavingsTable()
    def getTopBar(self):
        # this bar contains:
        # 1- the month selector
        # 2- button to create a new spending category (i.e. regular spending, savings, etc)
        # 3- button to create a new spending entry (i.e. )
        topBarData = "<div class=\"row\">"
        topBarData += getFormatColumn(self.getMonthSelector(), 1, self.js_getMonthSelectorId())
        topBarData += getFormatColumn(getPlusButton(self.js_getNewCategoryButtonId()), 1, "") #button directly referenced
        topBarData += "</div>"
        return topBarData
    # named "js_ indicates that this value will be referenced from some js script"
    def js_getMonthSelectorId(self):
        return "monthSelectorDivId"
    def js_getNewCategoryButtonId(self):
        return "js_newCategoryButton"
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
    def js_getOcasionalSpendingDataId(self):
        return "userBudgetOcasionalSpendingTable"
    def getOcasionalSpendingTable(self):
        return "<h2>Ocasional Spending</h2>" + self.getDataTable(self.js_getOcasionalSpendingDataId(),1)
    def js_getRegularSpendingDataId(self):
        return "userBudgetRegularSpendingTable"
    def getRegularSpendingTable(self):
        return "<h2>Regular Spending</h2>" + self.getDataTable(self.js_getRegularSpendingDataId(),2)
    def js_getSavingsDataId(self):
        return "userBudgetSavingsTable"
    def getSavingsTable(self):
        return "<h2>Savings for future</h2>" + self.getDataTable(self.js_getSavingsDataId(),3)
    def getDataTable(self, tableId, tableDataId):
        tableData = self.getBudgetBaseTableHeader(tableId)
        for eachRow in Request_BudgetRegularSpending().getRows(tableDataId):
            tableData += "<tr>"
            # keep track of button ids to register the appropiate js event
            # we'll need to display a form to support manual addition of spending events
            plusButtonId = "js_plusButtonId_{}_{}".format(eachRow.name,tableDataId)
            plusButtonId.replace(" ","-")
            tableData += "<th>{}{}</th>".format(eachRow.name, getPlusButton(plusButtonId))
            tableData += "<th>{}</th>".format(eachRow.assigned)
            tableData += "<th>{}</th>".format(eachRow.budgetActual)

            availableValueColor = getClassColorForValue(eachRow.available, 0, 0) # good or bad
            tableData += "<th class=\"{}\">{}</th>".format(availableValueColor,eachRow.available)
            
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