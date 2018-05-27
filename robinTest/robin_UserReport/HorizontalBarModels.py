from django.db import models

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

class HorizontalBarItem_Budget(HorizontalBarItem):
    def getHref(self):
        return "userBudget"
    def getName(self):
        return "Budget"
    def getText(self):
        userBudgetDetails = "Budget details:"
        return userBudgetDetails
    def getTextSelectedByDefault(self):
        return "in " + self.getSelectedByDefault()
    def getSelectedByDefault(self):
        return "active"

class HorizontalBarItem_Tools(HorizontalBarItem):
    def getHref(self):
        return "userTools"
    def getName(self):
        return "Tools"
    def getText(self):
        return "To display various tools. Section details TBD."