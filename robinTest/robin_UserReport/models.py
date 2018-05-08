from django.db import models

class ApplicationUser(models.Model):
    email_address = models.EmailField(max_length=30, primary_key=True, help_text="Email address used to register in application. Typically used to sent alerts, account updates and other news.")
    user_name = models.CharField(max_length=15, help_text="User name for login to the application. Replaces need of using long email address.")
    def get_absolute_url(self):
         return reverse('appUser', args=[str(self.id)])
    def __str__(self):
        return self.field_name

class SupportedBank(models.Model):
    bank_name = models.CharField(max_length=15, help_text="The name of an associated bank.")
    # todo: leave as text for now, but should be FileField:
    logo_id = models.CharField(max_length=2000, help_text="Path to the icon to display that corresponds to the respective bank.")
    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return "Supported Bank"


#### side bar objects ####
#### Main interface implemented by all different
#### functionalites to allow uniform html syntax
class SideBarItem(models.Model):
    # Standalone object
    # displayed in the user's main page
    id = models.CharField(max_length=15, primary_key=True, help_text="")
    idText = models.CharField(max_length=15, primary_key=False, help_text="")
    def getUserData(self):
        raise Exception('Invalid class. Use of base class not allowed.')
    def getText(self):
        raise Exception('Invalid class. Use of base class not allowed.')
    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return "sideBarItem"

class SideBarItem_Spending(SideBarItem):
    def getUserData(self):
        return "Mock spending data 123"
    def getText(self):
        return "Spending"

class SideBarItem_Savings(SideBarItem):
    def getUserData(self):
        return "Mock savings data 456"
    def getText(self):
        return "Savings"

class SideBarItem_Retirement(SideBarItem):
    def getUserData(self):
        return "Mock retirement data 234 along with other stuff"
    def getText(self):
        return "Retirement"

class SideBarItem_Investing(SideBarItem):
    def getUserData(self):
        return "Mock investing data 0987. Less stuff here."
    def getText(self):
        return "Investing"

class SideBarItem_PropertyAndDebt(SideBarItem):
    def getUserData(self):
        return "Mock property data. No number displayed."
    def getText(self):
        return "Property & Debt"

class HorizontalBarItem(models.Model):
    href = models.CharField(max_length=15, primary_key=True, help_text="")
    name = models.CharField(max_length=15, primary_key=False, help_text="")